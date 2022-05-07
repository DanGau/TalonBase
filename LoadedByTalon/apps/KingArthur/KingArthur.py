from talon import Module

mod = Module()

# Get the app names using ui.apps() in the REPL Window
# App(pid=14908, "King Arthur: Knight's tale")

mod.apps.KingArthur = """
os: windows
and app.name: King Arthur: Knight's tale
"""

@mod.action_class
class Actions:
    def king_arthur_level_skill():
        """Holds left mouse too level a skill"""
    