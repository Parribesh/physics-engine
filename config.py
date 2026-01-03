from dotenv import load_dotenv
from pydantic_settings import BaseSettings
import os

load_dotenv()
class Settings(BaseSettings):
    GAME_NAME: str = "Physics Engine"
    GAME_FPS: int = 60
    GAME_DESCRIPTION: str = "Physics Engine"
    GAME_IMAGE: str = "assets/images/image.png"
    GAME_WINDOW_WIDTH: int = 1920
    GAME_WINDOW_HEIGHT: int = 1080
    GAME_WINDOW_FULLSCREEN: bool = False
    GAME_WINDOW_VSYNC: bool = True
    GAME_WINDOW_TITLE: str = "Civilization"
    GAME_WINDOW_ICON: str = "assets/images/icon.png"
    GAME_WINDOW_BACKGROUND_COLOR: str = "#000000"
    GAME_WINDOW_BACKGROUND_COLOR_RGB: tuple[int, int, int] = (0, 0, 0)
    GAME_WINDOW_BACKGROUND_COLOR_RGBA: tuple[int, int, int, int] = (0, 0, 0, 255)
    CONTROL_PANEL_WIDTH: int = GAME_WINDOW_WIDTH 
    CONTROL_PANEL_HEIGHT: int = GAME_WINDOW_HEIGHT * 0.1
    CONTROL_PANEL_BACKGROUND_COLOR: str = "#ffffff"
    CONTROL_PANEL_BACKGROUND_COLOR_RGB: tuple[int, int, int] = (255, 255, 255)
    CONTROL_PANEL_BACKGROUND_COLOR_RGBA: tuple[int, int, int, int] = (255, 255, 255, 255)

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()








