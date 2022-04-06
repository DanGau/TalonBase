from talon import Module
from typing import Union

mod = Module()

#mod.apps.messenger = """
#tag: browser
#and title: Messenger - Google Chrome
#"""

mod.apps.messenger = """
tag: browser
"""
#browser.host: twitter.com

@mod.action_class
class Actions:
    def messenger_send_like():
        """Sends a link or emoji depending on chat config"""

    def messenger_chat_next(num: Union[int, str]):
        """Navigates down num chats in the left nav from the currently active chat"""
    def messenger_chat_last(num: Union[int, str]):
        """Navigates up num chats in the left nav from the currently active chat"""
    def messenger_chat_top():
        """Navigates to the top chat"""
    def messenger_chat_new():
        """Opens the new chat pane"""