import pygame
import random
from map import Tile, Map
from snake import Snake
from text import Text, Frame, Button
import json

WIDTH = 1200  # ширина игрового окна
HEIGHT = 600  # высота игрового окна
FPS = 30  # частота кадров в секунду

# Цвета (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)
LIGHT_GREY = (192, 192, 192)
PURPLE = (128, 0, 255)
CYAN = (0, 255, 255)
YELLOW = (255, 255, 0)


# создаем игру и окно
pygame.init()
pygame.mixer.init()  # для звука
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
images = []
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()

game_map = Map()
snake_movement_speed = 10
snake_movement_timer = 0
game = True

with open('maps.txt', 'r') as fr:
    # читаем из файла
    lst = json.load(fr)

game_map.restart(lst[random.randint(0, 2)])

gio_message = Text(54, (WIDTH / 2, HEIGHT / 2 - 60), "GAME IS OVER", BLACK, YELLOW)
pa_message = Text(36, (WIDTH / 2, HEIGHT / 2 + 10), "Play again?", BLACK, CYAN)
yes_message = Text(36, (WIDTH / 2 - 40, HEIGHT / 2 + 60), "YES", BLACK, GREEN)
no_message = Text(36, (WIDTH / 2 + 40, HEIGHT / 2 + 60), "NO", BLACK, RED)
apple_message = Text(36, (70, 25), "APPLES: " + str(game_map.apple_count), BLACK, LIGHT_GREY)

sounds = ['1.mp3', '2.mp3']