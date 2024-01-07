import pygame
import random

pygame.init()

SCREEN_WIDTH = 399
SCREEN_HEIGHT = 399

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

i = 0
computer_turn = False
isrunning = True
ispressed = False

# List to store the positions of clicked circles
clicked_circles = []
# List to store the positions of computer's crosses
computer_clicked_crosses = []

while isrunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isrunning = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            ispressed = True
        if event.type == pygame.MOUSEBUTTONUP:
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

    # Draw the clicked circles
    for circle_pos in clicked_circles:
        pygame.draw.circle(screen, "white", circle_pos, 50, 5)
        # i = 0

    # Draw the computer's crosses
    for cross_pos in computer_clicked_crosses:
        pygame.draw.circle(screen, "red", cross_pos, 50, 5)

    # Draw the current circle if the mouse button is pressed
    if ispressed and not computer_turn:
        # i = 0
        for rect in rects:
            if rect.collidepoint(pygame.mouse.get_pos()) and rect.center not in computer_clicked_crosses:
                clicked_circles.append(rect.center)
                computer_turn = True

    # Computer's Turn
    if computer_turn:
        computer_turn = False   
        available_rects = [rect for rect in rects if rect.center not in clicked_circles and rect.center not in computer_clicked_crosses]
        if available_rects and i < 1:
            chosen_rect = random.choice(available_rects)
            computer_clicked_crosses.append(chosen_rect.center)
            i += 1
            
    print(computer_clicked_crosses)

    pygame.display.flip()

pygame.quit()
