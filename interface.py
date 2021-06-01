import pygame 

pygame.init()

height = 800
width = 650

screen = pygame.display.set_mode((height, width))


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
        if contador >= 1000:
            playlists()
            return 1
        
        pygame.display.update()

def playlists():
    running = True
    while running:
        screen.fill(('#111010'))
        pygame.display.update()

def mp3():
    running = True
    while running:
        screen.fill(('#111010'))

def weather():
    running = True
    while running:
        screen.fill(('#111010'))


menu()