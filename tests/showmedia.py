import playlists
import vlc
import time

playlists.slowed_reverb_player.play()
time.sleep(20)
value = playlists.slowed_reverb_player.is_playing()
print(value)