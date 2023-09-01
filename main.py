import pygame

pygame.init()

WIDTH, HEIGHT = 1200, 800
GRID_CELL_SIZE = 60

WHITE = (255, 255, 255)
GRID_COLOR = (100, 100, 100)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Tower of God Game")


def draw_screen_segments():
    pygame.draw.line(
        screen,
        GRID_COLOR,
        (WIDTH * (1 / 5), 0),
        (WIDTH * (1 / 5), HEIGHT),
        5,
    )
    pygame.draw.line(
        screen,
        GRID_COLOR,
        (WIDTH - WIDTH * (1 / 5), 0),
        (WIDTH - WIDTH * (1 / 5), HEIGHT),
        5,
    )

    draw_grid()


def draw_grid():
    start_x = int(1 / 5 * WIDTH) + GRID_CELL_SIZE
    end_x = int(4 / 5 * WIDTH) - GRID_CELL_SIZE
    start_y = int((HEIGHT - 3 / 5 * WIDTH) / 2) + GRID_CELL_SIZE
    end_y = int(HEIGHT - (HEIGHT - 3 / 5 * WIDTH) / 2) - GRID_CELL_SIZE

    # vertical lines
    for x in range(start_x, end_x + 1, GRID_CELL_SIZE):
        pygame.draw.line(screen, GRID_COLOR, (x, start_y), (x, end_y), 2)

    # horizontal lines
    for y in range(start_y, end_y + 1, GRID_CELL_SIZE):
        pygame.draw.line(screen, GRID_COLOR, (start_x, y), (end_x, y), 2)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    draw_screen_segments()

    pygame.display.update()
    clock.tick(60)

# Quit Pygame
pygame.quit()
