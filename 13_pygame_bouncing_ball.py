import pygame

# color definition //
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)

# pygame window initilizion
bg_color = white
window_width = 800  # width in pixels
window_height = 600  # height in pixels
window_x_center = int(window_width / 2)
window_y_center = int(window_height / 2)
frameRate = 60  # FPS
pygame.init()
gameClock = pygame.time.Clock()
display_surface = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Bouncing ball')

# GameParameters
block_size = 40
speed_x = 8
speed_y = 8
position_x = window_width // 2
position_y = window_height // 2

# gameLOOP
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            exit()

    # Rendering
    display_surface.fill(bg_color)
    position_x = position_x + speed_x
    position_y = position_y + speed_y

    # boucing the ball

    if position_x + block_size >= window_width:  # right edge
        speed_x = -(speed_x)

    if position_x - block_size <= 0:  # left edge
        speed_x = -(speed_x)

    if position_y + block_size >= window_height:  # Bottom edge
        speed_y = -(speed_y)

    if position_y - block_size <= 0:  # Top edge
        speed_y = -(speed_y)

    pygame.draw.circle(display_surface, blue, (position_x, position_y), block_size)
    pygame.display.flip()
    gameClock.tick(frameRate)

