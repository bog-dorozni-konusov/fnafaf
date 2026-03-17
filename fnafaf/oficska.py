import pygame


class Office:
    def init(self, screen):
        self.screen = screen
        self.door_closed = False
        self.power = 100.0

    def draw(self):
        self.screen.fill((40, 40, 45))  # Цвет офиса
        # Если дверь закрыта — рисуем красную панель
        color = (200, 0, 0) if self.door_closed else (50, 50, 50)
        pygame.draw.rect(self.screen, color, (0, 100, 50, 500))

        # Энергия
        if self.door_closed:
            self.power -= 0.02  # Энергия тратится быстрее при закрытой двери

    def toggle_door(self):
        self.door_closed = not self.door_closed
