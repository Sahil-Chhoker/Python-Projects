import pygame
from pygame.font import Font
from pygame.time import Clock
import random 
import sys

class DodgySquare:
    def __init__(self):
        # Pygame
        pygame.init()
        pygame.mouse.set_visible(False)

        # Screen
        self.screen_width, self.screen_height = 600, 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Dodgy Square")

        # Colors
        self.WHITE: tuple = (255, 255, 255)
        self.BLACK: tuple = (0, 0, 0)
        self.RED: tuple = (255, 99, 71)
        self.GREEN: tuple = (0, 255, 0)
        self.BLUE: tuple = (65, 105, 255)

        # Font
        self.default: str = pygame.font.get_default_font()
        self.font: Font = pygame.font.Font(self.default, 26)

        # Player
        self.player_size: int = 30
        self.player_pos: list[int] = [0, 0]

        # Enemy
        self.enemy_size: float = 30
        self.enemy_pos: list[int] = []
        self.enemy_list = []
        self.enemy_speed: float = 3
        self.enemy_frequency: int = 20

        # Clock
        self.clock: Clock = pygame.time.Clock()

        # Game data
        self.game_over: bool = False
        self.score: int = 0
        self.frame_count: int = 0


    def create_enemy(self):
        enemy_pos: list[float] = [random.random() * (self.screen_width - self.enemy_size), -self.enemy_size]
        self.enemy_list.append(enemy_pos)

    def update_enemy_positions(self):
        if self.frame_count % self.enemy_frequency == 0:
            self.create_enemy()

        for id, enemy_pos in enumerate(self.enemy_list):
            if -self.enemy_size <= enemy_pos[1] < self.screen_height:
                enemy_pos[1] += self.enemy_speed
            else:
                self.enemy_list.pop(id)
                self.score += 1
                self.enemy_speed += 0.1

                if self.enemy_frequency > 10:
                    if self.score % 15 == 0:
                        self.enemy_frequency -= 2

    def detect_collision(self, player_pos: list[int], enemy_pos: list[int]):
        p_x, p_y = player_pos
        e_x, e_y = enemy_pos

        if (e_x <= p_x < e_x + self.enemy_size) or (p_x <= e_x < p_x + self.player_size):
            if (e_y <= p_y < e_y + self.enemy_size) or (p_y <= e_y < p_y + self.player_size):
                self.game_over = True
                return True

        return False

    def show_game_over(self):
        game_over_text = self.font.render("Game Over", True, self.RED)
        self.screen.blit(game_over_text, (self.screen_width // 2 - 70, self.screen_height // 2 - 50))

    def replay_game(self):
        self.enemy_list = []
        self.enemy_speed: float = 3
        self.enemy_frequency: int = 20
        self.game_over: bool = False
        self.frame_count: int = 0
        self.score: int = 0

    def draw_character(self, color: tuple, position: list[int], size: int):
        x, y = position
        pygame.draw.rect(self.screen, color, (x, y, size, size))

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if self.game_over and event.key == pygame.K_r:
                    self.replay_game()

            mouse_pos: tuple[int, int] = pygame.mouse.get_pos()

            self.player_pos = [mouse_pos[0] - self.player_size // 2, mouse_pos[1] - self.player_size // 2]

            # wall detection
            self.player_pos[0] = max(0, min(self.player_pos[0], self.screen_width - self.player_size))
            self.player_pos[1] = max(0, min(self.player_pos[1], self.screen_height - self.player_size))

            if not self.game_over:
                self.update_enemy_positions()

                for enemy_pos in self.enemy_list:
                    if self.detect_collision(self.player_pos, enemy_pos):
                        self.game_over = True
                        break

                self.screen.fill(self.BLACK)

                self.draw_character(self.BLUE, self.player_pos, self.player_size)

                for enemy in self.enemy_list:
                    if self.score > 100:
                        self.draw_character(self.GREEN, enemy, self.enemy_size)
                    else:
                        self.draw_character(self.RED, enemy, self.enemy_size)

                score_text = self.font.render("Score: " + str(self.score), True, self.WHITE)
                self.screen.blit(score_text, (10, 10))

                self.frame_count += 1
                if random.randint(-1, 1) + self.score % 10 == 0 and self.score > 0:
                    self.enemy_size += 0.1

            else:
                self.show_game_over()

            pygame.display.update()
            self.clock.tick(60)


if __name__ == "__main__":
    game = DodgySquare()
    game.run()
        





