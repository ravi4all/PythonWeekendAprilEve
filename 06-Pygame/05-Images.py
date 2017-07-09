import pygame

pygame.init()

white = 255,255,255
black = 0,0,0
red = 255,0,0
blue = 255,0,255

height = 500
width = 800

screen = pygame.display.set_mode((width,height))

hulk = pygame.image.load("assets/image_1.png")

hulk_x = width/2 - 64
hulk_y = height/2 - 68

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

    # pygame.draw.rect(screen, red, [hulk_x,hulk_y,50,50])

    screen.blit(hulk,[hulk_x, hulk_y])

    hulk_x += move_x
    hulk_y += move_y

    # print(hulk_x, hulk_y)

    if hulk_x == 1 or hulk_x == width - 119:
        move_x = 0
        print(move_x)
    elif hulk_y == 1 or hulk_y == height - 118:
        move_y = 0
        print(move_y)

    pygame.display.update()
    clock.tick(FPS)