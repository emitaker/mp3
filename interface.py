import pygame
import pygame_menu


pygame.init()
screen = pygame.display.set_mode((800, 650))


#------------------------------------------------------
#
#slowed and reverb menu
#
#------------------------------------------------------
def slowed_reverb():
    global playlist
    playlist = 1
    print(playlist)

#------------------------------------------------------
#
#Live music menu
#
#------------------------------------------------------
def live():
    global playlist
    playlist = 2
    print(playlist)

#------------------------------------------------------
#
#Classic music menu
#
#------------------------------------------------------
def classic():
    global playlist
    playlist = 3
    print(playlist)

#------------------------------------------------------
#
#Rock menu
#
#------------------------------------------------------
def rock():
    global playlist
    playlist = 4
    print(playlist)
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
    joystick_enabled=True
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
playlists_menu.add.button('Back',pygame_menu.events.BACK, margin=(-269,0))


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

menu.add.image('/home/pi/Documents/mp3/pics/musicicon2.png', scale=(.2,.2),margin=(-170,-211))
menu.add.image('/home/pi/Documents/mp3/pics/weather.png', scale=(.2,.2),margin=(170,20))

menu.add.button('Music', playlists, margin=(-167,-85))
menu.add.button('Weather', weather,margin=(174,0))



main_menu()
