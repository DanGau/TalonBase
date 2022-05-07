from talon import Context, actions
from typing import Union

ctx = Context()

ctx.matches = r"""
os: windows
app: codeflow
"""

@ctx.action_class('user')
class UserActions:
    # Navigation
    def codeflow_next_change():
        actions.key('f8')
    def codeflow_last_change():
        actions.key('f7')
    def codeflow_next_file():
        actions.key('ctrl-f8')
    def codeflow_last_file():
        actions.key('ctrl-f7')
    def codeflow_next_comment():
        actions.key('ctrl-f11')
    def codeflow_last_comment():
        actions.key('ctrl-f12')

    # Iterations

    # Reivew
    def codeflow_show_both():
        actions.key('alt-b')
    def codeflow_show_left():
        actions.key('alt-l')
    def codeflow_show_right():
        actions.key('alt-r')

    # Comments
    def codeflow_comment_add():
        actions.ket('alt-c')
    def codeflow_comment_publish():
        actions.key('ctrl-enter')

    # Status
    def codeflow_status_approve():
        actions.key('shift-alt-a')
    def codeflow_status_suggestions():
        actions.key('shift-alt-s')
    def codeflow_status_waiting():
        actions.key('shift-alt-w')
    def codeflow_status_reset():
        actions.key('shift-alt-n')
    def codeflow_status_reject():
        actions.key('shift-alt-r')