import random  # to generating random numbers
import sys
from typing import Mapping      # to exit program
import pygame   
from pygame.locals import *    # basic pygame import

# Globle variables
FPS = 200
SCREENWIDTH = 289
SCREENHEIGHT = 511
SCREEN = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
BACKGROUND = 'background.jpg'
COCKPIT = 'cockpit.png'
WELLCOME = 'WELLCOME.jpg'
UFO = 'UFO.png'
ASTEROID = 'asteroid.png'
GAME_SPRITES = {}
GAME_SOUNDS = {}
def MainGame():
    while True:
        ASTOX_CHANGE = 0
        ASTOY_CHANGE = 0
        Asteroid = []
        newAsteroid = randAsteroid()
        Asteroid.append(newAsteroid[0])
        print(Asteroid)
        for event in pygame.event.get():
           # if user presses cross button,close the game
            if event.type == pygame.QUIT or (event.type==KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            
        SCREEN.blit(GAME_SPRITES['background'],(0,0))
        i = 1
        while i < 600:
            SCREEN.blit(GAME_SPRITES['background2'],(0,0))
            ASTEROID2 = pygame.transform.scale(GAME_SPRITES['asteroid'], (2*i,2*i))
            SCREEN.blit(ASTEROID2,(Asteroid[0]['x']-(i),Asteroid[0]['y']-(i)))
            SCREEN.blit(GAME_SPRITES['COCKPIT'],(0,441))
            pygame.display.update()
            if 0 < Asteroid[0]['x'] < 5 or 284 < Asteroid[0]['x'] < 289:
                if len(Asteroid) < 3:
                    Asteroid.append(newAsteroid)
            if 0 < Asteroid[0]['y'] < 5 or 506 < Asteroid[0]['x'] < 511:
                if len(Asteroid) < 3:
                    Asteroid.append(newAsteroid)
            if Asteroid[0]['x'] < -GAME_SPRITES['asteroid'].get_width() or Asteroid[0]['x'] > (SCREENWIDTH + GAME_SPRITES['asteroid'].get_width()):
                Asteroid.pop(0)
                i = 100
                break
            if Asteroid[0]['y'] < -GAME_SPRITES['asteroid'].get_height() or Asteroid[0]['y'] > (SCREENHEIGHT + GAME_SPRITES['asteroid'].get_height()):
                Asteroid.pop(0)
                i = 100
                break
            else:
                i += 1
            for event in pygame.event.get():
           # if user presses cross button,close the game
                if event.type == pygame.QUIT or (event.type==KEYDOWN and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        ASTOX_CHANGE = 1.5
                    if event.key == pygame.K_RIGHT:
                        ASTOX_CHANGE = -1.5
                    if event.key == pygame.K_UP:
                        ASTOY_CHANGE = 1.5
                    if event.key == pygame.K_DOWN:
                        ASTOY_CHANGE = -1.5
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        ASTOY_CHANGE = 0
                        ASTOX_CHANGE = 0
            Asteroid[0]['x'] += ASTOX_CHANGE
            Asteroid[0]['y'] += ASTOY_CHANGE
            FPSCLOCK.tick(FPS)
def wellcomescreen():
    while True:
       for event in pygame.event.get():
           # if user presses cross button,close the game
            if event.type == pygame.QUIT or (event.type==KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type==KEYDOWN and (event.key==K_SPACE or event.key == K_UP):
                return
            else:
                SCREEN.blit(GAME_SPRITES['wellcome'],(0,0))
                pygame.display.update()
                FPSCLOCK.tick(FPS)
def randAsteroid():
    PLAYERX = random.randint(0,200)
    PLAYERY = random.randint(0,400)
    randAst = [
        {'x' : PLAYERX, 'y' : PLAYERY}
    ]
    return randAst

if __name__ == "__main__":


    pygame.init()  #initialize all pygame modules
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption('GAME by Mahendra')
    GAME_SPRITES['wellcome'] = pygame.image.load(WELLCOME).convert()
    GAME_SPRITES['background'] = pygame.image.load(BACKGROUND).convert()
    GAME_SPRITES['UFO'] = pygame.image.load(UFO).convert_alpha()
    GAME_SPRITES['asteroid'] = pygame.image.load(ASTEROID).convert_alpha()
    GAME_SPRITES['COCKPIT'] = pygame.image.load(COCKPIT).convert_alpha()
    GAME_SPRITES['background2'] = pygame.transform.scale(GAME_SPRITES['background'], (289,441))
    while True:
        wellcomescreen()
        MainGame()