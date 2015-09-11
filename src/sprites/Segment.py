from MovableSprite import *

class Segment(MovableSprite):
    def __init__(self, x, y):
        super(Segment, self).__init__(SEGMENT_SIZE, SEGMENT_SIZE, x, y)
        self.image.fill(SNAKE_COLOR)
        self.direction = RIGHT

    def setDirection(self, direction):
        """ Determines in which direction the segment should move when it becomes the tail"""
        self.direction = direction
