from modules import *
from application import Application
from colours import *
from datetime import timedelta
import pygame

if __name__ == "__main__":
    app = Application()
    app.addModules(ImageSlideShow(0, 0, 0, 1920, 1080, ("./images/ceiling.jpg", "./images/bridge.jpg",
                                                         "./images/under_bridge.jpg", "./images/firth.jpg",
                                                         "./images/over_bridge.jpg", "./images/mountain.jpg"),
                                   timedelta(minutes=1)),
                    TransparencyBlock(0, 0, 1, 1828, 32, TITLE_OVERLAY_BLACK),
                    DigitalClock(4, 0, 2, pygame.font.Font("./fonts/Roboto/Roboto-Light.ttf", 24), WHITE,
                                 "%H:%M:%S %p - %A, %d %B %Y"),
                    Button(1874, 0, 1, 46, 32, "×", pygame.font.Font("./fonts/Roboto/Roboto-Light.ttf", 32),
                           WHITE, BLACK, TITLE_RED, TITLE_PALE_RED, lambda: app.stop()),
                    Button(1828, 0, 1, 46, 32, "-", pygame.font.Font("./fonts/Roboto/Roboto-Light.ttf", 32),
                           WHITE, BLACK, TITLE_GREY, TITLE_LIGHT_GREY, lambda: app.minimise()),
                    TransparencyBlock(16, 48, 1, 936, 420, UI_OVERLAY_BLACK),
                    BinaryClock(32, 64, 2, 904, 388, WHITE),

                    TransparencyBlock(968, 48, 1, 920, 1016, UI_OVERLAY_DARK),
                    RSSFeed(984, 64, 2, 888, 984, "http://feeds.bbci.co.uk/news/rss.xml", timedelta(minutes=5)),
                    FPSCounter(0, 1000, 1, pygame.font.Font("./fonts/Roboto/Roboto-Light.ttf", 32), WHITE, app.clock))
    app.run()