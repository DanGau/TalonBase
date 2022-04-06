from talon import Context, actions
from typing import Union

# This doesn't work
# ctx = Context('messenger', func = lambda app, win: win.title.endswith('Messenger - Google Chrome'))

ctx = Context()

#ctx.matches = r"""
#app: messenger
#"""

ctx.matches = r"""
app: messenger
"""

@ctx.action_class('user')
class UserActions:
    # Chat pane
    def messenger_send_like():
        actions.key('ctrl-shift-1')

    # Chat navigation
    def messenger_chat_next(num: Union[int, str]):
        for i in range(int(num)):
            actions.key('ctrl-shift-2')
            actions.sleep("300ms")

    def messenger_chat_last(num: Union[int, str]):
        for i in range(int(num)):
            actions.key('ctrl-shift-3')
            actions.sleep("300ms")

    def messenger_chat_top():
        actions.key('ctrl-shift-5')
        
    def messenger_chat_new():
        actions.key('ctrl-shift-4')
