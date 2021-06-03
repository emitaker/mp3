import vlc
import time
import RPi.GPIO as GPIO
import random
import MediaInfo #to do
import playlists

pb_play = 17 #pin 11
pb_pause = 27 #pin 13
pb_skip = 22 #pin 15
pb_prev = 5 #pin 29
pb_shuffle = 6 #pin 31
Enc_A = 18  
Enc_B = 16 

playlist = 1 #aqui ver lo del menu

sound_play = 60
sound_pause = 60
sound_next = 60
sound_prev = 60
sound_shuffle = 60

def init():
    GPIO.setwarnings(True)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pb_play, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(pb_pause, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(pb_skip, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(pb_prev, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(pb_shuffle, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(Enc_A, GPIO.IN)
    GPIO.setup(Enc_B, GPIO.IN)
    GPIO.add_event_detect(Enc_A, GPIO.RISING, callback=rotation_decode, bouncetime=10)
    return


def play():
    '''Play the music when the button is pushed'''
    global sound_play
    if (playlist == 1):
        playlists.slowed_reverb_player.get_media_player().audio_set_volume(sound_play)
        playlists.slowed_reverb_player.play()
    elif(playlist == 2):
        playlists.lv_list_player.get_media_player().audio_set_volume(sound_play)
        playlists.lv_list_player.play()
    elif (playlist == 3):
        playlists.cl_list_player.get_media_player().audio_set_volume(sound_play)
        playlists.cl_list_player.play()
    elif(playlist == 4):
        playlists.rock_list_player.get_media_player().audio_set_volume(sound_play)
        playlists.rock_list_player.play()


def pause():
    '''Pause the music when the button is pushed'''
    global sound_pause
    if (playlist == 1):
        playlists.slowed_reverb_player.get_media_player().audio_set_volume(sound_pause)
        playlists.slowed_reverb_player.pause()
    elif(playlist == 2):
        playlists.lv_list_player.get_media_player().audio_set_volume(sound_pause)
        playlists.lv_list_player.pause()
    elif (playlist == 3):
        playlists.cl_list_player.get_media_player().audio_set_volume(sound_pause)
        playlists.cl_list_player.pause()
    elif(playlist == 4):
        playlists.rock_list_player.get_media_player().audio_set_volume(sound_pause)
        playlists.rock_list_player.pause()


def skip():
    '''Pass to the next '''
    global sound_next
    if (playlist == 1):
        playlists.slowed_reverb_player.get_media_player().audio_set_volume(sound_next)
        playlists.slowed_reverb_player.next()
    elif(playlist == 2):
        playlists.lv_list_player.get_media_player().audio_set_volume(sound_next)
        playlists.lv_list_player.next()
    elif (playlist == 3):
        playlists.cl_list_player.get_media_player().audio_set_volume(sound_next)
        playlists.cl_list_player.next()
    elif(playlist == 4):
        playlists.rock_list_player.get_media_player().audio_set_volume(sound_next)
        playlists.rock_list_player.next()


def prev():
    '''Pass to the prev song'''
    global sound_prev
    if (playlist == 1):
        playlists.slowed_reverb_player.get_media_player().audio_set_volume(sound_prev)
        playlists.slowed_reverb_player.previous()
    elif(playlist == 2):
        playlists.lv_list_player.get_media_player().audio_set_volume(sound_prev)
        playlists.lv_list_player.previous()
    elif (playlist == 3):
        playlists.cl_list_player.get_media_player().audio_set_volume(sound_prev)
        playlists.cl_list_player.previous()
    elif(playlist == 4):
        playlists.rock_list_player.get_media_player().audio_set_volume(sound_prev)
        playlists.rock_list_player.previous()


def shuffle():
    '''Plays a random song in the playlist'''
    global sound_shuffle
    index = random.randint(0,4)
    print(index)

    if (playlist == 1):
        playlists.slowed_reverb_player.get_media_player().audio_set_volume(sound_shuffle)
        playlists.slowed_reverb_player.play_item_at_index(index)
    elif(playlist == 2):
        playlists.lv_list_player.get_media_player().audio_set_volume(sound_shuffle)
        playlists.lv_list_player.play_item_at_index(index)
    elif (playlist == 3):
        playlists.cl_list_player.get_media_player().audio_set_volume(sound_shuffle)
        playlists.cl_list_player.play_item_at_index(index)
    elif(playlist == 4):
        playlists.rock_list_player.get_media_player().audio_set_volume(sound_shuffle)
        playlists.rock_list_player.play_item_at_index(index)


def rotation_decode(Enc_A):
    global sound_play
    global sound_pause
    global sound_next
    global sound_prev
    global sound_shuffle
    time.sleep(0.002)
    Switch_A = GPIO.input(Enc_A)
    Switch_B = GPIO.input(Enc_B)
 
    if (Switch_A == 1) and (Switch_B == 0):
        sound_play += 1
        sound_pause += 1
        sound_next += 1
        sound_prev += 1
        sound_shuffle += 1
        print("direction -> ", sound_play)
        while Switch_B == 0:
            Switch_B = GPIO.input(Enc_B)
        while Switch_B == 1:
            Switch_B = GPIO.input(Enc_B)
        return
 
    elif (Switch_A == 1) and (Switch_B == 1):
        sound_play -= 1
        sound_pause -= 1
        sound_next -= 1
        sound_prev -= 1
        sound_shuffle -= 1        
        print("direction <- ", sound_play)
        while Switch_A == 1:
            Switch_A = GPIO.input(Enc_A)
        return
    else:
        return

def main():
    try:
        init()
        while True :
            state_pb_play = GPIO.input(pb_play)
            state_pb_pause = GPIO.input(pb_pause)
            state_pb_skip = GPIO.input(pb_skip)
            state_pb_prev = GPIO.input(pb_prev)
            state_pb_shuffle = GPIO.input(pb_shuffle)

            if state_pb_play == True:
                play()
            if state_pb_pause == True:
                pause()
            if state_pb_skip == True:
                skip()
            if state_pb_prev == True:
                prev()
            if state_pb_shuffle == True:
                shuffle()
            time.sleep(1)
 
    except KeyboardInterrupt:
        GPIO.cleanup()
 
if __name__ == '__main__':
    main()