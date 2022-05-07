from talon import Module

mod = Module()

# Get the app names using ui.apps() in the REPL Window

mod.apps.helloWorld = """
os: windows
and app.exe: helloworld.EXE
"""

mod.apps.helloWorld = """
os: windows
and app.name: Hello World
"""

@mod.action_class
class Actions:
    def app_action_name():
        """Does a thing"""
    