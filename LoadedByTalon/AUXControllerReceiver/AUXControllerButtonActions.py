from talon import actions
import logging

# These void(void) functions are used by AUXControllerReceiver
# and are invoked when a button is pressed or released (as appropriate).

# NOTE: These functions are invoked on a worker thread which makes them _not_ thread
# safe by default. Ideally the button actions would be marshalled to the main thread
# but talon's message pump isn't exposed to scripts loaded from the user folder.
# As such, we take the thread safety risk and invoke actions anyway. Where possible
# action implementations should be written in a thread safe way.

# Button 1 - Talon push to talk
def Button1Pressed():
    logging.warning("AUX Controller Button 1 Pressed")
    actions.speech.enable()

def Button1Released():
    logging.warning("AUX Controller Button 1 Released")
    actions.speech.disable()

# Button 2
def Button2Pressed():
    logging.warning("AUX Controller Button 2 Pressed")
    return

def Button2Released():
    logging.warning("AUX Controller Button 2 Released")
    return

# Button 3
def Button3Pressed():
    logging.warning("AUX Controller Button 3 Pressed")
    return

def Button3Released():
    logging.warning("AUX Controller Button 3 Released")
    return

# Button 4
def Button4Pressed():
    logging.warning("AUX Controller Button 4 Pressed")
    return

def Button4Released():
    logging.warning("AUX Controller Button 4 Released")
    return

# Button 5
def Button5Pressed():
    logging.warning("AUX Controller Button 5 Pressed")
    return

def Button5Released():
    logging.warning("AUX Controller Button 5 Released")
    return

# Button 6
def Button6Pressed():
    logging.warning("AUX Controller Button 6 Pressed")
    return

def Button6Released():
    logging.warning("AUX Controller Button 6 Released")
    return

# Button 7
def Button7Pressed():
    logging.warning("AUX Controller Button 7 Pressed")
    return

def Button7Released():
    logging.warning("AUX Controller Button 7 Released")
    return

# Button 8
def Button8Pressed():
    logging.warning("AUX Controller Button 8 Pressed")
    return

def Button8Released():
    logging.warning("AUX Controller Button 8 Released")
    return

# Button 9
def Button9Pressed():
    logging.warning("AUX Controller Button 9 Pressed")
    return

def Button9Released():
    logging.warning("AUX Controller Button 9 Released")
    return

# Button 10
def Button10Pressed():
    logging.warning("AUX Controller Button 10 Pressed")
    return

def Button10Released():
    logging.warning("AUX Controller Button 10 Released")
    return