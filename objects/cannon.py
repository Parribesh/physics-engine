from view.grid.grid import Cell
from config import settings
import pygame
from enum import Enum

class CannonState(Enum):
    IDLE = "idle"
    READY = "ready"
    FIRING = "firing"
    RELOADING = "reloading"

class Cannon(Cell):
    def __init__(self, i: int, j: int,width: int = 20, height: int = 20, color: tuple[int, int, int] = (255, 255, 255), angle: float = 0, velocity: float = 0, mass: float = 1, charge: float = 100):
        super().__init__(i, j, width, height, color)
        self.angle = angle
        self.velocity = velocity
        self.mass = mass
        self.charge = charge
        self.state = CannonState.IDLE

    def draw(self, screen: pygame.Surface):
        pygame.draw.rect(screen, self.color, (self.i * self.width, settings.CONTROL_PANEL_HEIGHT + self.j * self.height, self.width, self.height))
        pygame.draw.rect(screen, (0, 0, 0), (self.i * self.width, settings.CONTROL_PANEL_HEIGHT + self.j * self.height, self.width, self.height), 1)

    def update(self):
        self.charge -= 1
        if self.charge <= 0:
            self.state = CannonState.RELOADING
        if self.state == CannonState.FIRING:
            self.velocity = self.charge
            self.charge = 0
            self.state = CannonState.IDLE