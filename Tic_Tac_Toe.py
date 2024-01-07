import pygame
import random

pygame.init()

SCREEN_WIDTH = 399
SCREEN_HEIGHT = 399

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

isrunning = True

ispressed = False

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

    for rect in rects:
        if ispressed:
            if rect.collidepoint(pygame.mouse.get_pos()):
                center = rect.center
                pygame.draw.circle(screen, "white", center, 50, 5)

    pygame.display.flip()

pygame.quit()
