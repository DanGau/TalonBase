tag: browser
browser.host: www.messenger.com
-

# Message pane
send like: user.messenger_send_like()

# Chat list navigation
chat next: user.messenger_chat_next(1)
chat next <user.number_key>: user.messenger_chat_next(number_key)

chat last: user.messenger_chat_last(1)
chat last <user.number_key>: user.messenger_chat_last(number_key)

chat top: user.messenger_chat_top()
chat new: user.messenger_chat_new()
