import pygame
from model import SnakeGameModel
from view import SnakeGameView
from controller import SnakeGameController
from patterns import Singleton,Observer,Command,SnakePrototype,GameFacade,SnakeAdapter

def main():
    pygame.init()
    frame_size_x, frame_size_y = 1080, 720
    screen = pygame.display.set_mode((frame_size_x, frame_size_y))
    pygame.display.set_caption('Snake Game')

    running = True
    while running:
        model = SnakeGameModel(frame_size_x, frame_size_y)
        view = SnakeGameView(screen)
        controller = SnakeGameController(model, view)

        game_running = True
        while game_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    game_running = False
                controller.process_events(event)
            if not controller.update():
                if not view.game_over():
                    game_running = False
                else:
                    break
            view.draw(model)
            pygame.display.update()
            pygame.time.Clock().tick(25)

    pygame.quit()

if __name__ == '__main__':
    main()
