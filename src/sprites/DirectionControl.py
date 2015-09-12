from MovableSprite import *

class DirectionControl(MovableSprite):
    def __init__(self, x, y, direction):
        super(DirectionControl, self).__init__(SEGMENT_SIZE, SEGMENT_SIZE, x, y)
        self.image = self.image.convert_alpha()
        self.image.fill((0, 0, 0, 0))

        self.letter = ''
        self.direction = direction

        self.setHeadPosition(x, y)
        self.rect.x = self.targetX
        self.rect.y = self.targetY

    def setHeadPosition(self, targetX, targetY):
        super(DirectionControl, self).moveTo(
            FIELD_MARGIN + targetX + self.direction[0] * SEGMENT_SIZE,
            FIELD_MARGIN + targetY + self.direction[1] * SEGMENT_SIZE)

    def setLetter(self, letter):
        self.letter = letter

        # Paint the letter
        font = pygame.font.Font(None, int(1.3 * SEGMENT_SIZE))
        text = font.render(self.letter, True, DIRECTION_CONTROL_COLOR)
        textRect = text.get_rect(centerx=SEGMENT_SIZE/2)

        self.image.fill((0, 0, 0, 0))
        self.image.blit(text, textRect)
