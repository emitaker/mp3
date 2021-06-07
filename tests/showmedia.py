import playlists
import vlc
import time

playlists.slowed_reverb_player.play_item_at_index(4)

time.sleep(5)
value = playlists.slowed_reverb_player.is_playing()
print(value)
