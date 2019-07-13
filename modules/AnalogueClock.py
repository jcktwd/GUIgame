from modules.BaseModule import BaseModule

import datetime


class AnalogueClock(BaseModule):
    name = "Analogue Clock"

    def __init__(self, x, y, length, colour_background, parent = None):
        super().__init__(x, y, length, length, parent)
        self.time = datetime.datetime.now()
        self.colour_background = colour_background
        self.radius = (length // 2) - 4
        self.centreX, self.centreY = x + self.radius, y + self.radius
        self.spacing = length // 50

    def update(self):
        currentTime = datetime.datetime.now()
        delta = currentTime - self.time
        if delta.seconds >= 1:
            self.time = currentTime
            self.changed = True

    def draw(self, surface):
        surface.fill(self.colour_background, self.bounds)
        # draw here
        drawing.draw_empty_circle(surface, self.centreX, self.centreY, self.radius - self.spacing, 3, WHITE)
        #drawing.draw_circle(surface, self.centreX, self.centreY, self.spacing, self.spacing, WHITE)
        # work out where 1 and 2 are on the clock then transform for the rest
        increment = math.pi / 6
        for i in (1, 2):
            angle = i * increment
            dx1 = int((self.radius - 3 * self.spacing) * math.cos(angle))
            dy1 = int((self.radius - 3 * self.spacing) * math.sin(angle))
            dx2 = int((self.radius - 5 * self.spacing) * math.cos(angle))
            dy2 = int((self.radius - 5 * self.spacing) * math.sin(angle))
            pygame.draw.aaline(surface, WHITE, (self.centreX + dx1, self.centreY + dy1),
                             (self.centreX + dx2, self.centreY + dy2), self.spacing)
            pygame.draw.aaline(surface, WHITE, (self.centreX + dx1, self.centreY - dy1),
                             (self.centreX + dx2, self.centreY - dy2), self.spacing)
            pygame.draw.aaline(surface, WHITE, (self.centreX - dx1, self.centreY - dy1),
                             (self.centreX - dx2, self.centreY - dy2), self.spacing)
            pygame.draw.aaline(surface, WHITE, (self.centreX - dx1, self.centreY + dy1),
                             (self.centreX - dx2, self.centreY + dy2), self.spacing)
        pygame.draw.aaline(surface, WHITE, (self.centreX, self.centreY + self.radius - 2 * self.spacing),
                           (self.centreX, self.centreY + self.radius - 6 * self.spacing))
        pygame.draw.aaline(surface, WHITE, (self.centreX, self.centreY - self.radius + 2 * self.spacing),
                           (self.centreX, self.centreY - self.radius + 6 * self.spacing))
        pygame.draw.aaline(surface, WHITE, (self.centreX + self.radius - 2 * self.spacing, self.centreY),
                           (self.centreX + self.radius - 6 * self.spacing, self.centreY))
        pygame.draw.aaline(surface, WHITE, (self.centreX - self.radius + 2 * self.spacing, self.centreY),
                           (self.centreX - self.radius + 6 * self.spacing, self.centreY))

        sHAngle = ((self.time.second / 30) - 0.5) * math.pi
        x2 = int(self.centreX + (self.radius - 7 * self.spacing) * math.cos(sHAngle))
        y2 = int(self.centreY + (self.radius - 7 * self.spacing) * math.sin(sHAngle))
        drawing.draw_line(surface, self.centreX, self.centreY, x2, y2, 1, WHITE)
        # pygame.draw.aaline(surface, WHITE, (self.centreX, self.centreY), (x2, y2))
        mHAngle = ((self.time.minute / 30) + (self.time.second / 1800) - 0.5) * math.pi
        x2 = int(self.centreX + (self.radius - 12 * self.spacing) * math.cos(mHAngle))
        y2 = int(self.centreY + (self.radius - 12 * self.spacing) * math.sin(mHAngle))
        drawing.draw_line(surface, self.centreX, self.centreY, x2, y2, 2, WHITE)
        hHAngle = ((self.time.hour / 6) + (self.time.minute / 360) - 0.5) * math.pi
        x2 = int(self.centreX + (self.radius - 20 * self.spacing) * math.cos(hHAngle))
        y2 = int(self.centreY + (self.radius - 20 * self.spacing) * math.sin(hHAngle))
        drawing.draw_line(surface, self.centreX, self.centreY, x2, y2, 5, WHITE)

        self.changed = False
        return self.bounds.copy()