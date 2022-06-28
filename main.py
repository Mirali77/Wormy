import pygame

from init import *


# Цикл игры
running = True
while running:
    # держим цикл на правильной скорости
    clock.tick(FPS)

    # Ввод процесса (события)
    for event in pygame.event.get():
        # проверить закрытие окна
        if event.type == pygame.QUIT:
            running = False
        if game:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    game_map.turn_snake(event.key)
        else:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if yes_message.rect.collidepoint(event.pos):
                    game = True
                    game_map.restart()
                elif no_message.rect.collidepoint(event.pos):
                    running = False

    # Обновление
    game_map.make_picture()
    if game:
        if snake_movement_timer == snake_movement_speed:
            snake_movement_timer = 0
            game = game_map.move_snake()
        snake_movement_timer += 1
    all_sprites.update()
    screen.fill(GREY)
    all_sprites.draw(screen)
    if not game:
        gio_message.draw()
        pa_message.draw()
        yes_message.draw()
        no_message.draw()
        yes_message.update(PURPLE)
        no_message.update(PURPLE)

    # Визуализация (сборка)
    pygame.display.flip()

pygame.quit()