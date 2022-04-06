from talon import Context, actions

ctx = Context()

ctx.matches = r"""
os: windows
app: outlook
"""

# User context actions are ones defined specifically for this app
# Other strings given to action_class are overrides
@ctx.action_class('user')
class UserActions:
    # Mail Navigation
    def outlook_mark_read(): actions.key('ctrl-q')
    def outlook_mark_unread(): actions.key('ctrl-u')
    def outlook_go_to_mail(): actions.key('ctrl-1')
    def outlook_new_mail(): actions.key('ctrl-shift-m')
    def outlook_new_meeting(): actions.key('ctrl-shift-q')
    def outlook_go_to_search(): actions.key('f3')

    def outlook_rotate_pane(): actions.key('ctrl-tab')
    def outlook_counter_rotate_pane(): actions.key('ctrl-shift-tab')
    def outlook_message_move():
        actions.key('alt-h')
        actions.key('m')
        actions.key('v')

    # Mail Authoring
    def outlook_reply_all(): actions.key('ctrl-shift-r')
    def outlook_reply(): actions.key('ctrl-r')
    def outlook_forward(): actions.key('ctrl-f')
    def outlook_discard():
        actions.key('escape')
        actions.sleep("100ms")
        actions.key('tab')
        actions.key('enter')
    def outlook_message_send(): actions.key('alt-s')

    # Calendar Navigation
    def outlook_go_to_calendar(): actions.key('ctrl-2')
