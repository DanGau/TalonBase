from talon import Module

mod = Module()

# Get the app names using ui.apps() in the REPL Window

mod.apps.shell = """
os: windows
and app.exe: explorer.exe
os: windows
and app.name: Windows Explorer
"""

@mod.action_class
class Actions:
    def shell_address_bar():
        """Navigate to the address bar"""