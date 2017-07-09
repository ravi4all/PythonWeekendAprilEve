import pygame

pygame.init()

white = 255,255,255
black = 0,0,0
red = 255,0,0
blue = 255,0,255

height = 400
width = 800

screen = pygame.display.set_mode((width,height))

while True:

    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill(white)
    pygame.display.update()