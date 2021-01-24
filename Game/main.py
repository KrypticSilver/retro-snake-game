import pygame
import random
import time
import itertools
from Data.constants import *


class Cube:
    snack = ()
    cube_nums = 0

    def __init__(self, pos, dir_x, dir_y):
        self.pos = pos
        self.dir_x = dir_x
        self.dir_y = dir_y
        self.num = Cube.cube_nums
        Cube.cube_nums += 1

    @classmethod
    def add_snack(cls, snake):
        if cls.snack == ():
            while True:
                on_snake = False
                x = random.randint(0, ROWS - 1) * SPAN
                y = random.randint(2, ROWS - 1) * SPAN
                for i in snake.body:
                    if i.pos == (x, y):
                        on_snake = True

                if not on_snake:
                    cls.snack = (x, y)
                    break

        WIN.blit(FOOD, cls.snack)


class Snake:
    def __init__(self):
        self.body = []
        self.body.append(Cube((WIDTH / 2, SPAN * 3), 0, 1))
        self.body.append(Cube((self.body[0].pos[0], self.body[0].pos[1] - SPAN), 0, 1))
        self.body.append(Cube((self.body[0].pos[0], self.body[0].pos[1] - SPAN * 2), 0, 1))

    def draw(self):
        for i in self.body:
            if i.dir_x == 1:
                rotation = 270

            elif i.dir_x == -1:
                rotation = 90

            elif i.dir_y == 1:
                rotation = 180

            elif i.dir_y == -1:
                rotation = 0

            if i.num == 0:
                WIN.blit(pygame.transform.rotate(SNAKE_HEAD, rotation), i.pos)

            elif i.num == len(self.body) - 1:
                WIN.blit(pygame.transform.rotate(SNAKE_TAIL, rotation), i.pos)

            else:

                WIN.blit(SNAKE_BODY, i.pos)

    def add_cube(self):
        self.body.append(Cube(self.body[- 1].pos, self.body[- 1].dir_x, self.body[- 1].dir_y))


def handle_movement(keys_pressed, snake):
    Cube.add_snack(snake)

    if snake.body[0].pos == Cube.snack:
        snake.add_cube()
        Cube.snack = ()
        pygame.mixer.Sound.play(BITE_SOUND)

    for i in snake.body[:0: - 1]:
        i.pos = snake.body[snake.body.index(i) - 1].pos
        i.dir_x, i.dir_y = snake.body[snake.body.index(i) - 1].dir_x, snake.body[snake.body.index(i) - 1].dir_y

    if keys_pressed[pygame.K_UP] and snake.body[0].dir_y != 1:
        if snake.body[0].dir_y != - 1:
            pygame.mixer.Sound.play(MOVE_SOUND)
        snake.body[0].dir_y = - 1
        snake.body[0].dir_x = 0
    elif keys_pressed[pygame.K_DOWN] and snake.body[0].dir_y != - 1:
        if snake.body[0].dir_y != 1:
            pygame.mixer.Sound.play(MOVE_SOUND)
        snake.body[0].dir_y = 1
        snake.body[0].dir_x = 0
    elif keys_pressed[pygame.K_LEFT] and snake.body[0].dir_x != 1:
        if snake.body[0].dir_x != - 1:
            pygame.mixer.Sound.play(MOVE_SOUND)
        snake.body[0].dir_x = - 1
        snake.body[0].dir_y = 0
    elif keys_pressed[pygame.K_RIGHT] and snake.body[0].dir_x != - 1:
        if snake.body[0].dir_x != 1:
            pygame.mixer.Sound.play(MOVE_SOUND)
        snake.body[0].dir_x = 1
        snake.body[0].dir_y = 0

    snake.body[0].pos = (snake.body[0].pos[0] + snake.body[0].dir_x * SPAN, snake.body[0].pos[1]
                         + snake.body[0].dir_y * SPAN)

    if snake.body[0].pos[0] < 0 or snake.body[0].pos[0] + SPAN > WIDTH or snake.body[0].pos[1] < SPAN\
            or snake.body[0].pos[1] + SPAN > WIDTH:
        del snake
        Cube.cube_nums = 0
        Cube.snack = ()

        pygame.mixer.Sound.play(GAME_OVER_SOUND)
        WIN.blit(GAME_OVER, (25, 195))
        pygame.display.update()
        time.sleep(2)
        main_menu()

    for i in itertools.product(snake.body, repeat=2):
        if i[0].pos == i[1].pos and i[0].num != i[1].num:
            del snake
            Cube.cube_nums = 0
            Cube.snack = ()

            pygame.mixer.Sound.play(GAME_OVER_SOUND)
            WIN.blit(GAME_OVER, (25, 195))
            pygame.display.update()
            time.sleep(2)
            main_menu()


def draw_window():
    WIN.blit(BACKGROUND, (0, SPAN))


def draw_grid(snake):
    for i in range(SPAN, WIDTH, SPAN):
        pygame.draw.line(WIN, LIGHT_GREY, (i, 0), (i, WIDTH))
        pygame.draw.line(WIN, LIGHT_GREY, (0, i), (WIDTH, i))

    WIN.blit(BORDER, (0, 0))

    text_surface = FONT.render(f'Score: {len(snake.body) - 3}', False, (255, 255, 255))
    WIN.blit(text_surface, (365, 6))


def main():
    clock = pygame.time.Clock()
    snake = Snake()
    run = True

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()

        draw_window()
        handle_movement(pygame.key.get_pressed(), snake)
        snake.draw()
        draw_grid(snake)

        pygame.display.update()



def main_menu():
    clock = pygame.time.Clock()

    run = True

    while run:
        clock.tick(FPS)
        WIN.blit(SNAKE_MENU_IMAGE, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 295 < pygame.mouse.get_pos()[0] < 470 \
                        and 200 < pygame.mouse.get_pos()[1] < 270:
                    pygame.mixer.Sound.play(CLICK_SOUND)
                    main()

                elif 295 < pygame.mouse.get_pos()[0] < 470 \
                        and 280 < pygame.mouse.get_pos()[1] < 350:
                    pygame.mixer.Sound.play(CLICK_SOUND)
                    pygame.quit()
                    quit()

        if 295 < pygame.mouse.get_pos()[0] < 470 \
                and 200 < pygame.mouse.get_pos()[1] < 270:
            WIN.blit(SELECTED_PLAY_BUTTON, (295, 200))
            WIN.blit(DESELECTED_QUIT_BUTTON, (295, 280))

        elif 295 < pygame.mouse.get_pos()[0] < 470 \
                and 280 < pygame.mouse.get_pos()[1] < 350:
            WIN.blit(DESELECTED_PLAY_BUTTON, (295, 200))
            WIN.blit(SELECTED_QUIT_BUTTON, (295, 280))

        else:
            WIN.blit(DESELECTED_PLAY_BUTTON, (295, 200))
            WIN.blit(DESELECTED_QUIT_BUTTON, (295, 280))

        pygame.display.update()


if __name__ == '__main__':
    main_menu()
