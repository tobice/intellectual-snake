#!/usr/bin/env python

import sys
from IntellectualSnake import *
from src.utils.FpsClock import *

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

if not pygame.font:
    print ('Fonts disabled! Unable to play the game')
    sys.exit(1)

if __name__ == '__main__':
    main()
