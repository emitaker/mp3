screen.fill(('#111010')) # #111010 = black
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
contador += 1
pygame.display.update()
