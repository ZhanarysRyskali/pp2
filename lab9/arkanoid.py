import pygame
import sys
from random import randrange

# Initialization
pygame.init()

# Setting up the main appearance
W = 1200
H = 800
sc = pygame.display.set_mode((W, H))
bg = pygame.image.load('1.jpg').convert()

# Setting up the fps
fps = 60
clock = pygame.time.Clock()

# Paddle settings
paddle_w = 330
paddle_h = 35
paddle_speed = 15
paddle = pygame.Rect(W//2 - paddle_w//2, H - paddle_h - 20, paddle_w, paddle_h)

# Ball settings
ball_radius = 20
ball_speed = 6
ball_rect = int(ball_radius*2**0.5)
ball = pygame.Rect(randrange(ball_rect, W - ball_rect), H//2, ball_rect, ball_rect)
dx, dy = 1, -1

# Block settings
block_list = [pygame.Rect(10 + 120 * i, 10 + 70 * j, 100, 50) for i in range(10) for j in range(4)]
color_list = [(randrange(30, 256), randrange(30,256), randrange(30,256)) for i in range(10) for j in range(4)]

# Collision function
def col(dx, dy, ball, rect):
    if(dx>0):
        delta_x = ball.right - rect.left
    else:
        delta_x = rect.right - ball.left
    if(dy>0):
        delta_y = ball.bottom - rect.top
    else:
        delta_y = rect.bottom-ball.top
    if(abs(delta_x-delta_y) < 10):
        dx,dy = -dx, -dy
    elif (delta_x > delta_y):
        dy = -dy
    elif(delta_y>delta_x):
        dx = -dx
    return dx, dy

# Appearance of pause menu
def draw_pause():
    # Create a surface for the pause menu
    surface = pygame.Surface((W, H), pygame.SRCALPHA)
    surface.fill((128, 128, 128, 150))  # Fill with semi-transparent gray color

    # Draw buttons with (0,0,0) frameworks
    button_font = pygame.font.Font(None, 36)  # Define font for buttons
    continue_button = button_font.render("Continue", True, (0, 0, 0))  # Render "Continue" button
    settings_button = button_font.render("Settings", True, (0, 0, 0))  # Render "Settings" button
    exit_button = button_font.render("Exit", True, (0, 0, 0))  # Render "Exit" button

    # Position buttons on the surface
    continue_button_rect = continue_button.get_rect(center=(W // 2, H // 2 - 50))
    settings_button_rect = settings_button.get_rect(center=(W // 2, H // 2))  # Assign to settings_button_rect
    exit_button_rect = exit_button.get_rect(center=(W // 2, H // 2 + 50))

    # Draw buttons on the surface with (0,0,0) frameworks
    pygame.draw.rect(surface, (0, 0, 0), continue_button_rect, 2)  # "Continue" button
    pygame.draw.rect(surface, (0, 0, 0), settings_button_rect, 2)  # "Settings" button
    pygame.draw.rect(surface, (0, 0, 0), exit_button_rect, 2)  # "Exit" button

    # Blit the surface onto the screen
    sc.blit(surface, (0, 0))

    # Blit buttons onto the screen
    sc.blit(continue_button, continue_button_rect.topleft)
    sc.blit(settings_button, settings_button_rect.topleft)
    sc.blit(exit_button, exit_button_rect.topleft)
    
    # Return button rectangles
    return continue_button_rect, settings_button_rect, exit_button_rect

def draw_settings():
    surface2 = pygame.Surface((W, H), pygame.SRCALPHA)
    surface2.fill((128, 128, 128, 150))  # Fill with semi-transparent gray color

    # Draw buttons with (0,0,0) frameworks
    button_font = pygame.font.Font(None, 36)  # Define font for buttons
    easy_button = button_font.render("Easy", True, (0, 0, 0))  # Render "Easy" button
    hard_button = button_font.render("Hard", True, (0, 0, 0))  # Render "Hard" button
    easy_button_rect = easy_button.get_rect(center=(W // 2, H // 2 - 50))
    hard_button_rect = hard_button.get_rect(center=(W // 2, H // 2 + 50))
    pygame.draw.rect(surface2, (0, 0, 0), easy_button_rect, 2)  # "Easy" button
    pygame.draw.rect(surface2, (0, 0, 0), hard_button_rect, 2) #"Hard" button
    sc.blit(surface2, (0, 0))

    sc.blit(easy_button, easy_button_rect.topleft)
    sc.blit(hard_button, hard_button_rect.topleft)
    return easy_button_rect, hard_button_rect
# Main loop
run = True
# Pause variable
pause = False
# Increasing speed
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Define button rectangles
continue_button_rect = None
settings_button_rect = None
easy_button_rect = None
hard_button_rect = None
exit_button_rect = None
settings = False
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            sys.exit()
        if event.type == INC_SPEED: #increasing speed
            ball_speed += 0.1 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                #making base of the pause
                if pause:
                    pause = False
                else:
                    pause = True 
        # Check for button presses in pause menu
        if pause and event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if continue_button_rect.collidepoint(mouse_pos):
                pause = False
            elif settings_button_rect.collidepoint(mouse_pos):
                settings = True
                pause = False
            elif exit_button_rect.collidepoint(mouse_pos):
                # Handle exit button press
                sys.exit()
        elif settings and event.type == pygame.MOUSEBUTTONDOWN:  # Check for settings button presses
            mouse_pos = pygame.mouse.get_pos()
            if easy_button_rect.collidepoint(mouse_pos):
                settings = False
                ball_speed += 0.1 #easy mode
            elif hard_button_rect.collidepoint(mouse_pos):
                settings = False
                ball_speed += 0.5 #hard mode
            elif exit_button_rect.collidepoint(mouse_pos):
                # Handle exit button press
                sys.exit()

    # Drawing objects, adding background
    sc.blit(bg, (0,0))
    [pygame.draw.rect(sc, color_list[color], block) for color, block in enumerate(block_list)]
    pygame.draw.rect(sc, pygame.Color('Violet'), paddle)
    pygame.draw.circle(sc, pygame.Color('darkorange'), ball.center, ball_radius)

    # Ball movement
    # All of this code under this line won't work if the game is paused
    if not pause and not settings:
        ball.x += ball_speed*dx
        ball.y += ball_speed*dy
        # Collision screen sides
        if ball.centerx < ball_radius or ball.centerx > W-ball_radius:
            dx = -dx
        if ball.centery < ball_radius:
            dy = -dy
        # Collision with paddle
        if ball.colliderect(paddle) and dy > 0:
            dx,dy = col(dx, dy, ball, paddle)
        hit_index = ball.collidelist(block_list)
        if hit_index!=-1:
            hit_rect = block_list.pop(hit_index)
            hit_color = color_list.pop(hit_index)
            dx, dy = col(dx, dy, ball, hit_rect)
        # Controls
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and paddle.left>0:
            paddle.left -= paddle_speed
        if key[pygame.K_RIGHT] and paddle.right<W:
            paddle.right += paddle_speed
        if(ball.bottom>H):
            print("You Lose")
            sys.exit()
        elif(len(block_list) == 0):
            print("You Won!")
            sys.exit()
    if pause:
        # Assign button rectangles from draw_pause() function
        continue_button_rect, settings_button_rect, exit_button_rect = draw_pause()
    if settings:
        easy_button_rect, hard_button_rect = draw_settings()      
    pygame.display.update()
    clock.tick(fps)
