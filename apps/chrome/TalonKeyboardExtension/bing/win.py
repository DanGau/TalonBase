from talon import Context, actions

# This appends the parent of this file's containing folder to the search paths
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from WebServerFileHelper import SetExtensionJSONNode

import json

ctx = Context()

ctx.matches = r"""
app: bing
"""

@ctx.action_class('user')
class UserActions:
    def bing_search(searchText: str):
        # Push the search text into the bing node.
        # If an app has more than one field, the existing data can be retrieved via GetExtensionJSONNode
        SetExtensionJSONNode('bing', {'searchText': searchText})

        # Invoke the extension to handle the rest
        actions.key('ctrl-shift-1')
