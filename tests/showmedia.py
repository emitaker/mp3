import playlists
import vlc
import time

playlists.slowed_reverb_player.play_item_at_index(4)
x = playlists.slowed_reverb_player
value = playlists.slowed_reverb_player.is_playing()
if value:
    print(x[1])
time.sleep(5)

