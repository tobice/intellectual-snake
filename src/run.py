#!/usr/bin/env python

import sys
import os
from IntellectualSnake import *

class FpsClock:
    """
    Measures time between clock ticks.
    http://www.pygame.org/pcr/fpstimer/index.php
    """
    def __init__(self):
        self.frame_duration = 0.000
        self.this_frame_time = 0
        self.last_frame_time = 0
        return

    def tick(self):
        """Call this every frame"""
        self.this_frame_time = self.getCurrentTime()
        self.frame_duration = (self.this_frame_time - self.last_frame_time) / 1000.000
        self.last_frame_time = self.this_frame_time
        return

    def getFrameDuration(self):
        """Returns the length of the previous frame, in seconds"""
        return self.frame_duration

    def getCurrentTime(self):
        """Used internally. Returns current time in ms."""
        return pygame.time.get_ticks()

    def begin(self):
        """Starts/restarts the timer. Call just before your main loop."""
        self.last_frame_time = self.getCurrentTime()
        return

def loadDictionary():
    path = os.path.dirname(sys.argv[0]) + "/../assets/dictionary"
    if not os.path.isfile(path):
        print("Unable to find the dictionary file in the assets folder!")
        sys.exit(1)

    dictionary = open(path, "r")
    words = dictionary.read().splitlines()
    dictionary.close()

    return words

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


if not pygame.font:
    print ('Fonts disabled! Unable to play the game')
    sys.exit(1)

if __name__ == '__main__':
    main()
