import pygame


SCREEN_WIDTH, SCREEN_HEIGHT = 504, 504
WIDTH, HEIGHT = 504, 504
ROWS = 14
SPAN = WIDTH // ROWS
# SPAN = 36
FPS = 10

pygame.init()
WIN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Snake')


FONT = pygame.font.Font('Media/FFFFORWA.TTF', 20)

SNAKE_HEAD = pygame.image.load('Media/snake_head.png')
SNAKE_BODY = pygame.image.load('Media/snake_body.png')
SNAKE_TAIL = pygame.image.load('Media/snake_tail.png')
BACKGROUND = pygame.image.load('Media/background.png')
BORDER = pygame.image.load('Media/border.png')
FOOD = pygame.image.load('Media/snake_food.png')
SNAKE_MENU_IMAGE = pygame.image.load("Media/snake_menu_image.png")
DESELECTED_PLAY_BUTTON = pygame.image.load('Media/deselected_play_button.png')
SELECTED_PLAY_BUTTON = pygame.image.load('Media/selected_play_button.png')
DESELECTED_QUIT_BUTTON = pygame.image.load('Media/deselected_quit_button.png')
SELECTED_QUIT_BUTTON = pygame.image.load('Media/selected_quit_button.png')
GAME_OVER = pygame.image.load('Media/game_over.png')

MOVE_SOUND = pygame.mixer.Sound('Media/move_sound_snake_2.wav')
MOVE_SOUND.set_volume(0.3)
BITE_SOUND = pygame.mixer.Sound('Media/apple_bite.wav')
GAME_OVER_SOUND = pygame.mixer.Sound('Media/snake_game_over_sound.wav')
GAME_OVER_SOUND.set_volume(0.3)
CLICK_SOUND = pygame.mixer.Sound('Media/snake_click.mp3')
CLICK_SOUND.set_volume(0.5)

LIGHT_GREY = (150, 150, 150)
