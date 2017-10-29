# Snake Game!

import pygame
import sys
import random
import time

# check for Initialization errors
check_errors = pygame.init()
if check_errors[1] > 0:
    print('(!) Had {0} initialization errors, exiting...'.format(check_errors[1]))
    sys.exit(-1)
else:
    print('(+) PyGame Successfully Initialized')

# Play Surface
playSurface = pygame.display.set_mode((720, 460))
pygame.display.set_caption('Snake Game!')

# Colors

red = pygame.Color(255, 0, 0)           # GameOver
green = pygame.Color(0, 255, 0)         # Snake
black = pygame.Color(0, 0, 0)           # Score
brown = pygame.Color(165, 42, 42)       # Food
white = pygame.Color(255, 255, 255)     # White

# Frame Per Second(FPS) Controller

fpsController = pygame.time.Clock()

# Important variables

snakePos = [100, 50]
snakeBody = [[100, 50], [90, 50], [80, 50]]

foodPos = random.randrange(1, 72)*10, random.randrange(1, 46)*10
foodSpawn = True

direction = 'RIGHT'
changeTo = direction

Score = 0


# Game Over Function
def over():
    myfont = pygame.font.SysFont('monaco', 72)
    gosurf = myfont.render('GAME OVER!', True, red)
    gorect = gosurf.get_rect()
    gorect.midtop = (360, 15)
    playSurface.blit(gosurf, gorect)
    pygame.display.flip()
    score(0)
    time.sleep(5)
    pygame.quit()   # pyGame exit
    sys.exit()      # Console exit


def score(choice=1):
    sfont = pygame.font.SysFont('monaco', 30)
    ssurf = sfont.render('SCORE : {0}'.format(Score), True, black)
    srect = ssurf.get_rect()
    if choice == 1:
        srect.midtop = (60, 10)
    else:
        srect.midtop = (360, 70)
    playSurface.blit(ssurf, srect)
    pygame.display.flip()


# Restart
def restart():
    rfont = pygame.font.SysFont('monaco', 10)
    rsurf = rfont.render('PRESS 'R' to RESTART', True, red)
    rrect = rsurf.get_rect()
    rrect.midtop = (360, 100)
    playSurface.blit(rsurf, rrect)
    restart()
    pygame.display.flip()


# Main Logic of the Game

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                changeTo = 'RIGHT'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                changeTo = 'LEFT'
            if event.key == pygame.K_UP or event.key == ord('w'):
                changeTo = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                changeTo = 'DOWN'
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))

    # Validation of direction
    if changeTo == 'RIGHT' and not direction == 'LEFT':
        direction = 'RIGHT'
    if changeTo == 'LEFT' and not direction == 'RIGHT':
        direction = 'LEFT'
    if changeTo == 'UP' and not direction == 'DOWN':
        direction = 'UP'
    if changeTo == 'DOWN' and not direction == 'UP':
        direction = 'DOWN'

    # Update the snake Position [x, y]

    if direction == 'RIGHT':
        snakePos[0] += 10
    if direction == 'LEFT':
        snakePos[0] -= 10
    if direction == 'DOWN':
        snakePos[1] += 10
    if direction == 'UP':
        snakePos[1] -= 10

    # Snake Body Mechanism

    snakeBody.insert(0, list(snakePos))
    if snakePos[0] == foodPos[0] and snakePos[1] == foodPos[1]:
        Score += 1
        foodSpawn = False
    else:
        snakeBody.pop()
    if foodSpawn == False:
        foodPos = random.randrange(1, 72)*10, random.randrange(1, 46)*10
    foodSpawn = True

    playSurface.fill(white)
    for pos in snakeBody:
        pygame.draw.rect(playSurface, green, pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.draw.rect(playSurface, brown, pygame.Rect(foodPos[0], foodPos[1], 10, 10))

    # Boundary
    if snakePos[0] > 710 or snakePos[0] < 0:
        over()
    if snakePos[1] > 450 or snakePos[1] < 0:
        over()

    for block in snakeBody[1:]:
        if snakePos[0] == block[0] and snakePos[1] == block[1]:
            over()
    pygame.display.flip()
    score()
    fpsController.tick(20)
