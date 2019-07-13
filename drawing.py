import pygame, pygame.gfxdraw, math
from colours import *

def draw_line(surface, x1, y1, x2, y2, thickness, colour):
    c_x, c_y = (x1 + x2) / 2, (y1 + y2) / 2
    angle = math.atan2(y2 - y1, x2 - x1)
    length = math.sqrt(((y2 - y1) ** 2) + ((x2 - x1) ** 2))
    UL = (c_x + (length / 2) * math.cos(angle) - (thickness / 2) * math.sin(angle),
          c_y + (thickness / 2) * math.cos(angle) + (length / 2) * math.sin(angle))
    UR = (c_x - (length / 2) * math.cos(angle) - (thickness / 2) * math.sin(angle),
          c_y + (thickness / 2) * math.cos(angle) - (length / 2) * math.sin(angle))
    BL = (c_x + (length / 2) * math.cos(angle) + (thickness / 2) * math.sin(angle),
          c_y - (thickness / 2) * math.cos(angle) + (length / 2) * math.sin(angle))
    BR = (c_x - (length / 2) * math.cos(angle) + (thickness / 2) * math.sin(angle),
          c_y - (thickness / 2) * math.cos(angle) - (length / 2) * math.sin(angle))
    pygame.gfxdraw.filled_polygon(surface, (UL, UR, BR, BL), colour)
    pygame.gfxdraw.aapolygon(surface, (UL, UR, BR, BL), colour)


def draw_empty_circle(surface, centre_x, centre_y, radius, thickness, colour):
    width = radius * 2 + thickness * 2
    c = width // 2
    circle = pygame.Surface((width, width), pygame.SRCALPHA)
    circle.fill(TRANSPARENT)
    pygame.draw.circle(circle, colour, (c, c), radius)
    pygame.draw.circle(circle, TRANSPARENT, (c, c), radius - thickness)
    surface.blit(circle, (centre_x - c, centre_y - c))
    pygame.gfxdraw.aacircle(surface, centre_x, centre_y, radius, colour)
    pygame.gfxdraw.aacircle(surface, centre_x, centre_y, radius - thickness, colour)


def draw_full_circle(surface, centre_x, centre_y, radius, colour):
    pygame.gfxdraw.filled_circle(surface, centre_x, centre_y, radius, colour)
    pygame.gfxdraw.aacircle(surface, centre_x, centre_y, radius, colour)


def draw_circle_outline(surface, centre_x, centre_y, radius, colour):
    pygame.gfxdraw.aacircle(surface, centre_x, centre_y, radius, colour)

def draw_rect(surface, rect, color):
    pygame.gfxdraw.rectangle(surface, rect, color)

def draw_thick_circle_outline(surface, centre_x, centre_y, radius, thickness, colour):
    pass


