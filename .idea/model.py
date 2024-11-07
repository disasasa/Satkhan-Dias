import random
import copy

class SnakeGameModel:
    def __init__(self, frame_size_x, frame_size_y):
        self.frame_size_x = frame_size_x
        self.frame_size_y = frame_size_y
        self.snake_pos = [100, 50]
        self.snake_body = [[100, 50], [90, 50], [80, 50]]
        self.food_pos = [random.randrange(1, (self.frame_size_x // 10)) * 10,
                         random.randrange(1, (self.frame_size_y // 10)) * 10]

        self.food_spawn = True
        self.direction = 'RIGHT'
        self.score = 0
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update()

    def change_direction(self, direction):
        if direction == 'UP' and self.direction != 'DOWN':
            self.direction = 'UP'
        elif direction == 'DOWN' and self.direction != 'UP':
            self.direction = 'DOWN'
        elif direction == 'LEFT' and self.direction != 'RIGHT':
            self.direction = 'LEFT'
        elif direction == 'RIGHT' and self.direction != 'LEFT':
            self.direction = 'RIGHT'

    def move_snake(self):
        if self.direction == 'UP':
            self.snake_pos[1] -= 10
        if self.direction == 'DOWN':
            self.snake_pos[1] += 10
        if self.direction == 'LEFT':
            self.snake_pos[0] -= 10
        if self.direction == 'RIGHT':
            self.snake_pos[0] += 10

    def update_snake(self):
        self.snake_body.insert(0, list(self.snake_pos))

        if self.snake_pos == self.food_pos:
            self.score += 1
            self.food_spawn = False
        else:
            self.snake_body.pop()
        if not self.food_spawn:
            self.food_pos = [random.randrange(1, (self.frame_size_x // 10)) * 10,
                             random.randrange(1, (self.frame_size_y // 10)) * 10]

        self.food_spawn = True
        self.notify_observers()

    def reset_game(self):
        self.snake_pos = [100, 50]
        self.snake_body = [[100, 50], [90, 50], [80, 50]]
        self.food_pos = [random.randrange(1, (self.frame_size_x // 10)) * 10, random.randrange(1, (self.frame_size_y // 10)) * 10]
        self.food_spawn = True
        self.direction = 'RIGHT'
        self.score = 0
