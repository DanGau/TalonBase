#include "stdafx.h"

#include "SerialPort.h"
#include "SerialPortInterface.h"

SerialPort g_serialPort;

int Initialize(char* pPortName)
{
    std::string portName(pPortName);

    return g_serialPort.Initialize(portName);
}

char* ReadSerialPort()
{
    std::string serialData;

    if (g_serialPort.IsConnected())
    {
        g_serialPort.ReadSerialPort(serialData);
    }
    else
    {
        printf("No connection to SerialPort. Call Initialize first.");
    }

    // Python doesn't easily use pointers, so we always return a value
    // rather than nullptr
    return _strdup(serialData.c_str());
}

// String allocated by SerialPortInterface need to be released in the same heap.
// We can't (or at least I don't want to find out how to) pass a SAFEARRAY
// to Python, so instead we provide the free functionality and expect that
// strings allocated and later freed by the caller.
void FreeString(char* pStr)
{
    delete pStr;
}
