from pygame import Rect, Surface
from pygame.constants import *
from custom_events import *


class BaseModule:
    name = "unnamed_component"   # Name of module

    def __init__(self, x: int, y: int, z: int, width: int, height: int, transparent: bool=False,
                 parent: 'BaseModule'=None):
        """
        :param x: the x position of the module
        :param y: the y position of the module
        :param z: the draw order of the module (Higher is on top)
        :param width: the width of the module
        :param height: the height of the module
        :param transparent: whether or not the module is transparent (requires background to be in place)
        :param parent: the parent of this module
        """
        self.bounds = Rect(x, y, width, height)
        self.z = z
        self.transparent = transparent
        self.children = []  # List of sub-components
        self.parent = parent
        self.changed = True

    def dispatch(self, event):
        """recursively handles the event for this component and dispatches it to child components"""
        self.handle(event)
        for child in self.children:
            child.dispatch(event)
            self.changed |= child.changed

    def handle(self, event):
        if event.type == QUIT:
            self.changed |= self.on_quit()
        elif event.type == ACTIVEEVENT:
            self.changed |= self.on_active_event(event.gain, event.state)
        elif event.type ==  KEYDOWN:
            self.changed |= self.on_key_down(event.unicode, event.key, event.mod)
        elif event.type == KEYUP:
            self.changed |= self.on_key_up(event.key, event.mod)
        elif event.type == MOUSEMOTION:
            self.changed |= self.on_mouse_motion(event.pos, event.rel, event.buttons)
        elif event.type == MOUSEBUTTONUP:
            self.changed |= self.on_mouse_button_up(event.pos, event.button)
        elif event.type == MOUSEBUTTONDOWN:
            self.changed |= self.on_mouse_button_down(event.pos, event.button)
        elif event.type == UPDATE:
            self.changed |= self.on_update()

    def reset(self):
        self.changed = False

    def align_centre(self, child: 'BaseModule'):
        """aligns a child module within the parent centred"""
        child.bounds.center = self.bounds.center

    def align_left(self, child: 'BaseModule'):
        child.bounds.left = self.bounds.left

    def align_top(self, child: 'BaseModule'):
        child.bounds.top = self.bounds.top

    def align_bottom(self, child: 'BaseModule'):
        child.bounds.bottom = self.bounds.bottom

    def align_right(self, child: 'BaseModule'):
        child.bounds.right = self.bounds.right

    # following to be overridden
    def draw(self, surface):
        """To be overridden, blits the data of the component to the Surface object resets the changed parameter, and
         returns the area to be updated"""
        return self.bounds.copy()

    def draw_portion(self, surface: Surface, bounds):
        s = Surface(surface.get_size(), SRCALPHA)
        self.draw(s)
        surface.blit(s, bounds, bounds)

    def on_quit(self):
        return False

    def on_active_event(self, gain, state):
        return False

    def on_key_down(self, unicode, key, mod):
        return False

    def on_key_up(self, key, mod):
        return False

    def on_mouse_motion(self, pos, rel, buttons):
        return False

    def on_mouse_button_up(self, pos, button):
        return False

    def on_mouse_button_down(self, pos, button):
        return False

    def on_update(self):
        """ Handles user event called periodically, updates the internal state of the components independent of pygame
         events at a time interval specified at application level"""
        return False