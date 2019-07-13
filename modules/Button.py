from modules.BaseModule import BaseModule
from modules.Label import Label

class Button(BaseModule):
    name = "Button"

    def __init__(self, x, y, z, width, height, text, font, textColour, backgroundColour, highlightColour, clickedColour,
                 onClick = None, parent = None):
        super().__init__(x, y, z, width, height, parent)

        self.text = Label(x, y, z, width, height, text, font, textColour, auto_size=True, alias_text=True, parent=self)
        self.children.append(self.text)

        self.backgroundColour = backgroundColour
        self.highlightColour = highlightColour
        self.clickedColour = clickedColour
        self.highlighted = False
        self.clicked = False

        if onClick is not None:
            self.onClick = onClick

        # centre text within button
        self.align_centre(self.text)

    def draw(self, surface):
        self.align_centre(self.text)
        if self.clicked:
            surface.fill(self.clickedColour, self.bounds)
        elif self.highlighted:
            surface.fill(self.highlightColour, self.bounds)
        else:
            surface.fill(self.backgroundColour, self.bounds)
        self.text.draw(surface)
        return self.bounds.copy()

    def on_mouse_motion(self, pos, rel, buttons):
        if self.bounds.collidepoint(*pos):
            self.highlighted = True
            return True
        else:
            if self.highlighted:
                self.highlighted = False
                return True
        return False

    def on_mouse_button_down(self, pos, button):
        if self.bounds.collidepoint(*pos):
            self.clicked = True
            return True
        return False

    def on_mouse_button_up(self, pos, button):
        if self.clicked:
            if self.bounds.collidepoint(*pos):
                self.onClick()
            self.clicked = False
            return True
        return False

    def onClick(self):
        return False