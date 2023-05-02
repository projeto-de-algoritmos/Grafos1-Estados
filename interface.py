import pygame
from bfs import *
from utils.generate_graph import generate_brasil_graph

# Recebe o grafo do brasil
brasil = generate_brasil_graph()


# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
vetor = [None, None]
shortestPath = []
aux = [False]

# Map
mapaImg = pygame.image.load('./assets/map.png')
mapX = 400
mapY = 200

# Flag
rawFlag = pygame.image.load('./assets/flag.png')
resizeFlag = pygame.transform.scale(rawFlag, (20,24))

# Text
font = pygame.font.SysFont(None, 36)
msg = font.render('Escolha o estado origem e o destino!', True, "black")

def text():
    screen.blit(msg, (1280/3-20, 50))

def flag(x, y):
    screen.blit(resizeFlag, (x, y))

def map():
    screen.blit(mapaImg, (mapX, mapY))

class Button():
    def __init__(self, pos, text, node):
        self.x, self.y = pos
        self.node = node
        self.surface = pygame.Surface((18, 14))
        self.surface.fill("black")
        self.surface.set_alpha(0)
        self.text = text
        self.rect = pygame.Rect(self.x, self.y, 18, 14)


    def knowNode(self, node):
        self.surface = pygame.Surface((18, 14))
        self.rect = pygame.Rect(self.x, self.y, 18, 14)
        self.surface.set_alpha(0)
        if vetor[0] == None:
            vetor[0] = node
        elif vetor[0] != None and vetor[1] == None:
            vetor[1] = node
            aux[0] = True
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
    "AC",
    0
    )

button2 = Button(
    (851, 380),
    "AL",
    1
    )

button3 = Button(
    (503, 305),
    "AM",
    2
    )

button4 = Button(
    (650, 242),
    "AP",
    3
    )

button5 = Button(
    (766, 402),
    "BA",
    4
    )

button6 = Button(
    (796, 322),
    "CE",
    5
    )

button7 = Button(
    (681, 435),
    "DF",
    6
    )

button8 = Button(
    (793, 498),
    "ES",
    7
    )

button9 = Button(
    (673, 450),
    "GO",
    8
    )

button10 = Button(
    (732, 316),
    "MA",
    9
    )

button11 = Button(
    (735, 472),
    "MG",
    10
    )

button12 = Button(
    (617, 493),
    "MS",
    11
    )

button13 = Button(
    (609, 409),
    "MT",
    12
    )

button14 = Button(
    (635, 314),
    "PA",
    13
    )

button15 = Button(
    (864, 347),
    "PB",
    14
    )

button16 = Button(
    (862, 361),
    "PE",
    15
    )

button17 = Button(
    (762, 350),
    "PI",
    16
    )

button18 = Button(
    (652, 542),
    "PR",
    17
    )

button19 = Button(
    (768, 535),
    "RJ",
    18
    )

button20 = Button(
    (859, 326),
    "RN",
    19
    )

button21 = Button(
    (520, 384),
    "RO",
    20
    )

button22 = Button(
    (541, 237),
    "RR",
    21
    )

button23 = Button(
    (633, 602),
    "RS",
    22
    )


button24 = Button(
    (668, 573),
    "SC",
    23
    )

button25 = Button(
    (835, 397),
    "SE",
    24
    )

button26 = Button(
    (682, 515),
    "SP",
    25
    )

button27 = Button(
    (691, 382),
    "TO",
    26
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
   
    if aux[0] == True:
        shortestPath = BFS(brasil, vetor[0], vetor[1])
        for i in range(len(shortestPath)):
            match shortestPath[i]:
                case 0:
                    flag(420, 354)
                case 1:
                    flag(851, 380)
                case 2:
                    flag(503, 305)
                case 3:
                    flag(650, 242)
                case 4:
                    flag(766, 402)
                case 5:
                    flag(796, 322)
                case 6:
                    flag(681, 435)
                case 7:
                    flag(793, 498)
                case 8:
                    flag(673, 450)
                case 9:
                    flag(732, 316)
                case 10:
                    flag(735, 472)
                case 11:
                    flag(617, 493)
                case 12:
                    flag(609, 409)
                case 13:
                    flag(635, 314)
                case 14:
                    flag(864, 347)
                case 15:
                    flag(862, 361)
                case 16:
                    flag(762, 350)
                case 17:
                    flag(652, 542)
                case 18:
                    flag(768, 535)
                case 19:
                    flag(859, 326)
                case 20:
                    flag(520, 384)
                case 21:
                    flag(541, 237)
                case 22:
                    flag(633, 602)
                case 23:
                    flag(668, 573)
                case 24:
                    flag(835, 397)
                case 25:
                    flag(682, 515)
                case 26:
                    flag(691, 382)

                
        
    # RENDER YOUR GAME HERE
    map()
    text()

    # flip() the display to put your work on screen
    pygame.display.update()
    #pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()