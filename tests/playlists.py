import vlc
#Slowed reverb


sb_list_player = vlc.MediaListPlayer() #playlist player
sb_player = vlc.Instance()
sb_volume = vlc.Instance()#new-------------------------------------------
slowed_reverb = sb_player.media_list_new() #creating playlist
sb_volume_player = sb_volume.media_list_player_new()#new-------------------

sr_songs = sb_player.media_new("/home/pi/Documents/mp3/music/slowed_reverb/aunque_no_sea_conmigo_slowed_reverb.mp3") #creating the song, but still not added
#----------------------------------------------------------------------
sb_volume_list = sb_volume.media_list_new(["/home/pi/Documents/mp3/music/slowed_reverb/aunque_no_sea_conmigo_slowed_reverb.mp3", "/home/pi/Documents/mp3/music/slowed_reverb/bad_bunny_120_slowed_reverb.mp3"])
sb_volume_player.set_media_list(sb_volume_list)
#----------------------------------------------------------------------
slowed_reverb.add_media(sr_songs) #adding the song to the playlist
sb_list_player.set_media_list(slowed_reverb) #setting media list to the media player
    
sr_songs = sb_player.media_new("/home/pi/Documents/mp3/music/slowed_reverb/bad_bunny_120_slowed_reverb.mp3") #creating the song, but still not added
slowed_reverb.add_media(sr_songs) #adding the song to the playlist
sb_list_player.set_media_list(slowed_reverb) #setting media list to the media player
    
sr_songs = sb_player.media_new("/home/pi/Documents/mp3/music/slowed_reverb/beach_house_space_song_slowed_reverb.mp3") #creating the song, but still not added
slowed_reverb.add_media(sr_songs) #adding the song to the playlist
sb_list_player.set_media_list(slowed_reverb) #setting media list to the media player

sr_songs = sb_player.media_new("/home/pi/Documents/mp3/music/slowed_reverb/fuentes_de_ortiz _ed_maverick_slowed_reverb.mp3") #creating the song, but still not added
slowed_reverb.add_media(sr_songs) #adding the song to the playlist
sb_list_player.set_media_list(slowed_reverb) #setting media list to the media player

sr_songs = sb_player.media_new("/home/pi/Documents/mp3/music/slowed_reverb/liue_suffer_with_me_slowed_reverb.mp3") #creating the song, but still not added
slowed_reverb.add_media(sr_songs) #adding the song to the playlist
sb_list_player.set_media_list(slowed_reverb) #setting media list to the media player

#------------------------------------------------------------------------------------------------------------------------------------------------------------
#Live music
lv_list_player = vlc.MediaListPlayer()
lv_player = vlc.Instance()
live_music = lv_player.media_list_new()#creating playlist

lv_songs = lv_player.media_new("/home/pi/Documents/mp3/music/live_music/cafe_tacvba_las_flores.mp3") #creating the song, but still not added
live_music.add_media(lv_songs) #adding the song to the playlist
lv_list_player.set_media_list(live_music) #setting media list to the media player

lv_songs = lv_player.media_new("/home/pi/Documents/mp3/music/live_music/jose_jose_el_triste.mp3") #creating the song, but still not added
live_music.add_media(lv_songs) #adding the song to the playlist
lv_list_player.set_media_list(live_music) #setting media list to the media player

lv_songs = lv_player.media_new("/home/pi/Documents/mp3/music/live_music/mijares_no_se_murio_el_amor.mp3") #creating the song, but still not added
live_music.add_media(lv_songs) #adding the song to the playlist
lv_list_player.set_media_list(live_music) #setting media list to the media player

lv_songs = lv_player.media_new("/home/pi/Documents/mp3/music/live_music/por_que_me_fui_a_enamorar_de_ti.mp3") #creating the song, but still not added
live_music.add_media(lv_songs) #adding the song to the playlist
lv_list_player.set_media_list(live_music) #setting media list to the media player

lv_songs = lv_player.media_new("/home/pi/Documents/mp3/music/live_music/zoe_luna.mp3") #creating the song, but still not added
live_music.add_media(lv_songs) #adding the song to the playlist
lv_list_player.set_media_list(live_music) #setting media list to the media player

#------------------------------------------------------------------------------------------------------------------------------------------------------------
#Classic Music
cl_list_player = vlc.MediaListPlayer()
cl_player = vlc.Instance()
classic_music = cl_player.media_list_new()#creating playlist

cl_songs = cl_player.media_new("/home/pi/Documents/mp3/music/classic_music/bach_aria_da_corda_sol.mp3") #creating the song, but still not added
classic_music.add_media(cl_songs) #adding the song to the playlist
cl_list_player.set_media_list(classic_music) #setting media list to the media player

cl_songs = cl_player.media_new("/home/pi/Documents/mp3/music/classic_music/brian_crain_canon_in_d.mp3") #creating the song, but still not added
classic_music.add_media(cl_songs) #adding the song to the playlist
cl_list_player.set_media_list(classic_music) #setting media list to the media player

cl_songs = cl_player.media_new("/home/pi/Documents/mp3/music/classic_music/carl_orff _o_fortuna_carmina_burana.mp3") #creating the song, but still not added
classic_music.add_media(cl_songs) #adding the song to the playlist
cl_list_player.set_media_list(classic_music) #setting media list to the media player

cl_songs = cl_player.media_new("/home/pi/Documents/mp3/music/classic_music/ludwig_van_beethoven_melody_of_love.mp3") #creating the song, but still not added
classic_music.add_media(cl_songs) #adding the song to the playlist
cl_list_player.set_media_list(classic_music) #setting media list to the media player

cl_songs = cl_player.media_new("/home/pi/Documents/mp3/music/classic_music/to_the_moon_piano_ending_version.mp3") #creating the song, but still not added
classic_music.add_media(cl_songs) #adding the song to the playlist
cl_list_player.set_media_list(classic_music) #setting media list to the media player

#------------------------------------------------------------------------------------------------------------------------------------------------------------
#Rock

rock_list_player = vlc.MediaListPlayer()
rock_player = vlc.Instance()
rock = rock_player.media_list_new()#creating playlist

rock_songs = rock_player.media_new("/home/pi/Documents/mp3/music/rock/babasonicos_puesto.mp3") #creating the song, but still not added
rock.add_media(rock_songs) #adding the song to the playlist
rock_list_player.set_media_list(rock) #setting media list to the media player

rock_songs = rock_player.media_new("/home/pi/Documents/mp3/music/rock/enrique_bunbury_parecemos_tontos.mp3") #creating the song, but still not added
rock.add_media(rock_songs) #adding the song to the playlist
rock_list_player.set_media_list(rock) #setting media list to the media player

rock_songs = rock_player.media_new("/home/pi/Documents/mp3/music/rock/i_wanna_be_yours_arctic_monkeys.mp3") #creating the song, but still not added
rock.add_media(rock_songs) #adding the song to the playlist
rock_list_player.set_media_list(rock) #setting media list to the media player

rock_songs = rock_player.media_new("/home/pi/Documents/mp3/music/rock/maroon5_lost_stars.mp3") #creating the song, but still not added
rock.add_media(rock_songs) #adding the song to the playlist
rock_list_player.set_media_list(rock) #setting media list to the media player

rock_songs = rock_player.media_new("/home/pi/Documents/mp3/music/rock/oasis_wonderwall.mp3") #creating the song, but still not added
rock.add_media(rock_songs) #adding the song to the playlist
rock_list_player.set_media_list(rock) #setting media list to the media player
