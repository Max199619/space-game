import pygame
import os

FPS = 60


SPACESHIP_WIDTH,SPACESHIP_HEIGHT = 55,40
YELLOW_SPACESHIP_IMAGE = pygame.image.load("Assets/spaceship_yellow.png")
RED_SPACESHIP_IMAGE = pygame.image.load("Assets/spaceship_red.png")

WHITE = (255,255,255)

VEL = 5
WIDTH,HEIGHT = 900,500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame_display_set_caption = "space fight"


YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),90) 
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),270)

def draw_window(red,yellow):
    WIN.fill(WHITE)
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    pygame.display.update()

def handle_yellow_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x - VEL > 0:
        yellow.x -= VEL
            
    if keys_pressed[pygame.K_d]:
         yellow.x += VEL

    if keys_pressed[pygame.K_w] and yellow.y - VEL > 0:
         yellow.y -= VEL

    if keys_pressed[pygame.K_s] and yellow.y + VEL < HEIGHT - SPACESHIP_HEIGHT - 10:
         yellow.y += VEL 

def handle_red_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT]:
        red.x -= VEL
            
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL < WIDTH - SPACESHIP_WIDTH + 20:
         red.x += VEL

    if keys_pressed[pygame.K_UP] and red.y - VEL > 0:
         red.y -= VEL

    if keys_pressed[pygame.K_DOWN] and red.y + VEL < HEIGHT - SPACESHIP_HEIGHT - 10:
         red.y += VEL 

def main():
    red = pygame.Rect(700,300, SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100,300, SPACESHIP_WIDTH,SPACESHIP_HEIGHT)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
        keys_pressed = pygame.key.get_pressed()
        handle_yellow_movement(keys_pressed, yellow)
        handle_red_movement(keys_pressed, red)
                
            
            
        draw_window(red, yellow)


if __name__ == "__main__":
    main()