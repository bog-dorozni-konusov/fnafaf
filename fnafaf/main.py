import pygame
from menushka import MainMenu
from oficska import Office
from robotti import Robot
from cumera import CameraSystem

pygame.init()
window = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

menu = MainMenu(window)
office = Office(window)
freddy = Robot()
cams = CameraSystem(window)

state = "MENU"
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if state == "MENU":
                state = menu.check_click(event.pos)

        if event.type == pygame.KEYDOWN:
            if state == "GAME":
                if event.key == pygame.K_d:  # Кнопка D для дверей
                    office.door_closed = not office.door_closed
                if event.key == pygame.K_SPACE:  # Пробіл для камер
                    cams.is_on = not cams.is_on
                if cams.is_on:
                    if event.key == pygame.K_1: cams.current_cam = 1
                    if event.key == pygame.K_2: cams.current_cam = 2
                    if event.key == pygame.K_3: cams.current_cam = 3
                    if event.key == pygame.K_4: cams.current_cam = 4

    if state == "GAME":
        office.update(cams.is_on)
        freddy.update()
        if freddy.pos == 4:
            if office.door_closed:
                freddy.reset()
            else:
                state = "MENU"  # Програш
                freddy.reset()

    if state == "MENU":
        menu.draw()
    elif state == "GAME":
        office.draw()
        if cams.is_on:
            cams.draw(freddy.pos)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()