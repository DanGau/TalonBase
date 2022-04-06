from .user_settings import read_mapping_from_csv
from talon import Module, Context
from urllib.parse import quote_plus
import webbrowser

mod = Module()
mod.list("website", desc="A website.")
mod.list(
    "search_engine",
)
ctx = Context()
ctx.lists["self.website"] = read_mapping_from_csv(
    "websites.csv",
    expectedHeaders=("URL", "Spoken name")
)
ctx.lists["self.search_engine"] = read_mapping_from_csv(
    "search_engines.csv",
    expectedHeaders=("URL Template", "Name")
)

@mod.action_class
class Actions:
    def open_url(url: str):
        """Visit the given URL."""
        webbrowser.open(url)

    def search_with_search_engine(search_template: str, search_text: str):
        """Search a search engine for given text"""
        url = search_template.replace("%s", quote_plus(search_text))
        webbrowser.open(url)
