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

move_x = 0
move_y = 0

clock = pygame.time.Clock()
FPS = 20

while True:

    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move_x = 5
                move_y = 0
            elif event.key == pygame.K_DOWN:
                move_y = 5
                move_x = 0
            elif event.key == pygame.K_UP:
                move_y = -5
                move_x = 0
            elif event.key == pygame.K_LEFT:
                move_x = -5
                move_y = 0
        # if event.type == pygame.KEYUP:
        #     move_x = 0

    screen.fill(white)

    pygame.draw.rect(screen, red, [rect_x,rect_y,50,50])

    rect_x += move_x
    rect_y += move_y

    if rect_x > width:
        rect_x = -50
    if rect_x == 0 or rect_x == width - 50:
        move_x = 0
    elif rect_y == 0 or rect_y == height - 50:
        move_y = 0

    pygame.display.update()
    clock.tick(FPS)