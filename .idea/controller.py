import pygame

class SnakeGameController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def process_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.model.change_direction('UP')
            elif event.key == pygame.K_DOWN:
                self.model.change_direction('DOWN')
            elif event.key == pygame.K_LEFT:
                self.model.change_direction('LEFT')
            elif event.key == pygame.K_RIGHT:
                self.model.change_direction('RIGHT')

    def update(self):
        self.model.move_snake()
        self.model.update_snake()
        if (self.model.snake_pos[0] < 0 or self.model.snake_pos[0] > self.model.frame_size_x - 10 or
                self.model.snake_pos[1] < 0 or self.model.snake_pos[1] > self.model.frame_size_y - 10):
            return False
        for block in self.model.snake_body[1:]:
            if self.model.snake_pos == block:
                return False
        return True
