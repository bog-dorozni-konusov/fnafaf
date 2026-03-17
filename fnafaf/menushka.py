import pygame
import random


class MainMenu:
    def init(self, screen):
        # ВАЖНО: два подчеркивания с каждой стороны!
        self.screen = screen
        self.font = pygame.font.SysFont("Arial", 60)
        self.btn = pygame.Rect(100, 300, 250, 60)

    def draw(self):
        self.screen.fill((0, 0, 0))
        # Рисуем помехи
        for _ in range(100):
            x = random.randint(0, 1280)
            y = random.randint(0, 720)
            pygame.draw.circle(self.screen, (100, 100, 100), (x, y), 1)

        # Текст и кнопка
        text = self.font.render("FNAF PROJECT", True, (255, 255, 255))
        self.screen.blit(text, (100, 100))
        pygame.draw.rect(self.screen, (150, 0, 0), self.btn)

    def check_click(self, pos):
        if self.btn.collidepoint(pos):
            return "GAME"
        return "MENU"