import sys
import pygame

class SnakeGameView:
    def __init__(self, game_window):
        self.game_window = game_window

    def draw(self, model):
        self.game_window.fill((0, 0, 0))

        grid_color = (50, 50, 50)
        grid_size = 10

        for x in range(0, model.frame_size_x, grid_size):
            pygame.draw.line(self.game_window, grid_color, (x, 0), (x, model.frame_size_y))

        for y in range(0, model.frame_size_y, grid_size):
            pygame.draw.line(self.game_window, grid_color, (0, y), (model.frame_size_x, y))

        for pos in model.snake_body:
            pygame.draw.rect(self.game_window, (0, 255, 0),
                             pygame.Rect(pos[0], pos[1], grid_size, grid_size))

        pygame.draw.rect(self.game_window, (255, 255, 255),
                         pygame.Rect(model.food_pos[0], model.food_pos[1], grid_size, grid_size))

        self.show_score(model)

    def show_score(self, model):
        font = pygame.font.SysFont('times new roman', 20)
        score_surface = font.render(f'Score: {model.score}', True, (255, 255, 255))
        self.game_window.blit(score_surface, (10, 10))

    def game_over(self):
        font = pygame.font.SysFont('times new roman', 90)
        game_over_surface = font.render('Game Over', True, (255, 0, 0))
        self.game_window.blit(game_over_surface, (
            self.game_window.get_width() // 2 - game_over_surface.get_width() // 2, self.game_window.get_height() // 4))

        restart_font = pygame.font.SysFont('times new roman', 30)
        restart_surface = restart_font.render('Press "R" to Restart or "Q" to Quit', True, (255, 255, 255))
        self.game_window.blit(restart_surface, (
            self.game_window.get_width() // 2 - restart_surface.get_width() // 2, self.game_window.get_height() // 2))

        pygame.display.flip()
        waiting_for_input = True
        while waiting_for_input:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        waiting_for_input = False
                        return True
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()
        return False
