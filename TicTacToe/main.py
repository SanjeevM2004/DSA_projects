import pygame
from tictactoe import TicTacToe
from ui import draw_board, check_click, show_message

# Initialize the game
game = TicTacToe()

# Initialize Pygame
pygame.init()

# Screen size
SIZE = (500, 500)
screen = pygame.display.set_mode(SIZE)

# Game loop
running = True
current_player = 'X'
while running:
    draw_board(game.board)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            row, col = check_click(pos)
            try:
                result = game.add(current_player, row, col)
                if result:
                    show_message(result)
                    game = TicTacToe()  # Reset the game
                current_player = 'O' if current_player == 'X' else 'X'
            except Exception as e:
                print(e)
    pygame.display.update()

pygame.quit()
