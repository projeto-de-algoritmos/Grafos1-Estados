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
        self.surface = pygame.Surface((18, 14))
        self.surface.fill("black")
        self.surface.set_alpha(0)
        self.rect = pygame.Rect(self.x, self.y, 18, 14)


    def knowNode(self, node):
        self.surface = pygame.Surface((18, 14))
        self.rect = pygame.Rect(self.x, self.y, 18, 14)
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
    (425, 364),
    "AC"
    )

button2 = Button(
    (851, 380),
    "AL"
    )

button3 = Button(
    (503, 305),
    "AM"
    )

button4 = Button(
    (650, 242),
    "AP"
    )

button5 = Button(
    (766, 402),
    "BA"
    )

button6 = Button(
    (796, 322),
    "CE"
    )

button7 = Button(
    (681, 435),
    "DF"
    )

button8 = Button(
    (793, 498),
    "ES"
    )

button9 = Button(
    (673, 450),
    "GO"
    )

button10 = Button(
    (732, 316),
    "MA"
    )

button11 = Button(
    (609, 409),
    "MT"
    )

button12 = Button(
    (617, 493),
    "MS"
    )

button13 = Button(
    (735, 472),
    "MG"
    )

button14 = Button(
    (635, 314),
    "PA"
    )

button15 = Button(
    (864, 347),
    "PB"
    )

button16 = Button(
    (652, 542),
    "PR"
    )

button17 = Button(
    (862, 361),
    "PE"
    )

button18 = Button(
    (762, 350),
    "PI"
    )

button19 = Button(
    (768, 535),
    "RJ"
    )

button20 = Button(
    (859, 326),
    "RN"
    )

button21 = Button(
    (633, 602),
    "RS"
    )

button22 = Button(
    (520, 384),
    "RO"
    )

button23 = Button(
    (541, 237),
    "RR"
    )

button24 = Button(
    (668, 573),
    "SC"
    )

button25 = Button(
    (682, 515),
    "SP"
    )

button26 = Button(
    (835, 397),
    "SE"
    )

button27 = Button(
    (691, 382),
    "TO"
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
        button3.click(event)
        button4.click(event)
        button5.click(event)
        button6.click(event)
        button7.click(event)
        button8.click(event)
        button9.click(event)
        button10.click(event)
        button11.click(event)
        button12.click(event)
        button13.click(event)
        button14.click(event)
        button15.click(event)
        button16.click(event)
        button17.click(event)
        button18.click(event)
        button19.click(event)
        button20.click(event)
        button21.click(event)
        button22.click(event)
        button23.click(event)
        button24.click(event)
        button25.click(event)
        button26.click(event)
        button27.click(event)
    button1.draw()
    button2.draw()
    button3.draw()
    button4.draw()
    button5.draw()
    button6.draw()
    button7.draw()
    button8.draw()
    button9.draw()
    button10.draw()
    button11.draw()
    button12.draw()
    button13.draw()
    button14.draw()
    button15.draw()
    button16.draw()
    button17.draw()
    button18.draw()
    button19.draw()
    button20.draw()
    button21.draw()
    button22.draw()
    button23.draw()
    button24.draw()
    button25.draw()
    button26.draw()
    button27.draw()


    # RENDER YOUR GAME HERE
    map()

    # flip() the display to put your work on screen
    pygame.display.update()
    #pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()