os: windows
app: KingArthur
-
# You can define certain tags to be active when this context is active

# movin around
move: mouse_click(1)
use: mouse_click(0)
loot: mouse_click(0)

# other stuff
open map: key(m)
continue: key(escape)

# inventory screen
level skill: user.king_arthur_level_skill()
learn skill: user.king_arthur_level_skill()
equip: mouse_click(1)

# combat
attack: mouse_click(0)
skill <user.number_key>: key(number_key)
cancel: key(escape)
end turn: key(ctrl-enter)

# Mapping of speech commands into python files.
# 
# [foo]	Optional
# foo*	Zero or more
# foo+	One or more
# foo|bar	Choice
# (foo)	Precedence/grouping
#mark read: user.app_action_name()  eg