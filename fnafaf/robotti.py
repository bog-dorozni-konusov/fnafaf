import pygame
import random

class Robot:
    def init(self, name, level):
        self.name = name
        self.level = level
        self.pos = 0 # 0 - сцена, 4 - у двери
        self.last_update = pygame.time.get_ticks()

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 4000: # Каждые 4 сек попытка хода
            self.last_update = now
            if random.randint(1, 20) <= self.level:
                self.pos += 1
                print(f"{self.name} на позиции {self.pos}")
