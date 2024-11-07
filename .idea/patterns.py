import copy

class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

class Observer:
    def __init__(self, model):
        self.model = model
        self.model.add_observer(self)

    def update(self):
        print(f"Score updated: {self.model.score}")

class Command:
    def execute(self, model):
        pass

class MoveUpCommand(Command):
    def execute(self, model):
        model.snake_pos[1] -= 10

class SnakePrototype:
    def clone(self):
        return copy.deepcopy(self)

class GameFacade:
    def __init__(self, frame_size_x, frame_size_y):
        self.model = SnakeGameModel(frame_size_x, frame_size_y)
        self.view = SnakeGameView(self.model)
        self.controller = SnakeGameController(self.model, self.view)

    def start_game(self):
        self.model.reset_game()
        self.view.draw(self.model)
        self.controller.process_events(self.view)

class SnakeAdapter:
    def __init__(self, snake):
        self.snake = snake


    def get_snake_coordinates(self):
        return [(x, y) for x, y in self.snake.snake_body]
