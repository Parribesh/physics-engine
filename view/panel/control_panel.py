from config import settings
import pygame
import typing
from dataclasses import dataclass, field

@dataclass  
class Payload:
    header: str
    width: int
    height: int = settings.CONTROL_PANEL_HEIGHT
    data: list[str] = field(default_factory=list)
    x: int = 0
    y: int = 0

    @property
    def header_rect(self) -> pygame.Rect:
        return pygame.Rect(self.x, self.y, self.width, self.height * 0.1)
    @property
    def data_rect(self) -> pygame.Rect:
        return pygame.Rect(self.x, self.y + self.height * 0.2, self.width, self.height * 0.9)
    @property
    def header_font(self) -> pygame.font.Font:
        return pygame.font.Font(None, 32)
    @property
    def data_font(self) -> pygame.font.Font:
        return pygame.font.Font(None, 32)
    @property
    def header_color(self) -> tuple[int, int, int]:
        return (0, 0, 0)
    @property
    def data_color(self) -> tuple[int, int, int]:
        return (0, 0, 0)
    @property
    def header_background_color(self) -> tuple[int, int, int]:
        return (255, 255, 255)
    @property
    def data_background_color(self) -> tuple[int, int, int]:
        return (255, 255, 255)
    @property
    def header_background_color_rgba(self) -> tuple[int, int, int, int]:
        return (255, 255, 255, 255)
    @property
    def data_background_color_rgba(self) -> tuple[int, int, int, int]:
        return (255, 255, 255, 255)

from view.view import View
class ControlPanel(View):                                                                                                                                                               
    def __init__(self, screen: pygame.Surface):
        pygame.init()
        self.payloads = list[Payload]()
        self.control_panel = {}
        self.control_panel["surface"] = pygame.Surface((settings.CONTROL_PANEL_WIDTH, settings.CONTROL_PANEL_HEIGHT))
        self.control_panel["rect"] = self.control_panel["surface"].get_rect()
        self.control_panel["rect"].topleft = (0, 0)
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.running = True
        self.font = pygame.font.Font(None, 32)
        self.add_default_payload()

    def draw(self, screen: pygame.Surface):
        # Fill the entire control panel surface once with background color
        self.control_panel["surface"].fill((255, 255, 255))
        
        current_payload_x = 0
        for payload in self.payloads:
            payload.x = current_payload_x
            current_payload_x += payload.width   
            payload.y = 0
            
            # Draw header background rectangle for this payload only
            header_rect = payload.header_rect
            pygame.draw.rect(self.control_panel["surface"], payload.header_background_color_rgba, header_rect)
            text = payload.header_font.render(payload.header, True, payload.header_color)
            self.control_panel["surface"].blit(text, header_rect)
            
            # Draw data background rectangle for this payload only
            data_rect = payload.data_rect
            pygame.draw.rect(self.control_panel["surface"], payload.data_background_color_rgba, data_rect)
            
            # Calculate starting y position for data (below header)
            data_start_y = payload.y + payload.height * 0.2
            font_height = payload.data_font.get_height()
            # Render each data item with proper vertical spacing
            for index, data in enumerate(payload.data):
                data_y = data_start_y + (index * font_height)
                text_rect = pygame.Rect(payload.x, data_y, payload.width, font_height)
                text = payload.data_font.render(data, True, payload.data_color)
                self.control_panel["surface"].blit(text, text_rect)
        
        # Blit the entire control panel surface to screen once after all payloads are drawn
        screen.blit(self.control_panel["surface"], self.control_panel["rect"])
        pygame.display.flip()

    def handle_event(self, event: pygame.event.Event) -> bool:
        if event.type == pygame.QUIT:
            return False
        return True
    def get_screen(self) -> pygame.Surface:
        return self.screen
    def add_default_payload(self):
        payload = Payload(
            width=100,
            header="Control Panel",
            data=["Data 1", "Data 2", "Data 3"],
        )
        self.payloads.append(payload)


    def get_payloads(self) -> list[Payload]:
        return self.payloads

    def add_payload(self, header: str,width: int, data: list[str]):
        payload = Payload(
            header=header,
            width=width,
            data=data,
        )
        self.payloads.append(payload)

    def remove_payload(self, index: int):
        self.payloads.pop(index)

    def get_payload(self, index: int) -> Payload:
        return self.payloads[index]

    def get_payloads(self) -> list[Payload]:
        return self.payloads
    
    def get_screen(self) -> pygame.Surface:
        return self.screen