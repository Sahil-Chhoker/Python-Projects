import pygame
import random

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

def check_winner():
    if len(clicked_circles) < 3:
        return None
    all_moves = clicked_circles + computer_clicked_crosses

    # Check for player's win
    for line in [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]:
        symbols = [all_moves[i] if i < len(all_moves) else None for i in line]
        if all(symbol == (255, 255, 255) for symbol in symbols if symbol is not None):
            return "Player wins!"

    # Check for computer's win
    for line in [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]:
        symbols = [all_moves[i] if i < len(all_moves) else None for i in line]
        if all(symbol == (255, 0, 0) for symbol in symbols if symbol is not None):
            return "Computer wins!"

    if len(all_moves) == 9:
        return "It's a tie!"

    return None



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

    if not player_turn and pygame.time.get_ticks() - player_turn_time > 1000:
        available_rects = [rect for rect in rects if rect.center not in clicked_circles and rect.center not in computer_clicked_crosses]
        if available_rects:
            chosen_rect = random.choice(available_rects)
            computer_clicked_crosses.append(chosen_rect.center)
            player_turn = True

    # winner = check_winner()
    # if winner:
    #     print(winner)
    #     # isrunning = False

    pygame.display.flip()

pygame.quit()
