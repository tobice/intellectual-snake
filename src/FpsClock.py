
import pygame

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
