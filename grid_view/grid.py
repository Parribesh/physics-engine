from dataclasses import dataclass
import pygame
from view.view import View
from config import settings


@dataclass
class Cell:
    x: int
    y: int
    width: int = 10
    height: int = 10
    color: tuple[int, int, int] = (255, 255, 255)
    border_color: tuple[int, int, int] = (0, 0, 255)
    border_width: int = 1
    border_radius: int = 0
    border_style: str = "solid"
    border_opacity: int = 255
    border_opacity_rgb: tuple[int, int, int] = (0, 0, 0)
    border_opacity_rgba: tuple[int, int, int, int] = (0, 0, 0, 255)

class Grid(View):
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.cell_size = 100
        self.cell_count = self.screen.get_width() // self.cell_size
        self.cell_count_y = self.screen.get_height() // self.cell_size
        self.cells_dict = [[Cell(i * self.cell_size, settings.CONTROL_PANEL_HEIGHT + j * self.cell_size, self.cell_size, self.cell_size) for j in range(self.cell_count_y)] for i in range(self.cell_count)]
        

    def handle_event(self, event: pygame.event.Event) -> bool:
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            cell_x = x // self.cell_size
            cell_y = (y - settings.CONTROL_PANEL_HEIGHT) // self.cell_size
            if cell_x < self.cell_count and cell_y < self.cell_count_y:
                self.cells_dict[cell_x][cell_y].color = (255, 0, 0)
                return True
        return True

    def draw(self, screen: pygame.Surface):
        for i in range(self.cell_count):
            for j in range(self.cell_count_y):
                cell_data = self.cells_dict[i][j]
                rect = pygame.Rect(cell_data.x, cell_data.y, cell_data.width, cell_data.height)
                pygame.draw.rect(screen, cell_data.color, rect)
                pygame.draw.rect(screen, cell_data.border_color, rect, cell_data.border_width, cell_data.border_radius)
    def get_screen(self) -> pygame.Surface:
        return self.screen
