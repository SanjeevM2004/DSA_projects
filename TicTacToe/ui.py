import pygame
import tictactoe

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 0, 0)

# Initialize Pygame
pygame.init()

# Screen size
SIZE = (500, 500)
LINE_WIDTH = 25

# Create the screen
screen = pygame.display.set_mode(SIZE)

# Font
font = pygame.font.SysFont(None, 75)

def draw_board(board):
    screen.fill(WHITE)
    # Draw grid
    pygame.draw.line(screen, BLACK, (0, 167), (500, 167), LINE_WIDTH)
    pygame.draw.line(screen, BLACK, (0, 334), (500, 334), LINE_WIDTH)
    pygame.draw.line(screen, BLACK, (167, 0), (167, 500), LINE_WIDTH)
    pygame.draw.line(screen, BLACK, (334, 0), (334, 500), LINE_WIDTH)

    for x in range(3):
        for y in range(3):
            if board[x][y] == 'X':
                color = BLUE
            elif board[x][y] == 'O':
                color = RED
            else:
                continue
            text = font.render(board[x][y], True, color)
            screen.blit(text, (y * 167 + 55, x * 167 + 55))

    pygame.display.update()

def check_click(pos):
    x, y = pos
    return y // 167, x // 167

def show_message(message):
    screen.fill(WHITE)
    text = font.render(message, True, GREEN)
    screen.blit(text, (100, 200))
    pygame.display.update()
    pygame.time.wait(2000)
