from modules.Label import Label


class FPSCounter(Label):
    name = "FPS Counter"

    def __init__(self, x, y, z, font, colour_text, clock, parent = None):
        self.clock = clock
        super().__init__(x, y, z, 1, 1, "", font, colour_text, auto_size=True,
                         alias_text=True, parent=parent)
        self.changed = self.on_update()

    def on_update(self):
        self.updateText("Avg FPS: {:.2f}".format(self.clock.get_fps()))
        return True
