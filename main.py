from config import settings
import pygame
from panel_view.control_panel import ControlPanel
from grid_view.grid import Grid
screen = pygame.display.set_mode((settings.GAME_WINDOW_WIDTH, settings.GAME_WINDOW_HEIGHT))
control_panel = ControlPanel(screen)
grid = Grid(screen)

class Game:
    def __init__(self):
        self.screen = screen
        self.control_panel = control_panel
        self.grid = grid
        self.running = True
        pygame.init()
        pygame.display.set_caption(settings.GAME_NAME)
        # pygame.display.set_icon(pygame.image.load(settings.GAME_ICON))
        pygame.display.set_mode((settings.GAME_WINDOW_WIDTH, settings.GAME_WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                self.grid.handle_event(event)
                self.control_panel.handle_event(event)
            self.screen.fill(settings.GAME_WINDOW_BACKGROUND_COLOR_RGB)
            self.control_panel.draw(self.screen)
            self.grid.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(settings.GAME_FPS)


if __name__ == "__main__":
    game = Game()
    game.run()