# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
vetor = [None, None]
aux = 0

# Map
mapaImg = pygame.image.load('./assets/map.png')
mapX = 400
mapY = 200

def map():
    screen.blit(mapaImg, (mapX, mapY))

class Button():
    def __init__(self, pos, node):
        self.x, self.y = pos
        self.node = node
        self.surface = pygame.Surface((15, 14))
        self.surface.fill("black")
        self.rect = pygame.Rect(self.x, self.y, 15, 14)


    def knowNode(self, node):
        self.surface = pygame.Surface((15, 14))
        self.surface.fill("black")
        self.rect = pygame.Rect(self.x, self.y, 15, 14)
        if vetor[0] == None:
            vetor[0] = node
        elif vetor[0] != None and vetor[1] == None:
            vetor[1] = node
        else:
            print(vetor[0], vetor[1])
    
    def draw(self):
        #Draw Button
        screen.blit(button1.surface, (self.x, self.y))

    def click(self, event):
        x,y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    self.knowNode(self.node)

button1 = Button(
    (50, 50),
    "AM"
    )

button2 = Button(
    (150, 150),
    "MA"
    )


while running:
    
    screen.fill("white")
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            print(mouse_pos)
        button1.click(event)
        button2.click(event)
    button1.draw()
    button2.draw()


    # RENDER YOUR GAME HERE
    map()

    # flip() the display to put your work on screen
    pygame.display.update()
    #pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()