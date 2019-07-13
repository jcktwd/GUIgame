from modules.BaseModule import BaseModule
from pygame import image, transform
from datetime import datetime, timedelta

class ImageSlideShow(BaseModule):

    name = "Image Slide Show"

    def __init__(self, x: int, y: int, z:int , width: int, height: int, image_files: tuple, update_frequency: timedelta,
                 parent: BaseModule = None):
        super().__init__(x, y, z, width, height, transparent=False, parent=parent)
        self.image_files = image_files
        self.update_frequency = update_frequency
        self.last_time = datetime.now()
        self.images = [transform.smoothscale(image.load(file), (self.bounds.width, self.bounds.height))
                       for file in image_files]
        self.current_index = 0
        self.current_image = self.images[0]

    def on_update(self):
        current_time = datetime.now()
        if (current_time - self.last_time) >= self.update_frequency:
            self.last_time = current_time
            self.current_index = (self.current_index + 1) % len(self.images)
            self.current_image = self.images[self.current_index]
            return True
        return False

    def draw(self, surface):
        surface.blit(self.current_image, self.bounds)
        return self.bounds

    def draw_portion(self, surface, bounds):
        surface.blit(self.current_image, bounds, bounds)
        return bounds
