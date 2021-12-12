import pygame
import os

FPS = 60

WHITE = (255,255,255)

WIDTH,HEIGHT = 900,500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame_display_set_caption = "space fight"
clock = pygame.time.Clock()

def draw():
    WIN.fill(WHITE)
    pygame.display.update()

def main():

    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw()


if __name__ == "__main__":
    main()