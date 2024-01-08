import pygame
import random
import button

pygame.init()

SCREEN_WIDTH = 399
SCREEN_HEIGHT = 399

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player_turn = True
isrunning = True
ispressed = False

# List to store the positions of clicked circles (player's moves)
clicked_circles = []
# List to store the positions of computer's crosses
computer_clicked_crosses = []

def check_winner(board):
    # Check rows, columns, and diagonals for a winner
    for i in range(3):
        if all(board[i][j] == 'O' for j in range(3)) or all(board[j][i] == 'O' for j in range(3)):
            return "Player wins!"
        elif all(board[i][j] == 'X' for j in range(3)) or all(board[j][i] == 'X' for j in range(3)):
            return "Computer wins!"

    if board[0][0] == board[1][1] == board[2][2] == 'O' or board[0][2] == board[1][1] == board[2][0] == 'O':
        return "Player wins!"
    elif board[0][0] == board[1][1] == board[2][2] == 'X' or board[0][2] == board[1][1] == board[2][0] == 'X':
        return "Computer wins!"

    return None

# Initialize an empty 3x3 game board
board = [['' for _ in range(3)] for _ in range(3)]

while isrunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isrunning = False
        if event.type == pygame.MOUSEBUTTONDOWN and player_turn:
            ispressed = True
        if event.type == pygame.MOUSEBUTTONUP and player_turn:
            ispressed = False
            player_turn_time = pygame.time.get_ticks()
    
    screen.fill("black")

    rects = [pygame.Rect(0, 0, 133, 133), pygame.Rect(0, 133, 133, 133), pygame.Rect(0, 266, 133, 133),
             pygame.Rect(133, 0, 133, 133), pygame.Rect(266, 0, 133, 133), pygame.Rect(133, 266, 133, 133),
             pygame.Rect(266, 133, 133, 133), pygame.Rect(266, 266, 133, 133), pygame.Rect(133, 133, 133, 133)]

    pygame.draw.line(screen, "white", (133, 0), (133, 399), 5)
    pygame.draw.line(screen, "white", (266, 0), (266, 399), 5)
    pygame.draw.line(screen, "white", (0, 133), (399, 133), 5)
    pygame.draw.line(screen, "white", (0, 266), (399, 266), 5)

    for circle_pos in clicked_circles:
        pygame.draw.circle(screen, (255, 255, 255), circle_pos, 50, 5)

    for cross_pos in computer_clicked_crosses:
        pygame.draw.line(screen, (255, 0, 0), (cross_pos[0] - 50, cross_pos[1] - 50), (cross_pos[0] + 50, cross_pos[1] + 50), 5)
        pygame.draw.line(screen, (255, 0, 0), (cross_pos[0] - 50, cross_pos[1] + 50), (cross_pos[0] + 50, cross_pos[1] - 50), 5)

    if player_turn and ispressed:
        for rect in rects:
            if rect.collidepoint(pygame.mouse.get_pos()) and rect.center not in clicked_circles and rect.center not in computer_clicked_crosses:
                clicked_circles.append(rect.center)
                player_turn = False
                ispressed = False
                player_turn_time = pygame.time.get_ticks()

                # Update the game board with player's move
                row, col = rect.center[1] // 133, rect.center[0] // 133
                board[row][col] = 'O'

    if not player_turn and pygame.time.get_ticks() - player_turn_time > 1000:
        available_rects = [rect for rect in rects if rect.center not in clicked_circles and rect.center not in computer_clicked_crosses]
        if available_rects:
            chosen_rect = random.choice(available_rects)
            computer_clicked_crosses.append(chosen_rect.center)
            player_turn = True

            # Update the game board with computer's move
            row, col = chosen_rect.center[1] // 133, chosen_rect.center[0] // 133
            board[row][col] = 'X'

    winner = check_winner(board)
    if winner:
        print(winner)
        
        isrunning = False

    pygame.display.flip()

pygame.quit()
