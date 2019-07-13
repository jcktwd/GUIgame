from modules.BaseModule import BaseModule
from modules.Label import Label
from colours import *
import forecastio, datetime, pygame

class WeatherForecast(BaseModule):
    icon_lookup = {
        'clear-day':'\uf00d',
        'clear-night':'\uf02e',
        'rain':'\uf019',
        'snow':'\uf01b',
        'sleet':'\uf0b5',
        'wind':'\uf050',
        'fog':'\uf0b6',
        'cloudy':'\uf013',
        'partly-cloudy-day':'\uf002',
        'partly-cloudy-night':'\uf086',
        'default':'\uf07b'}

    def __init__(self, x, y, api_key, update_frequency, latitude, longitude, parent = None):
        super().__init__(x, y, 500, 500, parent)
        self.api_key = api_key
        self.update_frequency = update_frequency
        self.previous_time = datetime.datetime.now()
        self.location = (latitude, longitude)
        icon_font = pygame.font.Font("weathericons.ttf", 150)
        temp_font = pygame.font.SysFont("segoeui", 60, True)
        text_font = pygame.font.SysFont("segoeui", 100)
        self.forecast = forecastio.load_forecast(self.api_key, latitude, longitude)

        self.icon_text = Label(x, y, self.icon_lookup[self.forecast.currently().icon], icon_font, WHITE, None, self)
        self.temp_text = Label(x, y, "{:.1f}°C".format(self.forecast.currently().temperature), temp_font, WHITE, None, self)
        self.children.append(self.icon_text)
        self.children.append(self.temp_text)
        self.temp_text.bounds.x = self.icon_text.bounds.right + 10

    def update(self):
        current_time = datetime.datetime.now()
        delta = current_time - self.previous_time
        if delta >= self.update_frequency:
            self.previous_time = current_time
            self.forecast = forecastio.load_forecast(self.api_key, *self.location)
            self.icon_text.updateText(self.icon_lookup[self.forecast.currently().icon])
            self.temp_text.updateText("{:.1f}°C".format(self.forecast.currently().temperature))
            self.changed = True

    def draw(self, surface):
        surface.fill(BLACK, self.bounds)
        self.icon_text.draw(surface)
        self.temp_text.draw(surface)
        return self.bounds