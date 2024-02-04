import pygame
import random

class Button:
    def __init__(self, surface, x, y, image, size_x, size_y):
        self.image = pygame.transform.scale(image, (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.surface = surface

    def draw(self):
        action = False

        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                action = True
                self.clicked = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        self.surface.blit(self.image, (self.rect.x, self.rect.y))

        return action

class TicTacToe:
    def __init__(self):
        pygame.init()
        self.SCREEN_WIDTH = 399
        self.SCREEN_HEIGHT = 399
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.restart_img = pygame.image.load('C:\MASTER FOLDER\Python-Projects\Tic-Tac-Toe\images\RESTART.png').convert_alpha()
        self.win_img = pygame.image.load('C:\MASTER FOLDER\Python-Projects\Tic-Tac-Toe\images\WIN.png').convert_alpha()
        self.lose_img = pygame.image.load('C:\MASTER FOLDER\Python-Projects\Tic-Tac-Toe\images\LOSE.png').convert_alpha()
        self.draw_img = pygame.image.load('C:\MASTER FOLDER\Python-Projects\Tic-Tac-Toe\images\DRAW.png').convert_alpha()
        self.player_turn = True
        self.isrunning = True
        self.ispressed = False
        self.clicked_circles = []
        self.computer_clicked_crosses = []
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.restart_button = Button(self.screen, self.SCREEN_WIDTH / 2 - 60, self.SCREEN_HEIGHT / 2 + 50, self.restart_img, 120, 30)
        self.player_turn_time = 0

        self.win_screen = Button(self.screen, self.SCREEN_WIDTH / 2 - 150, self.SCREEN_HEIGHT / 2 - 100, self.win_img, 300, 100)
        self.lose_screen = Button(self.screen, self.SCREEN_WIDTH / 2 - 150, self.SCREEN_HEIGHT / 2 - 100, self.lose_img, 300, 100)
        self.draw_screen = Button(self.screen, self.SCREEN_WIDTH / 2 - 175, self.SCREEN_HEIGHT / 2 - 100, self.draw_img, 350, 100)

    def check_winner(self):
        for i in range(3):
            if all(self.board[i][j] == 'O' for j in range(3)) or all(self.board[j][i] == 'O' for j in range(3)):
                return "Player wins!"
            elif all(self.board[i][j] == 'X' for j in range(3)) or all(self.board[j][i] == 'X' for j in range(3)):
                return "Computer wins!"

        if self.board[0][0] == self.board[1][1] == self.board[2][2] == 'O' or self.board[0][2] == self.board[1][1] == self.board[2][0] == 'O':
            return "Player wins!"
        elif self.board[0][0] == self.board[1][1] == self.board[2][2] == 'X' or self.board[0][2] == self.board[1][1] == self.board[2][0] == 'X':
            return "Computer wins!"

        return None
    
    def check_draw(self):
        # Check if all positions are filled and there is no winner
        if all(self.board[i][j] != '' for i in range(3) for j in range(3)) and self.check_winner() == None:
            return "It's a draw!"
        else:
            return None

    def game_over(self):
        winner = self.check_winner()
        draw = self.check_draw()

        if winner:
            pygame.draw.rect(self.screen, "black", (0, 0, self.SCREEN_HEIGHT, self.SCREEN_WIDTH))
            # Display game over image
            if winner == "Player wins!":
                self.win_screen.draw()
            elif winner == "Computer wins!":
                self.lose_screen.draw()
                # Display restart button
            if self.restart_button.draw():
                # Clear game state for a new game
                self.clicked_circles = []
                self.computer_clicked_crosses = []
                self.board = [['' for _ in range(3)] for _ in range(3)]
                self.player_turn = True
                self.ispressed = False
                self.player_turn_time = 0
    
        elif draw == "It's a draw!":
            pygame.draw.rect(self.screen, "black", (0, 0, self.SCREEN_HEIGHT, self.SCREEN_WIDTH))
            self.draw_screen.draw()

            # Display restart button
            if self.restart_button.draw():
                # Clear game state for a new game
                self.clicked_circles = []
                self.computer_clicked_crosses = []
                self.board = [['' for _ in range(3)] for _ in range(3)]
                self.player_turn = True
                self.ispressed = False
                self.player_turn_time = 0

    def run(self):
        while self.isrunning:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.isrunning = False
                if event.type == pygame.MOUSEBUTTONDOWN and self.player_turn:
                    self.ispressed = True
                if event.type == pygame.MOUSEBUTTONUP and self.player_turn:
                    self.ispressed = False
                    self.player_turn_time = pygame.time.get_ticks()

            self.screen.fill("black")

            rects = [pygame.Rect(0, 0, 133, 133), pygame.Rect(0, 133, 133, 133), pygame.Rect(0, 266, 133, 133),
                     pygame.Rect(133, 0, 133, 133), pygame.Rect(266, 0, 133, 133), pygame.Rect(133, 266, 133, 133),
                     pygame.Rect(266, 133, 133, 133), pygame.Rect(266, 266, 133, 133), pygame.Rect(133, 133, 133, 133)]

            pygame.draw.line(self.screen, "white", (133, 0), (133, 399), 5)
            pygame.draw.line(self.screen, "white", (266, 0), (266, 399), 5)
            pygame.draw.line(self.screen, "white", (0, 133), (399, 133), 5)
            pygame.draw.line(self.screen, "white", (0, 266), (399, 266), 5)

            for circle_pos in self.clicked_circles:
                pygame.draw.circle(self.screen, (255, 255, 255), circle_pos, 50, 5)

            for cross_pos in self.computer_clicked_crosses:
                pygame.draw.line(self.screen, (255, 0, 0), (cross_pos[0] - 50, cross_pos[1] - 50),
                                 (cross_pos[0] + 50, cross_pos[1] + 50), 5)
                pygame.draw.line(self.screen, (255, 0, 0), (cross_pos[0] - 50, cross_pos[1] + 50),
                                 (cross_pos[0] + 50, cross_pos[1] - 50), 5)

            if self.player_turn and self.ispressed:
                for rect in rects:
                    if rect.collidepoint(pygame.mouse.get_pos()) and rect.center not in self.clicked_circles and rect.center not in self.computer_clicked_crosses:
                        self.clicked_circles.append(rect.center)
                        self.player_turn = False
                        self.ispressed = False
                        self.player_turn_time = pygame.time.get_ticks()

                        row, col = rect.center[1] // 133, rect.center[0] // 133
                        self.board[row][col] = 'O'

            if not self.player_turn and pygame.time.get_ticks() - self.player_turn_time > 1000:
                available_rects = [rect for rect in rects if rect.center not in self.clicked_circles and rect.center not in self.computer_clicked_crosses]
                if available_rects:
                    chosen_rect = random.choice(available_rects)
                    self.computer_clicked_crosses.append(chosen_rect.center)
                    self.player_turn = True

                    row, col = chosen_rect.center[1] // 133, chosen_rect.center[0] // 133
                    self.board[row][col] = 'X'

            self.game_over()

            pygame.display.flip()

        pygame.quit()


if __name__ == "__main__":
    game = TicTacToe()
    game.run()