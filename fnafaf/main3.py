import pygame
import random

# Імпортуємо твої класи (переконайся, що назви файлів збігаються)
from menushka import MainMenu
from oficska import Office
from robotti import Robot
from cumera import CameraSystem


def main():
    # 1. Ініціалізація Pygame
    pygame.init()

    # 2. Створюємо вікно
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("FNAF UA PROJECT")
    clock = pygame.time.Clock()

    # 3. Створюємо об'єкти гри
    menu = MainMenu(screen)
    office = Office(screen)
    freddy = Robot()
    cams = CameraSystem(screen)

    state = "MENU"
    running = True

    # 4. ГОЛОВНИЙ ЦИКЛ (Це серце гри)
    while running:
        # Перевірка подій (мишка, кнопки)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if state == "MENU":
                    # Перевіряємо клік у меню
                    new_state = menu.check_click(event.pos)
                    if new_state == "GAME":
                        state = "GAME"

            if event.type == pygame.KEYDOWN:
                if state == "GAME":
                    if event.key == pygame.K_d:
                        office.door_closed = not office.door_closed
                    if event.key == pygame.K_SPACE:
                        cams.is_on = not cams.is_on

        # Логіка гри
        if state == "GAME":
            office.update(cams.is_on)
            freddy.update()

        # Малювання (Drawing)
        if state == "MENU":
            menu.draw()
        elif state == "GAME":
            office.draw()
            if cams.is_on:
                cams.draw(freddy.pos)

        # Оновлення екрана
        pygame.display.flip()
        # Обмежуємо до 60 кадрів на секунду
        clock.tick(60)

    pygame.quit()


# Запускаємо функцію main
if __name__ == "__main__":
    main()