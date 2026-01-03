import pygame

class View:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen

    def handle_event(self, event: pygame.event.Event) -> bool:
        return True
    def draw(self, screen: pygame.Surface) -> None:
        pass
    def get_screen(self) -> pygame.Surface:
        return self.screen