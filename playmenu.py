import pygame
from pygame import mixer

pygame.init()

height = 800
width = 650

screen = pygame.display.set_mode((height, width))


def slowed_reverb():
    running = True
    contador = 0
    while running:
        screen.fill(('#111010')) # #111010 = black
        #Text: Music
        font = pygame.font.SysFont(None, 48)
        img = font.render('Slowed & reverb', True, ('#f6f6f6')) # #f6f6f6 = white
        screen.blit(img, (110,65))
        #Musicicon2
        image = pygame.image.load('C:/Users/brend/OneDrive/Documentos/REPO MP3/pics/slowed&reverb.jpg')
        image.convert()
        image = pygame.transform.scale(image, (50,50))
        screen.blit(image, (50,55))
        image = pygame.image.load('C:/Users/brend/OneDrive/Documentos/REPO MP3/pics/pausab.png')
        image.convert()
        image = pygame.transform.scale(image, (65,65))
        screen.blit(image, (375,450))
        image = pygame.image.load('C:/Users/brend/OneDrive/Documentos/REPO MP3/pics/playb.png')
        image.convert()
        image = pygame.transform.scale(image, (65,65))
        screen.blit(image, (310,451))
        image = pygame.image.load('C:/Users/brend/OneDrive/Documentos/REPO MP3/pics/prevsi.png')
        image.convert()
        image = pygame.transform.scale(image, (62,62))
        screen.blit(image, (242,452))
        image = pygame.image.load('C:/Users/brend/OneDrive/Documentos/REPO MP3/pics/ffsi.png')
        image.convert()
        image = pygame.transform.scale(image, (58,58))
        screen.blit(image, (445,452))
        image = pygame.image.load('C:/Users/brend/OneDrive/Documentos/REPO MP3/pics/shufflew.png')
        image.convert()
        image = pygame.transform.scale(image, (50,50))
        screen.blit(image, (512,456))
        image = pygame.image.load('C:/Users/brend/OneDrive/Documentos/REPO MP3/pics/vol.png')
        image.convert()
        image = pygame.transform.scale(image, (50,50))
        screen.blit(image, (188,456))
        contador += 1
        print(contador)
        if contador >= 100:
            return 1
    pygame.display.update()
slowed_reverb()
