from modules.BaseModule import BaseModule
from drawing import *
from pygame.font import Font
from datetime import datetime, timedelta


class BinaryClock(BaseModule):
    def __init__(self, x, y, z, width, height, colour, colour_background=None, parent=None):
        super().__init__(x, y, z, width, height, transparent=(colour_background is None), parent=parent)
        self.colour_background = colour_background
        self.previous_time = datetime.now()
        self.update_frequency = timedelta(seconds=1)
        self.colour = colour

        self.dimension = min(self.bounds.width // 7, self.bounds.height // 3)
        self.font = Font("./fonts/Roboto/Roboto-Thin.ttf", self.dimension)


    def on_update(self):
        current_time = datetime.now()
        if (current_time - self.previous_time) >= self.update_frequency:
            self.previous_time = current_time
            return True
        return False

    def draw(self, surface):

        if self.colour_background is not None:
            surface.fill(self.colour_background, self.bounds)

        # 5 bits on top for hour
        # need six bits width, two height
        circle_size = int(0.4 * self.dimension)
        circle_radius = circle_size // 2
        circle_border = (self.dimension - circle_size) // 2

        x, y = self.bounds.topleft
        letter_H = self.font.render("H", True, self.colour)
        letter_M = self.font.render("M", True, self.colour)
        letter_S = self.font.render("S", True, self.colour)
        x, y = self.bounds.left + ((self.dimension - letter_H.get_width()) // 2), self.bounds.top - (circle_border // 3)
        surface.blit(letter_H, (x, y))
        x, y = self.bounds.left + ((self.dimension - letter_M.get_width()) // 2), y + self.dimension
        surface.blit(letter_M, (x, y))
        x, y = self.bounds.left + ((self.dimension - letter_S.get_width()) // 2), y + self.dimension
        surface.blit(letter_S, (x, y))

        # do hour
        x, y = self.bounds.left + self.dimension + circle_border + circle_radius,\
               self.bounds.top + circle_border + circle_radius
        hour = self.previous_time.hour
        for i in range(5, -1, -1):
            if hour & (1 << i):
                draw_full_circle(surface, x, y, circle_radius, self.colour)
            else:
                draw_circle_outline(surface, x, y, circle_radius, self.colour)
            x += self.dimension

        # do minute
        x, y = self.bounds.left + self.dimension + circle_border + circle_radius, \
               self.bounds.top + self.dimension + circle_border + circle_radius
        minute = self.previous_time.minute
        for i in range(5, -1, -1):
            if minute & (1 << i):
                draw_full_circle(surface, x, y, circle_radius, self.colour)
            else:
                draw_circle_outline(surface, x, y, circle_radius, self.colour)
            x += self.dimension

        # do second
        x, y = (self.bounds.left + self.dimension + circle_border + circle_radius,
                self.bounds.top + 2 * self.dimension + circle_border + circle_radius)
        second = self.previous_time.second
        for i in range(5, -1, -1):
            if second & (1 << i):
                draw_full_circle(surface, x, y, circle_radius, self.colour)
            else:
                draw_circle_outline(surface, x, y, circle_radius, self.colour)
            x += self.dimension

        return self.bounds
