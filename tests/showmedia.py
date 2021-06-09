import playlists
import vlc
import time


x = playlists.slowed_reverb_player
x.play_item_at_index(4)
value = x.is_playing()
if value:
    y = x.get_media_player()
    print(y)
time.sleep(5)

