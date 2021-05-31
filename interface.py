import pygame
from pygame.locals import *

class Text:
    """Create a text object."""

    def __init__(self, text, pos, **options):
        self.text = text
        self.pos = pos

        self.fontname = None
        self.fontsize = 72
        self.fontcolor = Color('black')
        self.set_font()
        self.render()

    def set_font(self):
        """Set the Font object from name and size."""
        self.font = pygame.font.Font(self.fontname, self.fontsize)

    def render(self):
        """Render the text into an image."""
        self.img = self.font.render(self.text, True, self.fontcolor)
        self.rect = self.img.get_rect()
        self.rect.topleft = self.pos

    def draw(self):
        """Draw the text image to the screen."""
        Menu.screen.blit(self.img, self.rect)

class Menu:
    """Create a single-window app with multiple scenes."""

    def __init__(self):
        """Initialize pygame and the application."""
        pygame.init()
        flags = RESIZABLE
        Menu.screen = pygame.display.set_mode((1500, 980), flags)
        Menu.t = Text('lol', pos=(20, 20))

        Menu.running = True

    def run(self):
        """Run the main event loop."""
        while Menu.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    Menu.running = False

            Menu.screen.fill(Color('gray'))
            Menu.t.draw()
            pygame.display.update()

        pygame.quit()

if __name__ == '__main__':
    Menu().run()