#include "stdafx.h"

#include "SerialPort.h"
#include <vector>

SerialPort::SerialPort() :
    _connected(false),
    _handle(nullptr)
{
}

SerialPort::~SerialPort()
{
    if (_connected)
    {
        _connected = false;
        CloseHandle(_handle);
    }
}

int SerialPort::Initialize(const std::string& portName)
{
    _connected = false;
    int error = ERROR_SUCCESS;

    _handle = CreateFileA(
        portName.c_str(),
        GENERIC_READ | GENERIC_WRITE,
        0,
        NULL,
        OPEN_EXISTING,
        FILE_ATTRIBUTE_NORMAL,
        NULL);

    if ((_handle == INVALID_HANDLE_VALUE) || (_handle == nullptr))
    {
        error = GetLastError();

        if (error == ERROR_FILE_NOT_FOUND)
        {
            printf("Handle was not attached. Reason: %s not available\n", portName.c_str());
        }
        else
        {
            printf("Unknown error: %d", error);
        }
    }
    else
    {
        DCB dcbSerialParameters = { 0 };

        if (GetCommState(_handle, &dcbSerialParameters))
        {
            dcbSerialParameters.BaudRate = CBR_9600;
            dcbSerialParameters.ByteSize = 8;
            dcbSerialParameters.StopBits = ONESTOPBIT;
            dcbSerialParameters.Parity = NOPARITY;
            dcbSerialParameters.fDtrControl = DTR_CONTROL_ENABLE;

            if (SetCommState(_handle, &dcbSerialParameters))
            {
                _connected = true;
                PurgeComm(_handle, PURGE_RXCLEAR | PURGE_TXCLEAR);
                Sleep(2000);
            }
            else
            {
                error = -2; // Custom error code to help debug
            }
        }
        else
        {
            error = -1; // Custom error code to help debug
        }
    }

    return error;
}

void SerialPort::ReadSerialPort(std::string& serialData) const
{
    DWORD bytesRead = 0;
    std::vector<char> buffer;

    DWORD errors = 0;
    COMSTAT status = {};
    ClearCommError(_handle, &errors, &status);

    if (status.cbInQue > 0)
    {
        buffer.resize(status.cbInQue);

        const bool success = !!ReadFile(_handle, buffer.data(), status.cbInQue, &bytesRead, nullptr);

        if (success)
        {
            serialData.assign(buffer.begin(), buffer.end());
        }
        else
        {
            const int error = GetLastError();
            printf("ReadFile failed. Error: %d", error);
        }
    }
}

bool SerialPort::WriteSerialPort(const std::string& serialData) const
{
    DWORD bytesSend = 0;
    bool success = false;

    if (!WriteFile(_handle, serialData.c_str(), serialData.size(), &bytesSend, 0))
    {
        DWORD errors = 0;
        COMSTAT status = {};
        ClearCommError(_handle, &errors, &status);
    }

    return success;
}

bool SerialPort::IsConnected() const
{
    return _connected;
}