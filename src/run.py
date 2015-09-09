#!/usr/bin/env python

import pygame
from IntellectualSnake import *
from FpsClock import *

def main():
    # Initialize Everything
    pygame.init()
    pygame.display.set_caption('Intellectual snake')
    clock = pygame.time.Clock()
    fpsClock = FpsClock()

    snake = IntellectualSnake()
    snake.render()
    fpsClock.begin()

    while snake.isRunning():
        clock.tick(60)
        fpsClock.tick()

        snake.update(fpsClock.getFrameDuration())
        snake.render()

        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    main()

