import playlists
import vlc
import time

playlists.slowed_reverb_player.play()
value = playlists.slowed_reverb_player.is_playing()
print(value)
time.sleep(20)
