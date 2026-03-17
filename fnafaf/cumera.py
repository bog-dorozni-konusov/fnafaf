import pygame

class CameraSystem:
    def init(self):
        self.is_on = False
        self.current_cam = 1

    def draw(self, screen):
        if self.is_on:
            # Рисуем серую рамку камеры
            pygame.draw.rect(screen, (100, 100, 100), (50, 50, 1180, 620), 10)
