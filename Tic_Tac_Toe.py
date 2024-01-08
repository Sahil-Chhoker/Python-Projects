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
    # Add logic to check for a winner or a tie
    pass

while isrunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isrunning = False
        if event.type == pygame.MOUSEBUTTONDOWN and player_turn:
            ispressed = True
        if event.type == pygame.MOUSEBUTTONUP and player_turn:
            ispressed = False
    
    screen.fill("black")

    # Draw Logic Squares:
    rects = [pygame.Rect(0, 0, 133, 133), pygame.Rect(0, 133, 133, 133), pygame.Rect(0, 266, 133, 133),
             pygame.Rect(133, 0, 133, 133), pygame.Rect(266, 0, 133, 133), pygame.Rect(133, 266, 133, 133),
             pygame.Rect(266, 133, 133, 133), pygame.Rect(266, 266, 133, 133), pygame.Rect(133, 133, 133, 133)]

    # Display Grid:
    pygame.draw.line(screen, "white", (133, 0), (133, 399), 5)
    pygame.draw.line(screen, "white", (266, 0), (266, 399), 5)
    pygame.draw.line(screen, "white", (0, 133), (399, 133), 5)
    pygame.draw.line(screen, "white", (0, 266), (399, 266), 5)

    # Draw the clicked circles (player's moves)
    for circle_pos in clicked_circles:
        pygame.draw.circle(screen, "white", circle_pos, 50, 5)

    # Draw the computer's crosses
    for cross_pos in computer_clicked_crosses:
        pygame.draw.circle(screen, "red", cross_pos, 50, 5)

    # Player's Turn
    if player_turn and ispressed:
        for rect in rects:
            if rect.collidepoint(pygame.mouse.get_pos()) and rect.center not in clicked_circles and rect.center not in computer_clicked_crosses:
                clicked_circles.append(rect.center)
                player_turn = False
                ispressed = False

    # Computer's Turn
    if not player_turn:
        # Implement logic for the computer's move
        available_rects = [rect for rect in rects if rect.center not in clicked_circles and rect.center not in computer_clicked_crosses]
        if available_rects:
            chosen_rect = random.choice(available_rects)
            computer_clicked_crosses.append(chosen_rect.center)
            player_turn = True

    # Check for a winner or a tie
    check_winner()

    pygame.display.flip()

pygame.quit()
