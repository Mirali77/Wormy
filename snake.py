import init
from init import *


class Snake:
    def __init__(self):
        self.nodes = []
        for idx in range(4):
            self.nodes.append((init.WIDTH // 50 // 2 - 2 + idx, init.HEIGHT // 50 // 2))
        self.sides = ["LEFT", "UP", "RIGHT", "DOWN"]
        self.forward_side = "LEFT"
        self.after_last_node = (self.nodes[-1][0] + 1, self.nodes[-1][1])
        self.after_last_node_flag = False

    def restart(self):
        self.nodes.clear()
        for idx in range(4):
            self.nodes.append((init.WIDTH // 50 // 2 - 2 + idx, init.HEIGHT // 50 // 2))
        self.forward_side = "LEFT"
        self.after_last_node = (self.nodes[-1][0] + 1, self.nodes[-1][1])
        self.after_last_node_flag = False

    def turn_right(self):
        self.forward_side = self.sides[(self.sides.index(self.forward_side) + 1) % 4]

    def turn_left(self):
        self.forward_side = self.sides[self.sides.index(self.forward_side) - 1]

    def get_forward_tile(self):
        x, y = self.nodes[0][0], self.nodes[0][1]
        if self.forward_side == "LEFT":
            x -= 1
        elif self.forward_side == "UP":
            y -= 1
        elif self.forward_side == "RIGHT":
            x += 1
        elif self.forward_side == "DOWN":
            y += 1
        res = (x, y)
        return res

    def move(self):
        if not self.after_last_node_flag:
            self.after_last_node = self.nodes[-1]
        else:
            self.after_last_node_flag = False
        for idx in range(len(self.nodes) - 1, 0, -1):
            self.nodes[idx] = self.nodes[idx - 1]
        self.nodes[0] = self.get_forward_tile()

    def grow(self):
        self.nodes.append(self.nodes[-1])
        self.after_last_node_flag = True

    def get_apple_pos(self, walls):
        while True:
            pos = (random.randint(0, init.WIDTH // 50 - 1), random.randint(0, init.HEIGHT // 50 - 1))
            if pos not in self.nodes and pos != self.after_last_node and pos not in walls:
                return pos
