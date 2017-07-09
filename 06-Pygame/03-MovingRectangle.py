import pygame

pygame.init()

white = 255,255,255
black = 0,0,0
red = 255,0,0
blue = 255,0,255

height = 500
width = 800

screen = pygame.display.set_mode((width,height))

rect_x = width/2 - 25
rect_y = height/2 - 25

move_x = 5
move_y = 5

clock = pygame.time.Clock()
FPS = 20

while True:

    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill(white)

    pygame.draw.rect(screen, red, [rect_x,rect_y,50,50])

    rect_x += move_x
    rect_y -= move_y

    pygame.display.update()
    clock.tick(FPS)