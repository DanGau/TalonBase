# Context header- defines under which circumstances this file applies.
os: windows
app: helloWorld

# Anything below the dash is part of the body.
# If there is no dash, then the body starts immediately.
-

# You can define certain tags to be active when this context is active
tag(): user.emoji

# Mapping of speech commands into python files.
# 
# [foo]	Optional
# foo*	Zero or more
# foo+	One or more
# foo|bar	Choice
# (foo)	Precedence/grouping
mark read: user.app_action_name()