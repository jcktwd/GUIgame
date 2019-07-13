from modules.BaseModule import BaseModule
from pygame.constants import *
from pygame import Surface, Rect


class TransparencyBlock(BaseModule):
    name = "Transparency Block"

    def __init__(self, x, y, z, width, height, alpha_colour, parent = None):
        super().__init__(x, y, z, width, height, transparent=True, parent=parent)
        self.alpha_colour = alpha_colour
        self.alpha_surface = Surface((width, height), SRCALPHA)
        self.alpha_surface.fill(self.alpha_colour)

    def draw(self, surface):
        surface.blit(self.alpha_surface, self.bounds)
        return self.bounds

    def draw_portion(self, surface:Surface, bounds:Rect):
        surface.blit(self.alpha_surface, bounds, Rect(bounds.left - self.bounds.left, bounds.top - self.bounds.top,
                                                      bounds.width, bounds.height))
        return bounds
