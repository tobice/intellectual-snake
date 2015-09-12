#!/usr/bin/env python

import sys
import os
from IntellectualSnake import *
from src.utils.FpsClock import *

def main():
    # Initialize Everything
    pygame.init()
    pygame.display.set_caption('Intellectual snake')
    clock = pygame.time.Clock()
    fpsClock = FpsClock()

    # Load dictionary
    dictionary = loadDictionary()

    snake = IntellectualSnake(dictionary)
    snake.render()
    fpsClock.begin()

    while snake.isRunning():
        clock.tick(60)
        fpsClock.tick()

        snake.update(fpsClock.getFrameDuration())
        snake.render()

        pygame.display.flip()

    pygame.quit()

def loadDictionary():
    path = os.path.dirname(sys.argv[0]) + "/../assets/dictionary"
    if not os.path.isfile(path):
        print("Unable to find the dictionary file in the assets folder!")
        sys.exit(1)

    dictionary = open(path, "r")
    words = dictionary.read().splitlines()
    dictionary.close()

    return words

if not pygame.font:
    print ('Fonts disabled! Unable to play the game')
    sys.exit(1)

if __name__ == '__main__':
    main()
