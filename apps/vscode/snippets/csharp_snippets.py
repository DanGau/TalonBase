from talon import Context, actions, ui, Module, app
import os

ctx = Context()
ctx.matches = r"""
app: vscode
tag: user.csharp
"""
# short name -> ide clip name
ctx.lists["user.snippets"] = {
    "class": "class",
    "else": "else",
    "for each": "foreach",
    "if": "if",
    "try except": "try",
    "try finally": "tryf",
    "while": "while",
    # "class funky": "def(class method)",
    # "class static funky": "def(class static method)",
    # "for": "for",
    # "funky": "def",
}