import init
from init import *


class Text:
    def __init__(self, size: int, place_cord, message_str: str, colour, button_color):
        self.font = pygame.font.Font(None, size)
        self.message = self.font.render(message_str, True, colour)
        self.rect = self.message.get_rect(center=place_cord)
        self.text = message_str
        self.place_cord = place_cord
        self.button_color = button_color
        self.button = Button((self.rect.width + 10, self.rect.height + 10), button_color)
        self.frame = Frame((self.rect.width + 10, self.rect.height + 10), init.BLACK)
        self.frame.visible = True

    def draw(self):
        self.button.draw((self.rect.x - 5, self.rect.y - 5))
        self.frame.draw((self.rect.x - 5, self.rect.y - 5))
        init.screen.blit(self.message, self.rect)

    def set_message(self, message_str):
        self.message = self.font.render(message_str, True, init.BLACK)
        self.rect = self.message.get_rect(center=self.place_cord)
        self.text = message_str

    def update(self, color):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            self.button.change_color(color)
        else:
            self.button.change_color(self.button_color)


class Frame:
    def __init__(self, size, color):
        self.parts = []
        self.size = size
        width = size[0]
        height = size[1]
        self.parts.append(pygame.Surface((4, size[1])))
        self.parts.append(pygame.Surface((size[0], 4)))
        self.parts.append(pygame.Surface((size[0], 4)))
        self.parts.append(pygame.Surface((4, size[1])))
        for ind in self.parts:
            ind.fill(color)
        self.visible = False

    def draw(self, place):
        if self.visible:
            init.screen.blit(self.parts[0], place)
            init.screen.blit(self.parts[1], place)
            init.screen.blit(self.parts[2], (place[0], place[1] + self.size[1] - 4))
            init.screen.blit(self.parts[3], (place[0] + self.size[0] - 4, place[1]))

    def set_place(self, place):
        self.place = place


class Button:
    def __init__(self, size, color):
        self.image = pygame.Surface(size)
        self.image.fill(color)

    def draw(self, place):
        init.screen.blit(self.image, place)

    def change_color(self, color):
        self.image.fill(color)