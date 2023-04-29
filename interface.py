# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

# Map
mapaImg = pygame.image.load('./assets/map.png')
mapX = 400
mapY = 200

def map():
    screen.blit(mapaImg, (mapX, mapY))

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_rel()
            print(mouse_pos)

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")


    # RENDER YOUR GAME HERE
    map()
    pygame.display.update()

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()