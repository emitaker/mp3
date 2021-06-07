import vlc
import time
import RPi.GPIO as GPIO
import random
#import MediaInfo #to do
import playlists
import pygame
import pygame_menu
import serial

pygame.init()

ser = serial.Serial('/dev/ttyACM0',9600)#serial port
ser.flushInput()

pb_play = 17 #pin 11
pb_pause = 27 #pin 13
pb_skip = 22 #pin 15
pb_prev = 5 #pin 29
pb_shuffle = 6 #pin 31
Enc_A = 18
Enc_B = 16

playlist = 1

sound = 60

screen = pygame.display.set_mode((800, 650))

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


def slowed_reverb():
    global playlist
    playlist = 1
    print(playlist)


def slowed_reverb_screen():
    screen.fill(('#111010'))
    font = pygame.font.SysFont(None, 48)
    img = font.render('Slowed & reverb', True, ('#f6f6f6')) # #f6f6f6 = white
    screen.blit(img, (110,65))
    #Musicicon2
    image = pygame.image.load('/home/pi/Documents/mp3/pics/slow.bmp')

    image = pygame.transform.scale(image, (50,50))
    screen.blit(image, (50,55))
    image = pygame.image.load('/home/pi/Documents/mp3/pics/pausab.bmp')

    image = pygame.transform.scale(image, (65,65))
    screen.blit(image, (375,450))
    image = pygame.image.load('/home/pi/Documents/mp3/pics/playb.bmp')

    image = pygame.transform.scale(image, (65,65))
    screen.blit(image, (310,451))
    image = pygame.image.load('/home/pi/Documents/mp3/pics/prevsi.bmp')

    image = pygame.transform.scale(image, (62,62))
    screen.blit(image, (242,452))
    image = pygame.image.load('/home/pi/Documents/mp3/pics/ffsi.bmp')

    image = pygame.transform.scale(image, (58,58))
    screen.blit(image, (445,452))
    image = pygame.image.load('/home/pi/Documents/mp3/pics/shufflew.bmp')

    image = pygame.transform.scale(image, (50,50))
    screen.blit(image, (512,456))
    image = pygame.image.load('/home/pi/Documents/mp3/pics/vol.bmp')

    image = pygame.transform.scale(image, (50,50))
    screen.blit(image, (188,456))


def live():
    global playlist
    playlist = 2
    print(playlist)


def live_screen():
    screen.fill(('#111010'))
    font = pygame.font.SysFont(None, 48)
    img = font.render('Live', True, ('#f6f6f6')) # #f6f6f6 = white
    screen.blit(img, (110,65))
    #Musicicon2
    image = pygame.image.load('/home/pi/Documents/mp3/pics/live.bmp')

    image = pygame.transform.scale(image, (50,50))
    screen.blit(image, (50,55))
    image = pygame.image.load('/home/pi/Documents/mp3/pics/pausab.bmp')

    image = pygame.transform.scale(image, (65,65))
    screen.blit(image, (375,450))
    image = pygame.image.load('/home/pi/Documents/mp3/pics/playb.bmp')

    image = pygame.transform.scale(image, (65,65))
    screen.blit(image, (310,451))
    image = pygame.image.load('/home/pi/Documents/mp3/pics/prevsi.bmp')

    image = pygame.transform.scale(image, (62,62))
    screen.blit(image, (242,452))
    image = pygame.image.load('/home/pi/Documents/mp3/pics/ffsi.bmp')

    image = pygame.transform.scale(image, (58,58))
    screen.blit(image, (445,452))
    image = pygame.image.load('/home/pi/Documents/mp3/pics/shufflew.bmp')

    image = pygame.transform.scale(image, (50,50))
    screen.blit(image, (512,456))
    image = pygame.image.load('/home/pi/Documents/mp3/pics/vol.bmp')

    image = pygame.transform.scale(image, (50,50))
    screen.blit(image, (188,456))


def classic():
    global playlist
    playlist = 3
    print(playlist)


def classic_screen():
    screen.fill(('#111010'))
    font = pygame.font.SysFont(None, 48)
    img = font.render('Classic', True, ('#f6f6f6')) # #f6f6f6 = white
    screen.blit(img, (110,65))
    #Musicicon2
    image = pygame.image.load('/home/pi/Documents/mp3/pics/classicmusic.bmp')

    image = pygame.transform.scale(image, (50,50))
    screen.blit(image, (50,55))
    image = pygame.image.load('/home/pi/Documents/mp3/pics/pausab.bmp')

    image = pygame.transform.scale(image, (65,65))
    screen.blit(image, (375,450))
    image = pygame.image.load('/home/pi/Documents/mp3/pics/playb.bmp')

    image = pygame.transform.scale(image, (65,65))
    screen.blit(image, (310,451))
    image = pygame.image.load('/home/pi/Documents/mp3/pics/prevsi.bmp')

    image = pygame.transform.scale(image, (62,62))
    screen.blit(image, (242,452))
    image = pygame.image.load('/home/pi/Documents/mp3/pics/ffsi.bmp')

    image = pygame.transform.scale(image, (58,58))
    screen.blit(image, (445,452))
    image = pygame.image.load('/home/pi/Documents/mp3/pics/shufflew.bmp')

    image = pygame.transform.scale(image, (50,50))
    screen.blit(image, (512,456))
    image = pygame.image.load('/home/pi/Documents/mp3/pics/vol.bmp')

    image = pygame.transform.scale(image, (50,50))
    screen.blit(image, (188,456))


def rock():
    global playlist
    playlist = 4
    print(playlist)


def rock_screen():
    screen.fill(('#111010'))
    font = pygame.font.SysFont(None, 48)
    img = font.render('Rock', True, ('#f6f6f6')) # #f6f6f6 = white
    screen.blit(img, (110,65))
    #Musicicon2
    image = pygame.image.load('/home/pi/Documents/mp3/pics/ock.bmp')

    image = pygame.transform.scale(image, (50,50))
    screen.blit(image, (50,55))
    image = pygame.image.load('/home/pi/Documents/mp3/pics/pausab.bmp')

    image = pygame.transform.scale(image, (65,65))
    screen.blit(image, (375,450))
    image = pygame.image.load('/home/pi/Documents/mp3/pics/playb.bmp')

    image = pygame.transform.scale(image, (65,65))
    screen.blit(image, (310,451))
    image = pygame.image.load('/home/pi/Documents/mp3/pics/prevsi.bmp')

    image = pygame.transform.scale(image, (62,62))
    screen.blit(image, (242,452))
    image = pygame.image.load('/home/pi/Documents/mp3/pics/ffsi.bmp')

    image = pygame.transform.scale(image, (58,58))
    screen.blit(image, (445,452))
    image = pygame.image.load('/home/pi/Documents/mp3/pics/shufflew.bmp')

    image = pygame.transform.scale(image, (50,50))
    screen.blit(image, (512,456))
    image = pygame.image.load('/home/pi/Documents/mp3/pics/vol.bmp')

    image = pygame.transform.scale(image, (50,50))
    screen.blit(image, (188,456))

def play():
    '''Play the music when the button is pushed'''
    if (playlist == 1):
        playlists.slowed_reverb_player.play()
    elif(playlist == 2):
        playlists.lv_list_player.play()
    elif (playlist == 3):
        playlists.cl_list_player.play()
    elif(playlist == 4):
        playlists.rock_list_player.play()


def pause():
    '''Pause the music when the button is pushed'''
    if (playlist == 1):
        playlists.slowed_reverb_player.pause()
    elif(playlist == 2):
        playlists.lv_list_player.pause()
    elif (playlist == 3):
        playlists.cl_list_player.pause()
    elif(playlist == 4):
        playlists.rock_list_player.pause()


def skip():
    '''Pass to the next '''
    if (playlist == 1):
        playlists.slowed_reverb_player.next()
    elif(playlist == 2):
        playlists.lv_list_player.next()
    elif (playlist == 3):
        playlists.cl_list_player.next()
    elif(playlist == 4):
        playlists.rock_list_player.next()


def prev():
    '''Pass to the prev song'''
    if (playlist == 1):
        playlists.slowed_reverb_player.previous()
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
        playlists.slowed_reverb_player.play_item_at_index(index)
    elif(playlist == 2):
        playlists.lv_list_player.play_item_at_index(index)
    elif (playlist == 3):
        playlists.cl_list_player.play_item_at_index(index)
    elif(playlist == 4):
        playlists.rock_list_player.play_item_at_index(index)


def rotation_decode(Enc_A):
    global sound
    time.sleep(0.002)
    Switch_A = GPIO.input(Enc_A)
    Switch_B = GPIO.input(Enc_B)

    if (Switch_A == 1) and (Switch_B == 0):
        sound += 1
        if (playlist == 1):
            playlists.slowed_reverb_player.get_media_player().audio_set_volume(sound)
        elif(playlist == 2):
            playlists.lv_list_player.get_media_player().audio_set_volume(sound)
        elif (playlist == 3):
            playlists.cl_list_player.get_media_player().audio_set_volume(sound)
        elif(playlist == 4):
            playlists.rock_list_player.get_media_player().audio_set_volume(sound)
        print("volume: ", sound, " +")
        while Switch_B == 0:
            Switch_B = GPIO.input(Enc_B)
        while Switch_B == 1:
            Switch_B = GPIO.input(Enc_B)
        return

    elif (Switch_A == 1) and (Switch_B == 1):
        sound -= 1
        if (playlist == 1):
            playlists.slowed_reverb_player.get_media_player().audio_set_volume(sound)
        elif(playlist == 2):
            playlists.lv_list_player.get_media_player().audio_set_volume(sound)
        elif (playlist == 3):
            playlists.cl_list_player.get_media_player().audio_set_volume(sound)
        elif(playlist == 4):
            playlists.rock_list_player.get_media_player().audio_set_volume(sound)
        print("volume: ", sound, " -")
        while Switch_A == 1:
            Switch_A = GPIO.input(Enc_A)
        return
    else:
        return

def main():

    init()
    #-------------------------------------------------------------------------
    #
    #Weather Menu
    #
    #-------------------------------------------------------------------------

    weather_theme = pygame_menu.themes.THEME_DARK.copy()
    weather_theme.title_background_color=('#fc3a4b') # This line puts the title background in some kind of red color
    weather_theme.title_bar_style =  pygame_menu.widgets.MENUBAR_STYLE_SIMPLE
    weather_theme.title_offset = (20,0)
    weather_theme.background_color=('#111010') # Black


    weather_menu = pygame_menu.Menu(
        height=650, #height
        theme=weather_theme,
        title='Weather',
        width=800,
    )

    weather_menu.add.button('Back',pygame_menu.events.BACK)

    #-------------------------------------------------------------------------
    #
    #Playlists Menu
    #
    #-------------------------------------------------------------------------

    playlists_theme = pygame_menu.themes.THEME_DARK.copy()
    playlists_theme.title_background_color=('#fc3a4b') # This line puts the title background in some kind of red color
    playlists_theme.title_bar_style =  pygame_menu.widgets.MENUBAR_STYLE_SIMPLE
    playlists_theme.title_offset = (20,0)
    playlists_theme.background_color=('#111010') # Black
    playlists_theme.widget_font_size = 45

    playlists_menu = pygame_menu.Menu(
        height=650, #height
        theme=playlists_theme,
        title='Playlists',
        width=800,
    )

    #playlists_menu.add_image('D:\Programacion\Programs\mp3\pics\slow.bmp', scale=(0.25,0.25),margin=(-370,15))
    #playlists_menu.add_image('D:\Programacion\Programs\mp3\pics\live.bmp', scale=(0.25,0.25),margin=(-370,15))
    #playlists_menu.add_image('D:\Programacion\Programs\mp3\pics\classicmusic.bmp', scale=(0.09,0.09),margin=(-370,15))
    #playlists_menu.add_image('D:\Programacion\Programs\mp3\pics\ock.bmp', scale=(0.25,0.25),margin=(-370,-305))

    playlists_menu.add.image('/home/pi/Documents/mp3/pics/slow.bmp', scale=(0.25,0.25),margin=(-370,15))
    playlists_menu.add.image('/home/pi/Documents/mp3/pics/live.bmp', scale=(0.25,0.25),margin=(-370,15))
    playlists_menu.add.image('/home/pi/Documents/mp3/pics/classicmusic.bmp', scale=(0.09,0.09),margin=(-370,15))
    playlists_menu.add.image('/home/pi/Documents/mp3/pics/ock.bmp', scale=(0.25,0.25),margin=(-370,-305))


    playlists_menu.add.button('Slowed & Reverb',slowed_reverb , margin=(-140,12))
    playlists_menu.add.button('Live',live , margin=(-280,10))
    playlists_menu.add.button('Classic',classic , margin=(-252,10))
    playlists_menu.add.button('Rock',rock ,margin=(-269,10))
    playlists_menu.add.button('Back',pygame_menu.events.BACK, margin=(-269,0))
    #playlists_menu.add.VMargin(230)


    #-------------------------------------------------------------------------
    #
    #Main Menu
    #
    #-------------------------------------------------------------------------

    main_menu_theme = pygame_menu.themes.THEME_DARK.copy()
    main_menu_theme.title_bar_style =  pygame_menu.widgets.MENUBAR_STYLE_NONE
    main_menu_theme.background_color=('#111010') # Black
    main_menu_theme.widget_font_size = 55

    menu = pygame_menu.Menu(
        height=650, #height
        theme=main_menu_theme,
        title='',
        width=800,
    )

    #menu.add_image('D:\Programacion\Programs\mp3\pics\musicicon2.bmp', scale=(.2,.2),margin=(-170,-211))
    #menu.add_image('D:\Programacion\Programs\mp3\pics\weather.bmp', scale=(.2,.2),margin=(170,20))

    menu.add.image('/home/pi/Documents/mp3/pics/musicicon2.bmp', scale=(.2,.2),margin=(-170,-211))
    menu.add.image('/home/pi/Documents/mp3/pics/weather.bmp', scale=(.2,.2),margin=(170,20))

    #menu.add.button('Music', playlists_menu, margin=(-167,-85))
    menu.add.button('Music', playlists_menu, margin=(-167,-85))
    menu.add.button('Weather', weather_menu,margin=(174,0))
    #menu.add.VMargin(120)


    while True :

        state_pb_play = GPIO.input(pb_play)
        state_pb_pause = GPIO.input(pb_pause)
        state_pb_skip = GPIO.input(pb_skip)
        state_pb_prev = GPIO.input(pb_prev)
        state_pb_shuffle = GPIO.input(pb_shuffle)
        ser_bytes = ser.readline() #Undestanding arduino
        decoded_bytes = ser_bytes[0:len(ser_bytes)-2].decode("utf-8") #translation
        print(decoded_bytes)


        current_menu = menu.get_current()

        if current_menu.get_title() != '' or not menu.is_enabled():
            if playlist == 1:
                slowed_reverb_screen()
                playlists.lv_list_player.stop()
                playlists.cl_list_player.stop()
                playlists.rock_list_player.stop()
                ser_bytes = ser.readline() #Undestanding arduino
                decoded_bytes = ser_bytes[0:len(ser_bytes)-2].decode("utf-8") #translation
                
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


            elif playlist == 2:
                live_screen()
                playlists.slowed_reverb_player.stop()
                playlists.cl_list_player.stop()
                playlists.rock_list_player.stop()
                ser_bytes = ser.readline() #Undestanding arduino
                decoded_bytes = ser_bytes[0:len(ser_bytes)-2].decode("utf-8") #translation
                
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

            elif playlist == 3:
                classic_screen()
                playlists.slowed_reverb_player.stop()
                playlists.lv_list_player.stop()
                playlists.rock_list_player.stop()
                ser_bytes = ser.readline() #Undestanding arduino
                decoded_bytes = ser_bytes[0:len(ser_bytes)-2].decode("utf-8") #translation
            
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

            elif playlist == 4:
                rock_screen()
                playlists.slowed_reverb_player.stop()
                playlists.lv_list_player.stop()
                playlists.cl_list_player.stop()
                ser_bytes = ser.readline() #Undestanding arduino
                decoded_bytes = ser_bytes[0:len(ser_bytes)-2].decode("utf-8") #translation
                
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

        else:
            screen.fill('#111010')

        if decoded_bytes == "pushed":
            #pushed_event=pygame.event.Event(pygame.USEREVENT, attr1='pushed_event')
            #pygame.event.post(pushed_event)
            pushed_event = pygame.event.Event(pygame.K_KEYDOWN(pygame.K_ESCAPE))
            pygame.event.post(pushed_event)
            print(pushed_event)
            print(pushed_event.type)

        events = pygame.event.get()
        for event in events:
            print(event)
            if event.type == pygame.QUIT:
                exit()
            elif event.type == 27 and current_menu.get_title() == '':
                menu.toggle()
            elif event.type == 27 and current_menu.get_title() == 'Playlists':
                playlists_menu.toggle()
            elif event.type == 27 and current_menu.get_title() == 'Weather':
                weather_menu.toggle()

        if menu.is_enabled():
            menu.draw(screen)
            menu.update(events)

        pygame.display.flip()

main()
