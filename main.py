import vlc
import time
import RPi.GPIO as GPIO
import random
import MediaInfo #to do
import playlists


pb_play = 6 #pin 31
pb_pause = 5 #pin 29
pb_skip = 22 #pin 15
pb_prev = 27 #pin 13
pb_shuffle = 17 #pin 11

playlist = 1

def play():
    '''Play the music when the button is pushed'''
    #media = vlc.MediaPlayer("/home/pi/Documents/mp3/music/slowed_reverb/aunque_no_sea_conmigo_slowed_reverb.mp3")
    if (playlist == 1):
        playlists.sb_list_player.play()
    elif(playlist == 2):
        playlists.lv_list_player.play()
    elif (playlist == 3):
        playlists.cl_list_player.play()
    elif(playlist == 4):
        playlists.rock_list_player.play()


def pause():
    '''Pause the music when the button is pushed'''
    #media = vlc.MediaPlayer("/home/pi/Documents/mp3/music/slowed_reverb/aunque_no_sea_conmigo_slowed_reverb.mp3")
    if (playlist == 1):
        playlists.sb_list_player.pause()
    elif(playlist == 2):
        playlists.lv_list_player.pause()
    elif (playlist == 3):
        playlists.cl_list_player.pause()
    elif(playlist == 4):
        playlists.rock_list_player.pause()

def skip():
    '''Pass to the next '''
    if (playlist == 1):
        playlists.sb_list_player.next()
    elif(playlist == 2):
        playlists.lv_list_player.next()
    elif (playlist == 3):
        playlists.cl_list_player.next()
    elif(playlist == 4):
        playlists.rock_list_player.next()

def prev():
    '''Pass to the prev song'''
    if (playlist == 1):
        playlists.sb_list_player.previous()
    elif(playlist == 2):
        playlists.lv_list_player.previous()
    elif (playlist == 3):
        playlists.cl_list_player.previous()
    elif(playlist == 4):
        playlists.rock_list_player.previous()

def shuffle():
    '''Plays a random song in the playlist'''
    index = random.randint(0,4)
    print(index)
    if (playlist == 1):
        playlists.sb_list_player.play_item_at_index(index)
    elif(playlist == 2):
        playlists.lv_list_player.play_item_at_index(index)
    elif (playlist == 3):
        playlists.cl_list_player.play_item_at_index(index)
    elif(playlist == 4):
        playlists.rock_list_player.play_item_at_index(index)


def main():
    try:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pb_play, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(pb_pause, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(pb_skip, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(pb_prev, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(pb_shuffle, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        
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




