import pygame, math

#calucation of angle with respect to midpoint and mouse co-ordinates.
def getAngle(x1, y1, x2, y2):
    angle = math.atan2(x1 - x2, y1 - y2) # get the angle in radians
    angle = angle * (180 / math.pi) # convert to degrees
    angle = (angle + 90) % 360# adjusting for 90 degree difference.
    return angle

#color definition //
#in (R,G,B) format
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

#pygame window initialization
pygame.init()
bg_color = white
window_width = 640 # width in pixels
window_height = 480 # height in pixels
windows_resolution = (window_width,window_height)
window_x_center = int(window_width / 2)
window_y_center = int(window_height / 2)
frameRate = 60 #fps
gameClock = pygame.time.Clock()
display_surface = pygame.display.set_mode(windows_resolution)
pygame.display.set_caption('Elliptical Orbit')


#GameLOOP
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == K_ESCAPE):
            pygame.quit()
            exit()

    #Rendering
    display_surface.fill(bg_color)
    mousex, mousey = pygame.mouse.get_pos()
    degrees = getAngle(window_x_center, window_y_center, mousex, mousey)
    pygame.draw.circle(display_surface, green, (window_x_center, window_y_center), 100, 4)
    pygame.draw.circle(display_surface, blue, (window_x_center, window_y_center), 20, 0)
    xPos = math.cos(degrees * (math.pi / 180)) * 100
    yPos = math.sin(degrees * (math.pi / 180)) * 100
    pygame.draw.circle(display_surface, red, (int(xPos) + window_x_center, -1 * int(yPos) + window_y_center), 40)
    pygame.display.update()
    gameClock.tick(frameRate)