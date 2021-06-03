import pygame
import pygame_menu

pygame.init()
screen = pygame.display.set_mode((800, 650))

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
    width=800
    )

weather_menu.add.button('Back',pygame_menu.events.BACK)


#-------------------------------------------------------------------------
#
#Music Menu
#
#-------------------------------------------------------------------------

music_theme = pygame_menu.themes.THEME_DARK.copy()
music_theme.title_background_color=('#fc3a4b') # This line puts the title background in some kind of red color
music_theme.title_bar_style =  pygame_menu.widgets.MENUBAR_STYLE_SIMPLE
music_theme.title_offset = (20,0)
music_theme.background_color=('#111010') # Black
music_theme.widget_font_size = 45

music_menu = pygame_menu.Menu(
    height=650, #height
    theme=music_theme,
    title='Music',
    width=800
    )

music_menu.add.button('Back',pygame_menu.events.BACK)

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
    joystick_enabled=True
    )
playlists_menu.add_image('D:\Programacion\Programs\mp3\pics\slow.jpg', scale=(0.25,0.25),margin=(-370,15))
playlists_menu.add_image('D:\Programacion\Programs\mp3\pics\live.jpg', scale=(0.25,0.25),margin=(-370,15))
playlists_menu.add_image('D:\Programacion\Programs\mp3\pics\classicmusic.jpg', scale=(0.09,0.09),margin=(-370,15))
playlists_menu.add_image('D:\Programacion\Programs\mp3\pics\ock.jpg', scale=(0.25,0.25),margin=(-370,-305))


playlists_menu.add.button('Slowed & Reverb', music_menu, margin=(-140,12))
playlists_menu.add.button('Live', music_menu, margin=(-280,10))
playlists_menu.add.button('Classic',music_menu, margin=(-252,10))
playlists_menu.add.button('Rock',music_menu, margin=(-269,10))
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

main_menu = pygame_menu.Menu(
    height=650, #height
    theme=main_menu_theme,
    title='',
    width=800
    )


main_menu.add_image('D:\Programacion\Programs\mp3\pics\musicicon2.png', scale=(.2,.2),margin=(-170,-211))
main_menu.add_image('D:\Programacion\Programs\mp3\pics\weather.png', scale=(.2,.2),margin=(170,20))

main_menu.add.button('Music', playlists_menu, margin=(-167,-85))
main_menu.add.button('Weather', weather_menu,margin=(174,0))
main_menu.add_vertical_margin(120)

main_menu.mainloop(screen)

#menu.add.button('Quit', pygame_menu.events.EXIT)
