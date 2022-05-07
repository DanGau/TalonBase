from talon import Module

mod = Module()

mod.apps.bing = """
tag: browser
"""

@mod.action_class
class Actions:
    def bing_search(searchText: str):
        """Searches bing for the given text"""