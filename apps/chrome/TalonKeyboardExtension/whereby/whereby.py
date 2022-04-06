from talon import Module

mod = Module()

mod.apps.whereby = """
tag: browser
"""

@mod.action_class
class Actions:
    def whereby_toggle_mute():
        """Toggles mute"""
    def whereby_toggle_camera():
        """Toggles the camera"""
    def whereby_share_screen():
        """Opens the screen share pane"""
    def whereby_toggle_chat():
        """Toggles the chat window"""