#pragma once

#include <windows.h>
#include <stdio.h>
#include <stdlib.h>
#include <string>

class SerialPort
{
public:
    SerialPort();
    virtual ~SerialPort();

    int Initialize(const std::string& portName);

    void ReadSerialPort(std::string& serialData) const;
    bool WriteSerialPort(const std::string& serialData) const;
    bool IsConnected() const;

private:
    HANDLE _handle;
    bool _connected;
};
