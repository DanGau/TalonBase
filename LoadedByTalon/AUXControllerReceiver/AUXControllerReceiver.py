# This is a file used to connect to an arduino over the serial port
# Including libraries into talon can cause issues, so instead we use a custom implementation
# of a serial interface. See the SerialPortInterface for details.

# This is a windows only implementation, the underlying IO needs to be investigated for macOS

import ctypes
import logging
import os
import pathlib
import threading
import time

from .AUXControllerButtonActions import *
from talon import app

# Flag helpers
def IsFlagSet(mask: int, flag: int) -> bool:
    return (mask & flag) == flag

def SetFlag(mask: int, flag: int) -> int:
    return mask | flag

def ClearFlag(mask: int, flag: int) -> int:
    return mask & ~flag

# Initialization of the CPython code
def CreateConnection() -> ctypes.CDLL:
    # Make sure the dll matches the bitness of Talon (probably 64-bit)
    auxReceiverDllPath = os.path.join(pathlib.Path(__file__).parent.resolve(), "SerialPortInterface.dll")

    # Load the DLL and define the signatures. Methods are from SerialPortInterface.cpp
    auxReceiver = ctypes.CDLL(auxReceiverDllPath)

    # int Initialize(char* pPortName)
    auxReceiver.Initialize.restype = ctypes.c_int
    auxReceiver.Initialize.argtypes = [ctypes.POINTER(ctypes.c_char)]

    # char* ReadSerialPort()
    auxReceiver.ReadSerialPort.restype = ctypes.POINTER(ctypes.c_char)

    # void FreeString(char* pStr)
    auxReceiver.FreeString.argtypes = [ctypes.POINTER(ctypes.c_char)]

    # Initialize the connection on the COM port
    # The Arduino seems to always connect on COM3. If this changes with any regularity,
    # this will have to be made configurable.
    error = auxReceiver.Initialize(b"COM3")
    if error != 0:
        print(error)

    return auxReceiver

# Helper struct used to organize button mask, flag, and actions
class ButtonAction:
    def __init__(self, mask, flag, onPress, onRelease):
        self.mask = mask
        self.flag = flag
        self.onPress = onPress
        self.onRelease = onRelease

# This function loops infinitely. It is designed to be run by a daemon thread
def ReadConnectionLoop(auxReceiver: ctypes.CDLL):
    currentState = 0

    buttonActions = [
        ButtonAction(0x80, 0x1, Button1Pressed, Button1Released),
        ButtonAction(0x80, 0x2, Button2Pressed, Button2Released),
        ButtonAction(0x80, 0x4, Button3Pressed, Button3Released),
        ButtonAction(0x80, 0x8, Button4Pressed, Button4Released),
        ButtonAction(0x80, 0x10, Button5Pressed, Button5Released),
        ButtonAction(0x80, 0x20, Button6Pressed, Button6Released),
        ButtonAction(0x40, 0x100, Button7Pressed, Button7Released),
        ButtonAction(0x40, 0x200, Button8Pressed, Button8Released),
        ButtonAction(0x40, 0x400, Button9Pressed, Button9Released),
        ButtonAction(0x40, 0x800, Button10Pressed, Button10Released)]

    while True:
        cString = auxReceiver.ReadSerialPort()
        returnedBuffer = ctypes.c_char_p.from_buffer(cString).value

        # Go through each byte written to the serial port
        for byte in returnedBuffer:
            # Look for changes in each button state
            for buttonAction in buttonActions:
                # Filter to the buttons that are related to the given mask (high order bits)
                # The mask is used as we want to transfer more button state than is available
                # if a since byte.
                if IsFlagSet(byte, buttonAction.mask):
                    # currentState tracks the state across all masks, so some masks need to be
                    # bit shifted to an open part of the mask.
                    if IsFlagSet(byte, 0x40): # Byte 2
                        byte = byte << 8

                    flag = buttonAction.flag
                    # Key was active, now released
                    if IsFlagSet(currentState, flag) and not IsFlagSet(byte, flag):
                        buttonAction.onRelease()
                        currentState = ClearFlag(currentState, flag)
                    # Key was not active, now pressed
                    elif not IsFlagSet(currentState, flag) and IsFlagSet(byte, flag):
                        buttonAction.onPress()
                        currentState = SetFlag(currentState, flag)

        # The native binary allocates strings on the heap for use in python
        # but they can't be cleaned up from python so we call FreeString
        # which acts as a custom implementation of free for string data
        # returned by other functions exposed by auxReceiver.
        auxReceiver.FreeString(cString)

        # We don't need lightning fast response rates, so we add a 200ms delay to
        # parsing the input provided by the AUX controller to avoid CPU load.
        time.sleep(.2)

def AuxListener():
    auxReceiver = CreateConnection()
    ReadConnectionLoop(auxReceiver)

hasStartedListenerThread = False

def StartAuxControllerReceiver():
    global hasStartedListenerThread

    if not hasStartedListenerThread:
        # Only start one Daemon thread per process lifetime.
        hasStartedListenerThread = True

        # Spawned as a daemon thread so it'll exit when the main thread exits without
        # needing to join. This is useful so we can run an infinite loop on the listener
        # thread without needing to listen to app close events.
        listenerThread = threading.Thread(target=AuxListener, args=(), daemon=True)
        listenerThread.start()

        logging.warning("The stack trace in the log window above can be ignored. This thread is being created knowingly.")

# Wait until Talon indicates it's ready before starting the daemon thread.
app.register("ready", StartAuxControllerReceiver)