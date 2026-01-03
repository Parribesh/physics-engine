import numpy as np
import pygame
WINDOW_WIDTH , GRID_WIDTH = 1000, 100
WINDOW_HEIGHT , GRID_HEIGHT = 1000, 100
CELL_SIZE = 10
grid = None
def main_grid():
    global grid
    grid = np.zeros((GRID_WIDTH, GRID_HEIGHT))
    for i in range(GRID_WIDTH):
        for j in range(GRID_HEIGHT):
            grid[i, j] = np.random.randint(0, 2)
    return grid

def draw_grid(screen: pygame.Surface):
    global grid
    if grid is None:
        main_grid()
        return
    for i in range(GRID_WIDTH):
        for j in range(GRID_HEIGHT):
            pygame.draw.rect(screen, (0, 155, 255), (i * CELL_SIZE, j * CELL_SIZE, CELL_SIZE, CELL_SIZE), 0)

def fps_monitor(screen: pygame.Surface, fps: int):
    font = pygame.font.Font(None, 32)
    text = font.render(f"FPS: {fps}", True, (255, 255, 255))
    text_rect = text.get_rect()
    text_rect.topright = (10, 10)
    screen.blit(text, text_rect)

def refresh_grid(screen: pygame.Surface):
    global grid
    if grid is None:
        main_grid()
        return
    for i in range(GRID_WIDTH):
        for j in range(GRID_HEIGHT):
            pygame.draw.rect(screen, (0, 0, 0), (i * CELL_SIZE, j * CELL_SIZE, CELL_SIZE, CELL_SIZE), 0)

def draw_sine_wave(screen: pygame.Surface, frame_count: int):
    amplitude = 100 
    frequency = 0.01 
    offset = WINDOW_HEIGHT / 2
    # Use frame_count to animate the wave over time
    # This allows smooth animation without blocking the game loop
    for i in range(WINDOW_WIDTH):
        # Add frame_count to create animation effect
        phase = (i + frame_count * 2) % WINDOW_HEIGHT
        y = amplitude * np.sin(2 * np.pi * frequency * phase) + offset
        pygame.draw.circle(screen, (255, 255, 255), (i, int(y)), 1)
        

def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    main_grid()
    running = True
    clock = pygame.time.Clock()
    frame_count = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        screen.fill((0, 0, 0))
        draw_sine_wave(screen, frame_count)
        fps_monitor(screen, clock.get_fps())
        pygame.display.flip()
        refresh_grid(screen)
        clock.tick(60)
        frame_count += 1
    pygame.quit()

if __name__ == "__main__":
    main()