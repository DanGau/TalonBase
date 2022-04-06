from talon import Context, actions, Module
from collections import Counter

mod = Module()
ctx = Context()
ctx.matches = r"""
os: windows
app: Microsoft Visual Studio 2019
app: devenv.exe
"""

@mod.action_class
class Actions:
    def add_line_breaks_to_method():   
        """Add"""     
        # Determine number of parameters in this signature 
        actions.edit.line_start()
        text = actions.edit.selected_text()  
        characterCounts = Counter(text)
        
        if characterCounts['('] > 0:
            # Line break the first parameter 
            actions.user.select_next_occurrence('(')
            actions.user.paste("(")
            actions.key('enter')

        # Line break each comma
        for j in range(0,characterCounts[',']):
            actions.user.select_next_occurrence(',')
            actions.user.paste(",")
            actions.key('enter')

        # Go to the line end and create an extra line break
        actions.edit.line_end()
        actions.key('enter')