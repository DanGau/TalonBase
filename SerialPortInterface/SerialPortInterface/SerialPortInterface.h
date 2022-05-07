#pragma once

// These are the functions exposed by the DLL.
// extern "C" is needed to prevent name mangling so CPython can invoke the functions.
extern "C" __declspec(dllexport) int Initialize(char* pPortName);
extern "C" __declspec(dllexport) char* ReadSerialPort();
extern "C" __declspec(dllexport) void FreeString(char* pStr);
