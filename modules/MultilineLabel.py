from modules.BaseModule import BaseModule
from pygame import Surface, Rect
from drawing import *
from pygame.font import FontType
from itertools import chain


class MultiLineLabel(BaseModule):

    name = "Label"

    def __init__(self, x, y, z, width, height, text, font: FontType, colour_text, colour_background=None,
                 auto_size=False, alias_text=False, parent=None):
        super().__init__(x, y, z, width, height, transparent=(colour_background is None), parent=parent)
        self.text = text
        self.font = font
        self.lines = []
        self.colour_text = colour_text
        self.colour_background = colour_background
        self.auto_size = auto_size
        self.alias_text = alias_text
        self.updateText()


    def draw(self, surface):
        update_area = self.bounds.copy()

        if self.auto_size:
            self.bounds.height = len(self.lines) * self.font.get_height()

        if self.colour_background is not None:
            surface.fill(self.colour_background, self.bounds)

        dy = 0
        for line in self.lines:
            surface_text = self.font.render(line, self.alias_text, self.colour_text)
            if dy + surface_text.get_height() <= self.bounds.height:
                surface.blit(surface_text, (self.bounds.x, self.bounds.y + dy))
                dy += surface_text.get_height()
            else:
                break

        return update_area

    def updateText(self, text = None, font:FontType = None, colour = None):
        self.text = (self.text if text is None else text)
        self.font = (self.font if font is None else font)
        self.colour_text = (self.colour_text if colour is None else colour)
        self.lines = self.wrap_multi_line(self.text, self.font, self.bounds.width)
        if self.auto_size:
            self.bounds.height = max(len(self.lines) * self.font.get_height(), self.bounds.height)
        self.changed = True


    @classmethod
    def truncline(cls, text, font, max_width):
        text_length = len(text)
        stext = text
        text_width = font.size(text)[0]
        cut = 0
        a = 0
        done = 1
        old = None
        while text_width > max_width:
            a = a + 1
            n = text.rsplit(None, a)[0]
            if stext == n:
                cut += 1
                stext = n[:-cut]
            else:
                stext = n
            text_width = font.size(stext)[0]
            text_length = len(stext)
            done = 0
        return text_length, done, stext

    @classmethod
    def wrapline(cls, text, font, maxwidth):
        done = 0
        wrapped = []

        while not done:
            nl, done, stext = cls.truncline(text, font, maxwidth)
            wrapped.append(stext.strip())
            text = text[nl:]
        return wrapped

    @classmethod
    def wrap_multi_line(cls, text, font, maxwidth):
        """ returns text taking new lines into account.
        """
        lines = chain(*(cls.wrapline(line, font, maxwidth) for line in text.splitlines()))
        return list(lines)

