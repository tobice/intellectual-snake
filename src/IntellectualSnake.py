import random
from pygame.locals import *

from src.utils.textUtils import *
from src.sprites.Head import *
from src.sprites.DirectionControl import *
from src.sprites.Segment import *
from src.sprites.Food import *
from src.sprites.HudText import *

class IntellectualSnake:
    def __init__(self):
        self.running = True
        self.isGameOver = False
        self.score = 0

        # Init the screen
        screenWidth = FIELD_WIDTH + 2 * FIELD_MARGIN
        screenHeight = FIELD_HEIGHT + 2 * FIELD_MARGIN
        self.screen = pygame.display.set_mode((screenWidth, screenHeight))

        # Prepare the background
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((250, 250, 250))

        # Add hud fields
        self.hudTitle = HudText(FIELD_MARGIN, 10, 300, "Intellectual Snake!")
        self.hudGameStatus = HudText(FIELD_MARGIN, FIELD_MARGIN + FIELD_HEIGHT + 10, 300, "")
        self.hudScore = HudText(FIELD_MARGIN + FIELD_WIDTH - 100, 10, 100, "Score: 0")

        # Init The Snake
        headX = SEGMENT_SIZE * COLUMNS / 2
        headY = SEGMENT_SIZE * ROWS / 2
        self.head = Head(headX, headY)
        self.segments = []
        for i in xrange(0, INIT_SNAKE_LENGTH):
            self.segments.append(Segment(headX - i * SEGMENT_SIZE, headY))

        # Init direction controls
        self.directionControls = \
            DirectionControl(headX, headY, UP), \
            DirectionControl(headX, headY, DOWN), \
            DirectionControl(headX, headY, LEFT), \
            DirectionControl(headX, headY, RIGHT)

        for control in self.directionControls:
            control.setLetter(self.generateNewDirectionLetter())

        # Init Group of field objects that should not collide
        self.fieldObjects = pygame.sprite.Group()
        self.fieldObjects.add(self.segments)

        # Add initial food to the field
        self.addNewFood()

    def update(self, time):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                self.running = False
            elif event.type == KEYDOWN and not self.isGameOver:
                self.handleKeyDown(event.key)

        if self.isGameOver:
            return

        # Update the snake's head
        self.head.update(time)

        if self.head.moved:
            eatenFood = False

            # Check for collisions
            for sprite in pygame.sprite.spritecollide(self.head, self.fieldObjects, False):
                if type(sprite) is Food:
                    self.fieldObjects.remove(sprite)
                    self.addNewFood()
                    eatenFood = True
                    self.score += 1
                    self.hudScore.setContent("Score: %d" % self.score)
                elif type(sprite) is Segment:
                    self.hudGameStatus.setContent("Game over :-(")
                    self.isGameOver = True

            # Move the snake's body (possibly extend it if some food was eaten)
            self.moveBody(eatenFood)

            # Move direction controls to follow the snake's head
            for control in self.directionControls:
                control.setHeadPosition(self.head.rect.x, self.head.rect.y)

    def render(self):
        # Render field objects on a separate Surface (which allows us to work in an independent
        # coordinate system)
        field = pygame.Surface([FIELD_WIDTH, FIELD_HEIGHT])
        field.fill((0, 0, 255))
        field.blit(self.head.image, self.head.rect)
        self.fieldObjects.draw(field)

        # Render the game field and other UI objects directly on the screen
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(field, (FIELD_MARGIN, FIELD_MARGIN))

        for control in self.directionControls:
            self.screen.blit(control.image, control.rect)

        self.screen.blit(self.hudTitle.image, self.hudTitle.rect)
        self.screen.blit(self.hudGameStatus.image, self.hudGameStatus.rect)
        self.screen.blit(self.hudScore.image, self.hudScore.rect)

    def isRunning(self):
        return self.running

    def handleKeyDown(self, key):
        # Find direction control matching the pressed letter. If found, change the snake's
        # direction according to the control and
        control = self.findControlByLetter(pygame.key.name(key))
        if control:
            if self.head.changeDirection(control.direction):
                control.setLetter(self.generateNewDirectionLetter())

    def generateNewDirectionLetter(self):
        letter = getRandomLetter()

        # The new letter must be different from the previous one and must be unique across all
        # direction letters (to avoid ambiguity)
        while len(filter(lambda control: control.letter == letter, self.directionControls)) > 0:
            letter = getRandomLetter()

        return letter

    def addNewFood(self):
        x, y = self.generateRandomFieldPosition()
        food = Food(x, y)

        while pygame.sprite.spritecollide(food, self.fieldObjects, False):
            x, y = self.generateRandomFieldPosition()
            food = Food(x, y)

        self.fieldObjects.add(food)

    def generateRandomFieldPosition(self):
        x = random.randrange(COLUMNS) * SEGMENT_SIZE
        y = random.randrange(ROWS) * SEGMENT_SIZE
        return x, y

    def findControlByLetter(self, letter):
        controls = [control for control in self.directionControls if control.letter == letter]
        if not controls:
            return False
        else:
            return controls[0]

    def moveBody(self, eatenFood):
        # Add new segment at the head's position
        newSegment = Segment(self.head.rect.x, self.head.rect.y)
        self.segments.insert(0, newSegment)
        self.fieldObjects.add(newSegment)

        # Remove tail unless we ate food
        if not eatenFood:
            self.fieldObjects.remove(self.segments.pop())

