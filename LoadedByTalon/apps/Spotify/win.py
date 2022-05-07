from talon import Context, actions

ctx = Context()

ctx.matches = r"""
os: windows
app: Spotify
"""

# User context actions are ones defined specifically for this app
# Other strings given to action_class are overrides
@ctx.action_class('user')
class UserActions:
    def spotify_play_pause(): actions.key('space')
    def spotify_next(): actions.key('ctrl-right')
    def spotify_previous(): actions.key('ctrl-left')
    def spotify_volume_up(): actions.key('ctrl-up')
    def spotify_volume_down(): actions.key('ctrl-down')
