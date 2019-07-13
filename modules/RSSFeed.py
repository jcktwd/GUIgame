from modules.BaseModule import BaseModule
from modules.MultilineLabel import MultiLineLabel
from colours import *
import datetime
import feedparser
import pygame


class RSSFeed(BaseModule):
    name = "RSS Module"

    def __init__(self, x, y, z, width, height, feed_url, update_frequency, parent = None):
        super().__init__(x, y, z, width, height, transparent=True, parent=parent)
        self.previous_time = datetime.datetime.now()
        self.update_frequency = update_frequency
        self.feed_url = feed_url
        self.feed = feedparser.parse(self.feed_url)
        self.font_titles = pygame.font.Font("./fonts/Roboto/Roboto-Regular.ttf", 38)
        self.font_summaries = pygame.font.Font("./fonts/Roboto/Roboto-Thin.ttf", 28)
        self.changed = True

    def update(self):
        time_difference = datetime.datetime.now() - self.previous_time
        if time_difference > self.update_frequency:
            self.feed = feedparser.parse(self.feed_url)
            self.changed = True

    def draw(self, surface):
        x, y = self.bounds.topleft
        title = MultiLineLabel(x, y, self.z, self.bounds.width, self.font_titles.get_height(),
                               self.feed["feed"]["title"], self.font_titles, WHITE, None, True, True)
        title.draw(surface)
        y += title.bounds.height
        x += 10
        dy = 0
        for entry in self.feed.entries:
            title = MultiLineLabel(x, y + dy, self.z, self.bounds.width - 10, self.font_titles.get_height(),
                                   entry["title"], self.font_titles, WHITE, None, True, True)
            summary = MultiLineLabel(x, y + dy + title.bounds.height, self.z, self.bounds.width - 10,
                                     self.font_summaries.get_height(), entry["summary"], self.font_summaries,
                                     WHITE, None, True, True)

            if not self.bounds.collidepoint(x, y + dy + title.bounds.height + summary.bounds.height):
                break
            else:
                title.draw(surface)
                summary.draw(surface)
                dy += title.bounds.height + summary.bounds.height + 8

        self.changed = False
        return self.bounds.copy()

    def forceUpdate(self):
        self.feed = feedparser.parse(self.feed_url)
        self.changed = True