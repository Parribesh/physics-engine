from dataclasses import dataclass
import pygame
from view.view import View
from config import settings


class Cell:
    def __init__(self, i: int, j: int, width: int = 10, height: int = 10, color: tuple[int, int, int] = (255, 255, 255)):
        self.i = i
        self.j = j
        self.width = width
        self.height = height
        self.color = color

    def draw(self, screen: pygame.Surface):
        pygame.draw.rect(screen, self.color, (self.i * self.width, settings.CONTROL_PANEL_HEIGHT + self.j * self.height, self.width, self.height))
        pygame.draw.rect(screen, (0, 0, 0), (self.i * self.width, settings.CONTROL_PANEL_HEIGHT + self.j * self.height, self.width, self.height), 1)

class Grid(View):
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.cell_size = 100
        self.cell_count = self.screen.get_width() // self.cell_size
        self.cell_count_y = self.screen.get_height() // self.cell_size
        self.cells: list[list[Cell]] = [[Cell(i, j, self.cell_size, self.cell_size) for j in range(self.cell_count_y)] for i in range(self.cell_count)]
        

    def get_cell(self, x: int, y: int) -> Cell:
        return self.cells[x][y]

    def add_cell(self, cell: Cell):
        self.cells[cell.i][cell.j] = cell

    def remove_cell(self, cell: Cell):
        self.cells[cell.i][cell.j] = None

    def handle_event(self, event: pygame.event.Event) -> bool:
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            cell_x = x // self.cell_size
            cell_y = (y - settings.CONTROL_PANEL_HEIGHT) // self.cell_size
            if cell_x < self.cell_count and cell_y < self.cell_count_y:
                self.cells[cell_x][cell_y].color = (255, 0, 0)
                return True
        return True

    def draw(self, screen: pygame.Surface):
        for i in range(self.cell_count):
            for j in range(self.cell_count_y):
                cell_data = self.cells[i][j]
                cell_data.draw(screen)
    def get_screen(self) -> pygame.Surface:
        return self.screen
