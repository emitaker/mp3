import RPi.GPIO as GPIO
from time import sleep
import playlists
import random

 
counter = 10

sound = 10

Enc_A = 18  
Enc_B = 16  

pb_play = 17 #pin 11
pb_pause = 27 #pin 13
pb_skip = 22 #pin 15
pb_prev = 5 #pin 29
pb_shuffle = 6 #pin 31 
 
def init():
    print("Rotary Encoder Test Program")
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
    global sound
    playlists.sb_volume_player.get_media_player().audio_set_volume(sound)
    playlists.sb_volume_player.play()


def pause():
    '''Pause the music when the button is pushed'''
    playlists.sb_volume_player.pause()

def skip():
    '''Pass to the next '''
    playlists.sb_volume_player.next()
    

def prev():
    '''Pass to the prev song'''
    playlists.sb_volume_player.previous()


def shuffle():
    '''Plays a random song in the playlist'''
    index = random.randint(0,4)
    print(index)
    playlists.sb_volume_player.play_item_at_index(index)


def rotation_decode(Enc_A):
    global counter
    global sound
    sleep(0.002)
    Switch_A = GPIO.input(Enc_A)
    Switch_B = GPIO.input(Enc_B)
 
    if (Switch_A == 1) and (Switch_B == 0):
        counter += 1
        sound += 1
        print("direction -> ", counter)
        print(sound)
        while Switch_B == 0:
            Switch_B = GPIO.input(Enc_B)
        while Switch_B == 1:
            Switch_B = GPIO.input(Enc_B)
        return
 
    elif (Switch_A == 1) and (Switch_B == 1):
        counter -= 1
        sound -= 1
        print("direction <- ", counter)
        print(sound)
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
            sleep(1)
 
    except KeyboardInterrupt:
        GPIO.cleanup()
 
if __name__ == '__main__':
    main()
