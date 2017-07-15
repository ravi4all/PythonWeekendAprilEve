import pygame
import random

pygame.init()

size = width, height = 400, 600

white = 255,255,255

screen = pygame.display.set_mode(size)

bg_img = pygame.image.load("assets/background.png")
bird = pygame.image.load("assets/0.png")
top_wall = pygame.image.load("assets/top.png")
bottom_wall = pygame.image.load("assets/bottom.png")

clock = pygame.time.Clock()
FPS = 30

def game():

    bird_x = 50
    bird_y = 10

    jump = 0
    jumpspeed = 10
    gravity = 10

    wall_x = width + 20

    top_wall_y = random.randint(-300,0)
    bottom_wall_y = top_wall_y + height + 20

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    jump = 20
                    gravity = 10
                    jumpspeed = 10

        screen.fill(white)

        screen.blit(bg_img, [0,0])
        screen.blit(bird, [bird_x, bird_y])
        screen.blit(top_wall,[wall_x,top_wall_y])
        screen.blit(bottom_wall, [wall_x,bottom_wall_y])

        # bird_y += move_y

        wall_x -= 10

        if wall_x < -90:
            wall_x = width + 20
            top_wall_y = random.randint(-300,0)
            bottom_wall_y = top_wall_y + height + 20

        if bird_y > height:
            game()

        if jump:
            jumpspeed -= 1
            bird_y -= jumpspeed
            jump -= 1
        else:
            bird_y += gravity
            gravity += 0.2

        pygame.display.update()
        clock.tick(FPS)

game()