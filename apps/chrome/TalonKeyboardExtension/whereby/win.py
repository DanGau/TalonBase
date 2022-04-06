from talon import Context, actions

ctx = Context()

ctx.matches = r"""
app: whereby
"""

@ctx.action_class('user')
class UserActions:
    def whereby_toggle_mute():
        actions.key('ctrl-shift-1')
    def whereby_toggle_camera():
        actions.key('ctrl-shift-4')
    def whereby_share_screen():
        actions.key('ctrl-shift-2')
    def whereby_toggle_chat():
        actions.key('ctrl-shift-3')