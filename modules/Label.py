from modules.BaseModule import BaseModule

class Label(BaseModule):

    name = "Label"

    def __init__(self, x, y, z, width, height, text, font, colour_text, colour_background=None, auto_size=False,
                 alias_text=False, parent=None):
        super().__init__(x, y, z, width, height, transparent=(colour_background is None), parent=parent)
        self.text = text
        self.font = font
        self.colour_text = colour_text
        self.colour_background = colour_background
        self.auto_size = auto_size
        self.alias_text = alias_text

    def draw(self, surface):
        update_area = self.bounds.copy()
        surface_text = self.font.render(self.text, self.alias_text, self.colour_text)
        if self.auto_size:
            self.bounds.size = surface_text.get_size()
            update_area.union(self.bounds)
        if self.colour_background is not None:
            surface.fill(self.colour_background, self.bounds)
        surface.blit(surface_text, self.bounds)
        return update_area

    def updateText(self, text = None, font = None, colour = None):
        self.text = (self.text if text is None else text)
        self.font = (self.font if font is None else font)
        self.colour_text = (self.colour_text if colour is None else colour)
        self.changed = True