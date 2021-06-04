import pygame 
import pygame_menu


pygame.init()

width = 800
height = 650

screen = pygame.display.set_mode((width, height))


def menu():
    running = True
    contador = 0
    while running:
        screen.fill(('#111010')) # #111010 = black
        #Text: Music
        font = pygame.font.SysFont(None, 48)
        img = font.render('Music', True, ('#f6f6f6')) # #f6f6f6 = white
        screen.blit(img, (210,415))
        #Musicicon2
        image = pygame.image.load('D:\Programacion\Programs\mp3\pics\musicicon2.png')
        image.convert()
        image = pygame.transform.scale(image, (200,200))
        screen.blit(image, (155,180))
        #Weather
        image = pygame.image.load('D:\Programacion\Programs\mp3\pics\weather.png')
        image.convert()
        image = pygame.transform.scale(image, (200,200))
        screen.blit(image, (440,180))
        #Text: Weather
        font2 = pygame.font.SysFont(None, 48)
        img2 = font.render('Weather', True, ('#f6f6f6')) # #f6f6f6 = white
        screen.blit(img2, (473,415))

        contador += 1
        print(contador)
        if contador >= 50   :
            playlists()
            return 1
        
        pygame.display.update()


def mp3():
    running = True
    while running:
        screen.fill(('#111010'))


def playlists():
    running = True
    while running:
        mytheme = pygame_menu.themes.THEME_DARK.copy()

        mytheme.title_background_color=('#fc3a4b') # This line puts the title background in some kind of red color
        mytheme.title_bar_style =  pygame_menu.widgets.MENUBAR_STYLE_SIMPLE
        mytheme.title_offset = (20,0)
        mytheme.background_color=('#111010') # Black
        mytheme.widget_font_size = 45

        menu = pygame_menu.Menu(
            height=650, #height
            theme=mytheme,
            title='Playlists',
            width=800
        )
        menu.add_image('D:\Programacion\Programs\mp3\pics\slow.jpg', scale=(0.25,0.25),margin=(-370,15))
        menu.add_image('D:\Programacion\Programs\mp3\pics\live.jpg', scale=(0.25,0.25),margin=(-370,15))
        menu.add_image('D:\Programacion\Programs\mp3\pics\classicmusic.jpg', scale=(0.09,0.09),margin=(-370,15))
        menu.add_image('D:\Programacion\Programs\mp3\pics\ock.jpg', scale=(0.25,0.25),margin=(-370,-305))


        menu.add.button('Slowed & Reverb', mp3, margin=(-140,12))
        menu.add.button('Live', mp3, margin=(-280,10))
        menu.add.button('Classic', mp3, margin=(-252,10))
        menu.add.button('Rock', mp3, margin=(-269,0))
        menu.add_vertical_margin(230)

def mp3():
    running = True
    while running:
        screen.fill(('#111010'))

def weather():
    running = True
    while running:
        screen.fill(('#111010'))


menu()