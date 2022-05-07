app: Spotify
-
play | pause: user.spotify_play_pause()
next: user.spotify_next()
previous: user.spotify_previous()

(volume|turn) [it] up:user.spotify_volume_up()
(volume|turn) [it] down:user.spotify_volume_down()