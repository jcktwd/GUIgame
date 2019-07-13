from modules.Label import Label
import datetime


class DigitalClock(Label):
    name = "Digital Clock"

    def __init__(self, x, y, z, font, colour_text, format_string, colour_background = None, parent = None):
        self.previous_time = datetime.datetime.now()
        self.update_frequency = datetime.timedelta(seconds=1)
        self.format_string = format_string

        super().__init__(x, y, z, 1, 1, self.previous_time.strftime(self.format_string), font, colour_text,
                         colour_background=colour_background, auto_size=True, alias_text=True, parent=parent)


    def on_update(self):
        current_time = datetime.datetime.now()
        if (current_time - self.previous_time) >= self.update_frequency:
            self.previous_time = current_time
            self.updateText(text=current_time.strftime(self.format_string))
            return True
        return False
