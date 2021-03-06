import pygame
import pygame_menu
import serial

pygame.init()

playlist = 0

ser = serial.Serial('/dev/ttyACM0',9600)#-----------------------------------------------------------------------------
ser.flushInput()#--------------------------------------------------------------------------------

screen = pygame.display.set_mode((800, 650))

def slowed_reverb():
    global playlist
    playlist = 1
    print("cambio de valor ", playlist)

def slowed_reverb_screen():
    screen.fill(('#111010')) # #111010 = black
    #Text: Music
    #Text: Music
    font = pygame.font.SysFont(None, 48)
    img = font.render('Slowed & reverb', True, ('#f6f6f6')) # #f6f6f6 = white
    screen.blit(img, (110,65))
    #Musicicon2
    image = pygame.image.load('/home/emitaker/Documents/GitHub/mp3/pics/slowed&reverb.jpg')
    image.convert()
    image = pygame.transform.scale(image, (50,50))
    screen.blit(image, (50,55))
    image = pygame.image.load('/home/emitaker/Documents/GitHub/mp3/pics/pausab.png')
    image.convert()
    image = pygame.transform.scale(image, (65,65))
    screen.blit(image, (375,450))
    image = pygame.image.load('/home/emitaker/Documents/GitHub/mp3/pics/playb.png')
    image.convert()
    image = pygame.transform.scale(image, (65,65))
    screen.blit(image, (310,451))
    image = pygame.image.load('/home/emitaker/Documents/GitHub/mp3/pics/prevsi.png')
    image.convert()
    image = pygame.transform.scale(image, (62,62))
    screen.blit(image, (242,452))
    image = pygame.image.load('/home/emitaker/Documents/GitHub/mp3/pics/ffsi.png')
    image.convert()
    image = pygame.transform.scale(image, (58,58))
    screen.blit(image, (445,452))
    image = pygame.image.load('/home/emitaker/Documents/GitHub/mp3/pics/shufflew.png')
    image.convert()
    image = pygame.transform.scale(image, (50,50))
    screen.blit(image, (512,456))
    image = pygame.image.load('/home/emitaker/Documents/GitHub/mp3/pics/vol.png')
    image.convert()
    image = pygame.transform.scale(image, (50,50))
    screen.blit(image, (188,456))


def main():
    #Event1=pygame.event.customtype()
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

    #playlists_menu.add_image('D:\Programacion\Programs\mp3\pics\slow.jpg', scale=(0.25,0.25),margin=(-370,15))
    #playlists_menu.add_image('D:\Programacion\Programs\mp3\pics\live.jpg', scale=(0.25,0.25),margin=(-370,15))
    #playlists_menu.add_image('D:\Programacion\Programs\mp3\pics\classicmusic.jpg', scale=(0.09,0.09),margin=(-370,15))
    #playlists_menu.add_image('D:\Programacion\Programs\mp3\pics\ock.jpg', scale=(0.25,0.25),margin=(-370,-305))

    playlists_menu.add_image('/home/emitaker/Documents/GitHub/mp3/pics/slow.jpg', scale=(0.25,0.25),margin=(-370,15))
    playlists_menu.add_image('/home/emitaker/Documents/GitHub/mp3/pics/live.jpg', scale=(0.25,0.25),margin=(-370,15))
    playlists_menu.add_image('/home/emitaker/Documents/GitHub/mp3/pics/classicmusic.jpg', scale=(0.09,0.09),margin=(-370,15))
    playlists_menu.add_image('/home/emitaker/Documents/GitHub/mp3/pics/ock.jpg', scale=(0.25,0.25),margin=(-370,-305))


    playlists_menu.add.button('Slowed & Reverb',slowed_reverb, margin=(-140,12))
    playlists_menu.add.button('Live' , margin=(-280,10))
    playlists_menu.add.button('Classic', margin=(-252,10))
    playlists_menu.add.button('Rock', margin=(-269,10))
    playlists_menu.add.button('Back',pygame_menu.events.BACK, margin=(-269,0))
    playlists_menu.add_vertical_margin(230)


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

    #menu.add_image('D:\Programacion\Programs\mp3\pics\musicicon2.png', scale=(.2,.2),margin=(-170,-211))
    #menu.add_image('D:\Programacion\Programs\mp3\pics\weather.png', scale=(.2,.2),margin=(170,20))

    menu.add_image('/home/emitaker/Documents/GitHub/mp3/pics/musicicon2.png', scale=(.2,.2),margin=(-170,-211))
    menu.add_image('/home/emitaker/Documents/GitHub/mp3/pics/weather.png', scale=(.2,.2),margin=(170,20))

    menu.add.button('Music', playlists_menu, margin=(-167,-85))
    menu.add.button('Weather',margin=(174,0))
    menu.add_vertical_margin(120)

    while True:

        ser_bytes = ser.readline()#--------------------------------------------------------------------------------------------------
        decoded_bytes = ser_bytes[0:len(ser_bytes)-2].decode("utf-8")#--------------------------------------------------------------------------------------------------------------
        print(decoded_bytes)

        current_menu = menu.get_current()

        if current_menu.get_title() != '' or not menu.is_enabled():
            slowed_reverb_screen()
        else:
            screen.fill('#111010')

        if decoded_bytes == "pushed":
            pushed_event=pygame.event.Event(pygame.USEREVENT, attr1='pushed_event')
            pygame.event.post(pushed_event)
            print(pushed_event.type)

        events = pygame.event.get()
        for event in events:
            print(event)
            if event.type == pygame.QUIT:
                exit()
            elif event.type == 32847 and current_menu.get_title() == '':
                menu.toggle()
            elif event.type == 32847 and current_menu.get_title() == 'Playlists':
                playlists_menu.toggle()

            #elif event.type == pygame.KEYDOWN:
            #    if event.key == pygame.K_ESCAPE and \
            #            current_menu.get_title() == 'MENU':
            #            menu.toggle()

        if menu.is_enabled():
            menu.draw(screen)
            menu.update(events)

        pygame.display.flip()

main()
