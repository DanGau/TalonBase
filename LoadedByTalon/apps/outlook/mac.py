from talon import Context, actions

ctx = Context()

ctx.matches = r"""
os: mac
app: outlook
"""

# User context actions are ones defined specifically for this app
# Other strings given to action_class are overrides
@ctx.action_class('user')
class UserActions:
    # Mail Navigation
    def outlook_mark_read(): actions.key('cmd-t')
    def outlook_mark_unread(): actions.key('cmd-shift-t')
    def outlook_go_to_mail(): actions.key('cmd-1')
    def outlook_new_mail(): actions.key('cmd-n')
    # def outlook_new_meeting(): actions.key('ctrl-shift-q')
    # def outlook_go_to_search(): actions.key('f3')

    def outlook_rotate_pane(): actions.key('f6')
    def outlook_counter_rotate_pane(): actions.key('shift-f6') # no clue if this works
    def outlook_message_move(): actions.key('cmd-shift-m')

    # Mail Authoring
    def outlook_reply_all(): actions.key('cmd-shift-r')
    def outlook_reply(): actions.key('cmd-r')
    def outlook_forward(): actions.key('cmd-j')
    # def outlook_discard():
    #     actions.key('escape')
    #     actions.sleep("100ms")
    #     actions.key('tab')
    #     actions.key('enter')
    def outlook_message_send(): actions.key('cmd-enter')

    # Calendar Navigation
    def outlook_go_to_calendar(): actions.key('cmd-2')
