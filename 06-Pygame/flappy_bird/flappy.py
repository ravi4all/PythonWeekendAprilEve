import pygame
import random

pygame.init()

size = width, height = 400, 600

white = 255,255,255
red = 255,0,0

screen = pygame.display.set_mode(size)

bg_img = pygame.image.load("assets/background.png")
bird = pygame.image.load("assets/0.png")
top_wall = pygame.image.load("assets/top.png")
bottom_wall = pygame.image.load("assets/bottom.png")

point = pygame.mixer.Sound("assets/point.ogg")
hit = pygame.mixer.Sound("assets/die.wav")
# bg_sound = pygame.mixer.Sound("assets/audio_gt.wav")
# bg_sound.play(-1)



clock = pygame.time.Clock()
FPS = 30

def game_over():
    font = pygame.font.SysFont("", 50)
    text = font.render("Game Over", True, red)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.blit(text,[100,100])
        hit.play(1)
        # bg_sound.stop()

        pygame.display.update()


def show_counter(c):
    font = pygame.font.SysFont("", 40)
    text = font.render("Counter : "+str(c), True, red)
    screen.blit(text,[0,10])


def game():

    bird_x = 50
    bird_y = 10

    jump = 0
    jumpspeed = 10
    gravity = 10

    wall_x = width + 20

    top_wall_y = random.randint(-300,0)
    bottom_wall_y = top_wall_y + height + 20

    counter = 0

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

        bird_rect = pygame.Rect(bird_x, bird_y, bird.get_width(), bird.get_height())
        top_wall_rect = pygame.Rect(wall_x, top_wall_y, top_wall.get_width(), top_wall.get_height())
        bottom_wall_rect = pygame.Rect(wall_x, bottom_wall_y, bottom_wall.get_width(), bottom_wall.get_height())

        # bird_y += move_y

        if bird_rect.colliderect(top_wall_rect) or bird_rect.colliderect(bottom_wall_rect):
            print("Game Over")
            game_over()


        wall_x -= 10

        show_counter(counter)

        if wall_x < -90:
            wall_x = width + 20
            top_wall_y = random.randint(-300,0)
            bottom_wall_y = top_wall_y + height + 20
            counter += 1
            point.play(1)

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