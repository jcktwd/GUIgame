from modules.BaseModule import BaseModule
from pygame import image, transform

class Image(BaseModule):

    name = "Image"

    def __init__(self, x, y, z, width, height, file_address, parent = None):
        self.surface_image = transform.smoothscale(image.load(file_address), (width, height))
        super().__init__(x, y, z, width, height, parent)

    def draw(self, surface):
        surface.blit(self.surface_image, self.bounds)
        return self.bounds

    def draw_portion(self, surface, bounds):
        surface.blit(self.surface_image, bounds, bounds)
        return bounds

