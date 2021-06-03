import vlc
#Slowed reverb
#------------------------------------------------------------------------------------------
sr_inst = vlc.Instance()#Creating VLC instance
slowed_reverb_player = sr_inst.media_list_player_new()#Creating media list player
sr_songs = sr_inst.media_list_new(
            [
                "/home/pi/Documents/mp3/music/slowed_reverb/aunque_no_sea_conmigo_slowed_reverb.mp3", 
                "/home/pi/Documents/mp3/music/slowed_reverb/bad_bunny_120_slowed_reverb.mp3",
                "/home/pi/Documents/mp3/music/slowed_reverb/beach_house_space_song_slowed_reverb.mp3",
                "/home/pi/Documents/mp3/music/slowed_reverb/fuentes_de_ortiz _ed_maverick_slowed_reverb.mp3",
                "/home/pi/Documents/mp3/music/slowed_reverb/liue_suffer_with_me_slowed_reverb.mp3"
            ]
    )#Creting the songs, but still not added
slowed_reverb_player.set_media_list(sr_songs)#Setting media list to the media list player
#------------------------------------------------------------------------------------------------------------------------------------------------------------
#Live music
lv_inst = vlc.Instance()#Creating VLC instance
lv_list_player = lv_inst.media_list_player_new()#Creating media list player
lv_songs = lv_inst.media_list_new(
            [
                "/home/pi/Documents/mp3/music/live_music/cafe_tacvba_las_flores.mp3",
                "/home/pi/Documents/mp3/music/live_music/jose_jose_el_triste.mp3",
                "/home/pi/Documents/mp3/music/live_music/mijares_no_se_murio_el_amor.mp3",
                "/home/pi/Documents/mp3/music/live_music/por_que_me_fui_a_enamorar_de_ti.mp3",
                "/home/pi/Documents/mp3/music/live_music/zoe_luna.mp3"
            ]
    )#Creting the songs, but still not added
lv_list_player.set_media_list(lv_songs)#Setting media list to the media list player
#------------------------------------------------------------------------------------------------------------------------------------------------------------
#Classic Music
cl_inst = vlc.Instance()#Creating VLC instance
cl_list_player = cl_inst.media_list_player_new()#Creating media list player
cl_songs = cl_inst.media_list_new(
            [
                "/home/pi/Documents/mp3/music/classic_music/bach_aria_da_corda_sol.mp3",
                "/home/pi/Documents/mp3/music/classic_music/carl_orff _o_fortuna_carmina_burana.mp3",
                "/home/pi/Documents/mp3/music/classic_music/brian_crain_canon_in_d.mp3",
                "/home/pi/Documents/mp3/music/classic_music/ludwig_van_beethoven_melody_of_love.mp3",
                "/home/pi/Documents/mp3/music/classic_music/to_the_moon_piano_ending_version.mp3"
            ]
    )#Creting the songs, but still not added
cl_list_player.set_media_list(cl_songs) #setting media list to the media player
#------------------------------------------------------------------------------------------------------------------------------------------------------------
#Rock
rock_inst = vlc.Instance()#Creating VLC instance
rock_list_player = rock_inst.media_list_player_new()#Creating media list player
rock_songs = rock_inst.media_list_new(
            [
                "/home/pi/Documents/mp3/music/rock/babasonicos_puesto.mp3",
                "/home/pi/Documents/mp3/music/rock/enrique_bunbury_parecemos_tontos.mp3",
                "/home/pi/Documents/mp3/music/rock/i_wanna_be_yours_arctic_monkeys.mp3",
                "/home/pi/Documents/mp3/music/rock/maroon5_lost_stars.mp3",
                "/home/pi/Documents/mp3/music/rock/oasis_wonderwall.mp3"
            ]
    )#Creting the songs, but still not added
rock_list_player.set_media_list(rock_songs) #setting media list to the media player
