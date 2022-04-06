from talon import Context, actions

ctx = Context()

ctx.matches = r"""
os: windows
app: shell
"""

@ctx.action_class('user')
class UserActions:
    #Mail Navigation
    def shell_address_bar(): actions.key('ctrl-l')