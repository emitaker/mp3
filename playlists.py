import vlc
#Slowed reverb
sb_list_player = vlc.MediaListPlayer()
sb_player = vlc.Instance()
    
slowed_reverb = sb_player.media_list_new() #creating playlist
sr_songs = sb_player.media_new("/home/pi/Documents/mp3/music/slowed_reverb/aunque_no_sea_conmigo_slowed_reverb.mp3") #creating the song, but still not added
slowed_reverb.add_media(sr_songs) #adding the song to the playlist
sb_list_player.set_media_list(slowed_reverb) #setting media list to the media player
    
sr_songs = sb_player.media_new("/home/pi/Documents/mp3/music/slowed_reverb/bad_bunny_120_slowed_reverb.mp3") #creating the song, but still not added
slowed_reverb.add_media(sr_songs) #adding the song to the playlist
sb_list_player.set_media_list(slowed_reverb) #setting media list to the media player
    
sr_songs = sb_player.media_new("/home/pi/Documents/mp3/music/slowed_reverb/beach_house_space_song_slowed_reverb.mp3") #creating the song, but still not added
slowed_reverb.add_media(sr_songs) #adding the song to the playlist
sb_list_player.set_media_list(slowed_reverb) #setting media list to the media player

#------------------------------------------------------------------------------------------------------------------------------------------------------------
#Live music
lv_list_player = vlc.MediaListPlayer()
lv_player = vlc.Instance

live_music = lv_player.media_list_new()
lv_songs = lv_player.media_new("/home/pi/Documents/mp3/music/live_music/cafe_tacvba_las_flores.mp3") #creating the song, but still not added
live_music.add_media(lm_songs)
lv_list_player.set_media_list(live_music)
    
    
    
"""
def live_music():
    media_player = vlc.MediaListPlayer()
    player = vlc.Instance()
    media_list = player.media_list_new() #creating playlist
    media = player.media_new("/home/pi/Documents/mp3/music/live_music/cafe_tacvba_las_flores.mp3") #creating the song, but still not added
    media_list.add_media(media) #adding the song to the playlist
    media_player.set_media_list(media_list) #setting media list to the media player
    media = player.media_new("/home/pi/Documents/mp3/music/live_music/jose_jose_el_triste.mp3") #creating the song, but still not added
    media_list.add_media(media) #adding the song to the playlist
    media_player.set_media_list(media_list) #setting media list to the media player
    media = player.media_new("/home/pi/Documents/mp3/music/live_music/mijares_no_se_murio_el_amor.mp3") #creating the song, but still not added
    media_list.add_media(media) #adding the song to the playlist
    media_player.set_media_list(media_list) #setting media list to the media player
"""
