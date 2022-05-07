from talon import Context, actions

ctx = Context()

ctx.matches = r"""
os: mac
app: Xcode
"""

# User context actions are ones defined specifically for this app
# Other strings given to action_class are overrides
@ctx.action_class('user')
class UserActions:
    def xcode_open_file(): actions.key('cmd-shift-o')
    def xcode_find_in_files(): actions.key('cmd-shift-f')
    def xcode_jump_to_line(lineNumber: int):
        actions.key("cmd-l")
        actions.sleep("100ms")
        actions.insert(str(lineNumber))
        actions.key("enter")
    def xcode_swap_between_headder_and_implementation(): actions.key('ctrl-cmd-up')
    def xcode_debugger_step_over(): actions.key('f6')
    def xcode_debugger_step_into(): actions.key('f7')
    def xcode_debugger_step_out(): actions.key('f8')
    def xcode_debugger_continue(): actions.key('ctrl-cmd-y')
        