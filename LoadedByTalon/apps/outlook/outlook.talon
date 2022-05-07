app: outlook
-

tag(): user.emoji

# Mailbox Navigation
mark read: user.outlook_mark_read()
mark unread: user.outlook_mark_unread()
go to mail: user.outlook_go_to_mail()
new mail: user.outlook_new_mail()
new meeting: user.outlook_new_meeting()
go to find: user.outlook_go_to_search()
message move: user.outlook_message_move()

landmark next: user.outlook_rotate_pane()
landmark previous: user.outlook_counter_rotate_pane()


# Mail Authoring
(message reply all | big r): user.outlook_reply_all()
(message reply | little r): user.outlook_reply()
message forward: user.outlook_forward()
discard: user.outlook_discard()
message send: user.outlook_message_send()

# To line 
# ctrl+shift+b brings up the address book window

# Calendar Navigation
go to calendar: user.outlook_go_to_calendar()