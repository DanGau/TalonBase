from talon import Module

mod = Module()

# Get the app names using ui.apps() in the REPL Window

mod.apps.outlook = """
os: windows
and app.exe: OUTLOOK.EXE
"""

mod.apps.outlook = """
app.name: Microsoft Outlook
"""

@mod.action_class
class Actions:
    # Mail Navigation
    def outlook_mark_read():
        """Marks a message read"""
    def outlook_mark_unread():
        """Marks a message unread"""
    def outlook_go_to_mail():
        """Navigates to the mail pane"""
    def outlook_new_mail():
        """Creates a new mail"""
    def outlook_new_meeting():
        """Creates a new meeting"""
    def outlook_go_to_search():
        """Navigate to the search bar"""

    def outlook_rotate_pane():
        """Rotates between the outlook panes"""
    def outlook_counter_rotate_pane():
        """Counter rotate between the outlook panes"""
    def outlook_message_move():
        """Opens the move to pane"""

    # Mail Authoring
    def outlook_reply_all():
        """Replies all to the currently highlighted message"""
    def outlook_reply():
        """Replies to the currently highlighted message"""
    def outlook_forward():
        """Forwards the currently highlighted message"""
    def outlook_discard():
        """Discards the current item without saving"""
    def outlook_message_send():
        """Sends the current message"""

    # Calendar Navigation
    def outlook_go_to_calendar():
        """Navigates to the calendar pane"""