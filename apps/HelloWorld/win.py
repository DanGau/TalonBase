from talon import Context, actions

ctx = Context()

ctx.matches = r"""
os: windows
app: helloWorld
"""

# User context actions are ones defined specifically for this app
# Other strings given to action_class are overrides
@ctx.action_class('user')
class UserActions:
    def app_action_name(): actions.key('ctrl-q')
