from talon import Module
from pathlib import Path

mod = Module()

# Get the app names using ui.apps() in the REPL Window

mod.apps.xcode = """
os: mac
and app.name: XCode
"""

### Find a way to get this in another file
AutoGenPath = str(Path(__file__).parent) + '/xcode_Autogen.talon'
AutoGenHeader = """app: XCode
-
"""

with open(AutoGenPath, 'w+') as autoGenFile:
    autoGenFile.write(AutoGenHeader)


def mapCommand(speechCommand):
    def wrapper(f):
        with open(AutoGenPath, "a") as autoGenFile:
            autoGenFile.write(speechCommand + ": user." + f.__name__ + "()\n")
        return f
    return wrapper

### ------------------------------ ###


@mod.action_class
class Actions:
    @mapCommand("open file")
    def xcode_open_file():
        """Opens fuzzy search to open a file"""

    @mapCommand("hunt all")
    def xcode_find_in_files():
        """Opens a search of the project"""

    def xcode_jump_to_line(lineNumber: int):
        """Jumps to the line number passed in"""

    @mapCommand("open header")
    @mapCommand("open implementation") 
    def xcode_swap_between_headder_and_implementation():
        """Swaps between .cpp and .h files"""

    @mapCommand("debug step")
    def xcode_debugger_step_over():
        """debugger step over"""

    @mapCommand("debug step into")
    def xcode_debugger_step_into():
        """debugger step into"""

    @mapCommand("debug step out")
    def xcode_debugger_step_out():
        """debugger step out"""

    @mapCommand("debug continue")
    def xcode_debugger_continue():
        """debugger continue"""
    
    # to do
    # Add and remove breakpoints
    # Go to definition
    # Go to next and previous error
    # Fold and unfold code (aka minimizing functions)
    # Move line up/down
    # Build, build and run, run    
