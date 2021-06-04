import pygame
import pygame_menu
import main
import vlc


playlist = main.playlist
print(playlist)

pygame.init()
screen = pygame.display.set_mode((800, 650))
    

#-------------------------------------------------------------------------
#
#Weather Menu
#
#-------------------------------------------------------------------------
def weather():
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
        joystick_enabled=True
        )

    weather_menu.add.button('Back',main_menu)
    weather_menu.mainloop(screen)

#------------------------------------------------------
#
#slowed and reverb menu
#
#------------------------------------------------------    
def slowed_reverb():
    global playlist
    playlist = 1
    print(playlist)
    slowed_reverb_theme = pygame_menu.themes.THEME_DARK.copy()
    slowed_reverb_theme.title_bar_style =  pygame_menu.widgets.MENUBAR_STYLE_NONE
    slowed_reverb_theme.title_offset = (20,0)
    slowed_reverb_theme.background_color=('#111010') # Black
    slowed_reverb_theme.widget_font_size = 45

    slowed_reverb_menu = pygame_menu.Menu(
            height=650, #height
            theme=slowed_reverb_theme,
            title='',
            width=800,
            joystick_enabled=True
        )

    #slowed_reverb_menu.add_image('D:\Programacion\Programs\mp3\pics\slow.jpg', scale=(0.5,0.5),margin=(-370,15))
    slowed_reverb_menu.add_image('/home/pi/Documents/mp3/pics/slow.jpg', scale=(0.5,0.5),margin=(-370,15))

    slowed_reverb_menu.add.button('Back',playlists)
    slowed_reverb_menu.mainloop(screen)

#------------------------------------------------------
#
#Live music menu
#
#------------------------------------------------------
def live():
    global playlist
    playlist = 2
    print(playlist)
    live_theme = pygame_menu.themes.THEME_DARK.copy()
    live_theme.title_bar_style =  pygame_menu.widgets.MENUBAR_STYLE_NONE
    live_theme.title_offset = (20,0)
    live_theme.background_color=('#111010') # Black
    live_theme.widget_font_size = 45

    live_menu = pygame_menu.Menu(
        height=650, #height
        theme=live_theme,
        title='',
        width=800,
        joystick_enabled=True
        )

    #live_menu.add_image('D:\Programacion\Programs\mp3\pics\live.jpg', scale=(0.5,0.5),margin=(-370,15))
    live_menu.add_image('/home/pi/Documents/mp3/pics/live.jpg', scale=(0.5,0.5),margin=(-370,15))


    live_menu.add.button('Back',playlists)
    live_menu.mainloop(screen)

#------------------------------------------------------
#
#Classic music menu
#
#------------------------------------------------------
def classic():
    global playlist
    playlist = 3
    print(playlist)
    classic_theme = pygame_menu.themes.THEME_DARK.copy()
    classic_theme.title_bar_style =  pygame_menu.widgets.MENUBAR_STYLE_NONE
    classic_theme.title_offset = (20,0)
    classic_theme.background_color=('#111010') # Black
    classic_theme.widget_font_size = 45

    classic_menu = pygame_menu.Menu(
        height=650, #height
        theme=classic_theme,
        title='',
        width=800,
        joystick_enabled=True
        )

    #classic_menu.add_image('D:\Programacion\Programs\mp3\pics\classicmusic.jpg', scale=(0.5,0.5),margin=(-370,15))
    classic_menu.add_image('/home/pi/Documents/mp3/pics/classicmusic.jpg', scale=(0.5,0.5),margin=(-370,15))


    classic_menu.add.button('Back',playlists)
    classic_menu.mainloop(screen)

#------------------------------------------------------
#
#Rock menu
#
#------------------------------------------------------
def rock():
    global playlist
    playlist = 4
    print(playlist)
    rock_theme = pygame_menu.themes.THEME_DARK.copy()
    rock_theme.title_bar_style =  pygame_menu.widgets.MENUBAR_STYLE_NONE
    rock_theme.title_offset = (20,0)
    rock_theme.background_color=('#111010') # Black
    rock_theme.widget_font_size = 45

    rock_menu = pygame_menu.Menu(
        height=650, #height
        theme=rock_theme,
        title='',
        width=800,
        joystick_enabled=True
        )

    #rock_menu.add_image('D:\Programacion\Programs\mp3\pics\ock.jpg', scale=(0.5,0.5),margin=(-370,-305))
    rock_menu.add_image('/home/pi/Documents/mp3/pics/ock.jpg', scale=(0.5,0.5),margin=(-370,-305))


    rock_menu.add.button('Back',playlists)
    rock_menu.mainloop(screen)
#-------------------------------------------------------------------------
#
#Playlists Menu
#
#-------------------------------------------------------------------------
def playlists():
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
        joystick_enabled=True
        )

    #playlists_menu.add_image('D:\Programacion\Programs\mp3\pics\slow.jpg', scale=(0.25,0.25),margin=(-370,15))
    #playlists_menu.add_image('D:\Programacion\Programs\mp3\pics\live.jpg', scale=(0.25,0.25),margin=(-370,15))
    #playlists_menu.add_image('D:\Programacion\Programs\mp3\pics\classicmusic.jpg', scale=(0.09,0.09),margin=(-370,15))
    #playlists_menu.add_image('D:\Programacion\Programs\mp3\pics\ock.jpg', scale=(0.25,0.25),margin=(-370,-305))
    
    playlists_menu.add_image('/home/pi/Documents/mp3/pics/slow.jpg', scale=(0.25,0.25),margin=(-370,15))
    playlists_menu.add_image('/home/pi/Documents/mp3/pics/live.jpg', scale=(0.25,0.25),margin=(-370,15))
    playlists_menu.add_image('/home/pi/Documents/mp3/pics/classicmusic.jpg', scale=(0.09,0.09),margin=(-370,15))
    playlists_menu.add_image('/home/pi/Documents/mp3/pics/ock.jpg', scale=(0.25,0.25),margin=(-370,-305))


    playlists_menu.add.button('Slowed & Reverb', slowed_reverb, margin=(-140,12))
    playlists_menu.add.button('Live', live, margin=(-280,10))
    playlists_menu.add.button('Classic',classic, margin=(-252,10))
    playlists_menu.add.button('Rock',rock, margin=(-269,10))
    playlists_menu.add.button('Back',main_menu, margin=(-269,0))
    playlists_menu.add_vertical_margin(230)

    playlists_menu.mainloop(screen)

#-------------------------------------------------------------------------
#
#Main Menu
#
#-------------------------------------------------------------------------
def main_menu():
    main_menu_theme = pygame_menu.themes.THEME_DARK.copy()
    main_menu_theme.title_bar_style =  pygame_menu.widgets.MENUBAR_STYLE_NONE
    main_menu_theme.background_color=('#111010') # Black
    main_menu_theme.widget_font_size = 55

    menu = pygame_menu.Menu(
        height=650, #height
        theme=main_menu_theme,
        title='',
        width=800,
        joystick_enabled=True
        )

    #menu.add_image('D:\Programacion\Programs\mp3\pics\musicicon2.png', scale=(.2,.2),margin=(-170,-211))
    #menu.add_image('D:\Programacion\Programs\mp3\pics\weather.png', scale=(.2,.2),margin=(170,20))

    menu.add_image('/home/pi/Documents/mp3/pics/musicicon2.png', scale=(.2,.2),margin=(-170,-211))
    menu.add_image('/home/pi/Documents/mp3/pics/weather.png', scale=(.2,.2),margin=(170,20))

    menu.add.button('Music', playlists, margin=(-167,-85))
    menu.add.button('Weather', weather,margin=(174,0))
    menu.add_vertical_margin(120)

    menu.mainloop(screen)

main_menu()