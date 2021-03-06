import pygame.sprite

import init
from init import *
from snake import Snake


class Tile(pygame.sprite.Sprite):
    def __init__(self, size, place, group: pygame.sprite.Group):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(size)
        self.image.fill(init.BLACK)
        self.rect = self.image.get_rect()
        self.rect.topleft = place
        self.add(group)

    def paint(self, color):
        self.image.fill(color)


class Map:
    def __init__(self):
        self.field = []
        for idx1 in range(init.WIDTH // 50):
            row = []
            for idx2 in range(init.HEIGHT // 50):
                row.append(Tile((49, 49), (idx1 * 50, idx2 * 50), init.all_sprites))
            self.field.append(row)
        self.snake = Snake()
        self.walls = []
        self.apple = self.snake.get_apple_pos(self.walls)
        self.apple_count = 0

    def make_picture(self):
        self.field[self.apple[0]][self.apple[1]].paint(init.RED)
        for idx in self.walls:
            self.field[idx[0]][idx[1]].paint(init.GREY)
        for idx in self.snake.nodes:
            self.field[idx[0]][idx[1]].paint(init.GREEN)
        pos = self.snake.after_last_node
        self.field[pos[0]][pos[1]].paint(init.BLACK)

    def turn_snake(self, key):
        if key == pygame.K_LEFT:
            self.snake.turn_left()
        else:
            self.snake.turn_right()

    def move_snake(self):
        pos = self.snake.get_forward_tile()
        if pos in self.walls or pos[0] * pos[1] < 0 or pos[0] >= init.WIDTH // 50 or pos[1] >= init.HEIGHT // 50 or \
                pos in self.snake.nodes:
            pygame.mixer.music.load(init.sounds[1])
            pygame.mixer.music.play()
            return False
        else:
            if pos == self.apple:
                self.apple = self.snake.get_apple_pos(self.walls)
                self.snake.grow()
                self.apple_count += 1
                pygame.mixer.music.load(init.sounds[0])
                pygame.mixer.music.play()
            self.snake.move()
        return True

    def clear(self):
        for row in self.field:
            for tile in row:
                tile.kill()

    def restart(self, walls):
        pygame.mixer.music.stop()
        self.clear()
        self.field = []
        for idx1 in range(init.WIDTH // 50):
            row = []
            for idx2 in range(init.HEIGHT // 50):
                row.append(Tile((49, 49), (idx1 * 50, idx2 * 50), init.all_sprites))
            self.field.append(row)
        self.walls = []
        for pos in walls:
            if pos[0] < 0:
                pos[0] += len(self.field)
            if pos[1] < 0:
                pos[1] += len(self.field[0])
        for wall in walls:
            self.walls.append((wall[0], wall[1]))
        self.snake.restart()
        self.apple = self.snake.get_apple_pos(self.walls)
        self.apple_count = 0


