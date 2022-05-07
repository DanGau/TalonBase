from talon import actions

# These void(void) functions are used by AUXControllerReceiver
# and are invoked when a button is pressed or released (as appropriate).

# NOTE: These functions are invoked on a worker thread which makes them _not_ thread
# safe by default. Ideally the button actions would be marshalled to the main thread
# but talon's message pump isn't exposed to scripts loaded from the user folder.
# As such, we take the thread safety risk and invoke actions anyway. Where possible
# action implementations should be written in a thread safe way.

# Button 1 - Talon push to talk
def Button1Pressed():
    actions.speech.enable()

def Button1Released():
    actions.speech.disable()

# Button 2
def Button2Pressed():
    return

def Button2Released():
    return

# Button 3
def Button3Pressed():
    return

def Button3Released():
    return

# Button 4
def Button4Pressed():
    return

def Button4Released():
    return

# Button 5
def Button5Pressed():
    return

def Button5Released():
    return

# Button 6
def Button6Pressed():
    return

def Button6Released():
    return

# Button 7
def Button7Pressed():
    return

def Button7Released():
    return

# Button 8
def Button8Pressed():
    return

def Button8Released():
    return

# Button 9
def Button9Pressed():
    return

def Button9Released():
    return

# Button 10
def Button10Pressed():
    return

def Button10Released():
    return