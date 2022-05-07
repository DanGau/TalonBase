from talon import Module

mod = Module()

# Get the app names using ui.apps() in the REPL Window
mod.apps.helloWorld = """
os: windows
and app.exe: Spotify.EXE
"""

mod.apps.spotify = """
os: windows
and app.name: Spotify
"""

@mod.action_class
class Actions:
    def spotify_play_pause():
        """Play pause"""
    def spotify_next():
        """Next track"""
    def spotify_previous():
        """Previous track"""
    def spotify_volume_up():
        """volume up"""
    def spotify_volume_down():
        """Volume down"""
