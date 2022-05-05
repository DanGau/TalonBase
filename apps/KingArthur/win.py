from talon import (
    Context,
    Module,
    actions,
    ctrl
)
ctx = Context()

ctx.matches = r"""
os: windows
and app.name: King Arthur: Knight's tale
"""

# User context actions are ones defined specifically for this app
# Other strings given to action_class are overrides
@ctx.action_class('user')
class UserActions:
    def king_arthur_level_skill(): 
        # Start drag
        ctrl.mouse_click(button=0, down=True)
        actions.sleep("1000ms")
        ctrl.mouse_click(button=0, up=True)
