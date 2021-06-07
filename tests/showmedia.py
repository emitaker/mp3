import playlists
import vlc
import time


x = playlists.slowed_reverb_player
x.play_item_at_index(4)
value = x.is_playing()
if value:
    if x == x[3]:
        print("cancion 4")
    if == x[4]:
        print("cancion 5")
time.sleep(5)

