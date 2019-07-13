from modules.BaseModule import BaseModule
from pygame import Surface, Rect


class SolidBlock(BaseModule):

    name = "Solid Block"

    def __init__(self, x, y, z, width, height, colour, parent = None):
        super().__init__(x, y, z, width, height, transparent=False, parent=parent)
        self.colour = colour

    def draw(self, surface):
        surface.fill(self.colour, self.bounds)
        return self.bounds

    def draw_portion(self, surface:Surface, bounds:Rect):
        surface.fill(self.colour, bounds, bounds)
        return bounds