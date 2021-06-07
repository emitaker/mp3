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
        screen.fill(('#111010'))
        font = pygame.font.SysFont(None, 48)
        img = font.render('live', True, ('#f6f6f6')) # #f6f6f6 = white
        screen.blit(img, (110,65))
        font2 = pygame.font.SysFont(None, 30)
        img = font2.render('Puesto - Babasonicos', True, ('#f6f6f6'))
        screen.blit(img, (280,405))

        image = pygame.image.load('D:\Programacion\Programs\mp3\pics\ock_logo.bmp')
        image = pygame.transform.scale(image, (380,230))
        screen.blit(image, (200,150))

        #Musicicon2
        image = pygame.image.load('D:\Programacion\Programs\mp3\pics\slow.bmp')

        image = pygame.transform.scale(image, (50,50))
        screen.blit(image, (50,55))
        image = pygame.image.load('D:\Programacion\Programs\mp3\pics\pausab.bmp')

        image = pygame.transform.scale(image, (65,65))
        screen.blit(image, (375,450))
        image = pygame.image.load('D:\Programacion\Programs\mp3\pics\playb.bmp')

        image = pygame.transform.scale(image, (65,65))
        screen.blit(image, (310,451))
        image = pygame.image.load('D:\Programacion\Programs\mp3\pics\prevsi.bmp')

        image = pygame.transform.scale(image, (62,62))
        screen.blit(image, (242,452))
        
        image = pygame.image.load('D:\Programacion\Programs\mp3\pics\shufflew.bmp')

        image = pygame.transform.scale(image, (50,50))
        screen.blit(image, (512,456))
        

        pygame.display.update()
        contador += 1
        print(contador)
        if contador >= 50   :
            return 1
        

menu()