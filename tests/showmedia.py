import playlists
import vlc
import time

playlists.slowed_reverb_player.play_item_at_index(4)
value = playlists.slowed_reverb_player.is_playing()
if value:
    state = playlists.slowed_reverb_player.get_state() 
    print(state)
time.sleep(5)

