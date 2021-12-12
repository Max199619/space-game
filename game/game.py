import sys
import pygame
pygame.init()
import os
pygame.font.init()
pygame.mixer.init()

FPS = 60

YELLOW_HIT = pygame.USEREVENT+1
RED_HIT = pygame.USEREVENT+2

SPACESHIP_WIDTH,SPACESHIP_HEIGHT = 55,40
YELLOW_SPACESHIP_IMAGE = pygame.image.load("Assets/spaceship_yellow.png")
RED_SPACESHIP_IMAGE = pygame.image.load("Assets/spaceship_red.png")
#BULLET_HIT_SOUND = pygame.mixer.Sound("Assets/Grenade+1.mp3")
#BULLET_FIRE_SOUND = pygame.mixer.Sound("Assets/Gun+Silencer.mp3")

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)
HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 70)

VEL = 5
WIDTH,HEIGHT = 900,500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame_display_set_caption = "space fight"

BORDER = pygame.Rect(WIDTH/2 - 5, 0, 10, HEIGHT)

YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),90) 
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),270)
SPACE = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "space.png")), (WIDTH,HEIGHT))

NUM_BULLETS = 3
BULLET_VEL = 8

def handle_yellow_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x - VEL > 0:
        yellow.x -= VEL
            
    if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < BORDER.x:
         yellow.x += VEL

    if keys_pressed[pygame.K_w] and yellow.y - VEL > 0:
         yellow.y -= VEL

    if keys_pressed[pygame.K_s] and yellow.y + VEL < HEIGHT - SPACESHIP_HEIGHT - 10:
         yellow.y += VEL 

def handle_red_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x - VEL - red.width + 30 > BORDER.x:
        red.x -= VEL
            
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL < WIDTH - SPACESHIP_WIDTH + 20:
         red.x += VEL

    if keys_pressed[pygame.K_UP] and red.y - VEL > 0:
         red.y -= VEL

    if keys_pressed[pygame.K_DOWN] and red.y + VEL < HEIGHT - SPACESHIP_HEIGHT - 10:
         red.y += VEL 

def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
        bullet.x += BULLET_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            yellow_bullets.remove(bullet)

    for bullet in red_bullets:
        bullet.x -= BULLET_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)

def draw_window(red,yellow,red_bullets, yellow_bullets, red_health, yellow_health):
    WIN.blit(SPACE,(0,0))
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    pygame.draw.rect(WIN, BLACK, BORDER)
    for bullet in red_bullets:
        pygame.draw.rect(WIN,RED,bullet)
    
    for bullet in yellow_bullets:
        pygame.draw.rect(WIN,YELLOW,bullet)
    
    red_health_text = HEALTH_FONT.render("Health: " + str(red_health), 1, WHITE)
    yellow_health_text = HEALTH_FONT.render("Health: "+ str(yellow_health), 1, WHITE)

    WIN.blit(red_health_text, (WIDTH - red_health_text.get_width()-10, 10))
    WIN.blit(yellow_health_text, (10, 10))

    
    pygame.display.update()

def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width()/2, HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)

def main():
    red = pygame.Rect(700,300, SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100,300, SPACESHIP_WIDTH,SPACESHIP_HEIGHT)

    red_bullets = []
    yellow_bullets = []

    yellow_health = 10
    red_health = 10

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                run = False


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < NUM_BULLETS:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height//2-2, 10, 5)
                    yellow_bullets.append(bullet)
                    #BULLET_FIRE_SOUND.play()
                if event.key == pygame.K_RCTRL and len(red_bullets) < NUM_BULLETS:
                    bullet = pygame.Rect(red.x, red.y + red.height//2-2, 10, 5)
                    red_bullets.append(bullet)
                    #BULLET_FIRE_SOUND.play()

            if event.type == RED_HIT:
                red_health -= 1
                #BULLET_HIT_SOUND.play()
            if event.type == YELLOW_HIT:
                yellow_health -= 1
                #BULLET_HIT_SOUND.play()

        winner_text =""
        if red_health <= 0:
            winner_text = "Yellow wins"
        if yellow_health <= 0:
            winner_text = "Red wins"

        if winner_text != "": 
            draw_winner(winner_text)
            break
            
        keys_pressed = pygame.key.get_pressed()
        handle_yellow_movement(keys_pressed, yellow)
        handle_red_movement(keys_pressed, red)
                
        handle_bullets(yellow_bullets, red_bullets, yellow, red)    
            
        draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health)

    main()


if __name__ == "__main__":
    main()