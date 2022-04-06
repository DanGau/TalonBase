from .user_settings import read_mapping_from_csv
from talon import Module, Context, actions, app

mod = Module()
mod.list("file_extension", desc="A file extension, such as .py")

file_extensions = read_mapping_from_csv(
    "file_extensions.csv",
    expectedHeaders=("File extension", "Name")
)

ctx = Context()
ctx.lists["self.file_extension"] = file_extensions