app: codeflow
-

# I wrote this skeleton on my home machine without testing it, so it needs to be vetted
# I pulled the key bindings from the help menu, but not all seem to work and I didn't
# test all of them.

# Navigation
change next: user.codeflow_next_change()
change last: user.codeflow_last_change()
file next: user.codeflow_next_file()
file last: user.codeflow_last_file()
comment next: user.codeflow_next_comment()
comment last: user.codeflow_last_comment()
# go to find: user.codeflow_go_to_find()

# Iterations
# iteration <user.number_key>: user.codeflow_iteration_num(number_key)
# diff iteration <user.number_key> and <user.number_key>: user.codeflow_iteration_diff(number_key, number_key)

# Review
show both: user.codeflow_show_both()
show left: user.codeflow_show_left()
show right: user.codeflow_show_right()

# Comments
comment add: user.codeflow_comment_add()
comment publish: user.codeflow_comment_publish()
# comment resolved: user.codeflow_comment_resolve()
# comment active: user.codeflow_comment_active()
# comment pending: user.codeflow_comment_pending()
# comment closed: user.codeflow_comment_closed()
# comment won't fix: user.codeflow_comment_wontfix()

# Status
status approve: user.codeflow_status_approve()
status suggestions: user.codeflow_status_suggestions()
status waiting: user.codeflow_status_waiting()
status reset: user.codeflow_status_reset()
status reject: user.codeflow_status_reject()