import pygame
import sys
import random

# Inițializarea Pygame
pygame.init()

# Dimensiunile ferestrei
width, height = 400, 400
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Culori
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Dimensiunea blocului și viteză
block_size = 20
snake_speed = 50

# Inițializarea poziției inițiale a șarpelui
x, y = width // 2, height // 2
x_speed, y_speed = 0, 0

# Inițializarea corpului șarpelui
snake = [(x, y)]

# Inițializarea mâncării
food_x, food_y = random.randrange(0, width, block_size), random.randrange(0, height, block_size)

# Scor
score = 0

# Funcție pentru afișarea scorului
font = pygame.font.Font(None, 36)

def show_score():
    score_text = font.render(f"Score: {score}", True, white)
    window.blit(score_text, (10, 10))

# Funcție pentru desenarea șarpelui
def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(window, white, [segment[0], segment[1], block_size, block_size])

# Funcție pentru desenarea mâncării
def draw_food(food_x, food_y):
    pygame.draw.rect(window, red, [food_x, food_y, block_size, block_size])

# Loop-ul principal al jocului
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and x_speed == 0:
                x_speed = -block_size
                y_speed = 0
            elif event.key == pygame.K_RIGHT and x_speed == 0:
                x_speed = block_size
                y_speed = 0
            elif event.key == pygame.K_UP and y_speed == 0:
                x_speed = 0
                y_speed = -block_size
            elif event.key == pygame.K_DOWN and y_speed == 0:
                x_speed = 0
                y_speed = block_size

    # Mișcarea șarpelui
    x += x_speed
    y += y_speed

    # Verificarea coliziunii cu mâncarea
    if x == food_x and y == food_y:
        score += 1
        food_x, food_y = random.randrange(0, width, block_size), random.randrange(0, height, block_size)
        snake.append((x, y))

    # Verificarea coliziunii cu pereții sau cu propriul corp
    if x >= width or x < 0 or y >= height or y < 0 or (x, y) in snake[:-1]:
        game_over = True

    # Adăugarea capului șarpelui la începutul listei
    snake.insert(0, (x, y))

    # Ștergerea ultimului segment din corpul șarpelui
    if len(snake) > score + 1:
        del snake[-1]

    # Ștergerea ecranului
    window.fill(black)

    # Desenarea șarpelui și a mâncării
    draw_snake(snake)
    draw_food(food_x, food_y)

    # Afișarea scorului
    show_score()

    # Actualizarea ecranului
    pygame.display.update()

    # Controlul vitezei jocului
    pygame.time.delay(snake_speed)

# Închiderea Pygame
pygame.quit()
sys.exit()