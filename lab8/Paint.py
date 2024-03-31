import pygame
import sys

# Initialize Pygame
pygame.init()

# Set screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Paint")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set default drawing settings
d_c = BLACK  # d_c stands for drawing_color
draw_mode = 'rectangle'
radius = 10
start_pos = None
screen.fill(WHITE)

# Main loop
while True:
    # Handle color selection
    keys = pygame.key.get_pressed()
    if keys[pygame.K_1]:
        d_c = BLACK
    elif keys[pygame.K_2]:
        d_c = RED
    elif keys[pygame.K_3]:
        d_c = GREEN
    elif keys[pygame.K_4]:
        d_c = BLUE
    
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.key == pygame.K_r:
                draw_mode = 'rectangle'
            elif event.key == pygame.K_c:
                draw_mode = 'circle'
            elif event.key == pygame.K_e:
                draw_mode = 'eraser'
                d_c = WHITE  # Set drawing color to white when eraser mode is selected
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if draw_mode == 'rectangle' or draw_mode == 'circle':
                start_pos = event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
            if start_pos:
                end_pos = event.pos
                if draw_mode == 'rectangle':
                    pygame.draw.rect(screen, d_c, (start_pos, (end_pos[0] - start_pos[0], end_pos[1] - start_pos[1])))
                elif draw_mode == 'circle':
                    radius = max(abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1])) // 2
                    pygame.draw.circle(screen, d_c, (start_pos[0] + radius, start_pos[1] + radius), radius)
        elif event.type == pygame.MOUSEMOTION:
            if draw_mode == 'eraser' and pygame.mouse.get_pressed()[0]:  # If left mouse button is pressed
                end_pos = event.pos
                pygame.draw.circle(screen, WHITE, end_pos, radius)  # Draw white circles as eraser

    # Update the screen
    pygame.display.flip()
    pygame.time.Clock().tick(60)
