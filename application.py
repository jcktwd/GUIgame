from pygame import *
from colours import *
from custom_events import *
from pygame.constants import *
from modules.BaseModule import *


class Application():

    def __init__(self):
        pygame.init()
        self.target_fps = 120
        self.ms_update_frequency = 10
        self.clock = pygame.time.Clock()
        displayInfo = pygame.display.Info()
        w, h = displayInfo.current_w, displayInfo.current_h
        self.screen = pygame.display.set_mode((w, h), HWACCEL|DOUBLEBUF|FULLSCREEN)
        pygame.time.set_timer(UPDATE, self.ms_update_frequency)
        self.modules = []
        self.stopRunning = False

    def addModule(self, module):
        self.modules.append(module)
        self.modules.sort(key=lambda module: module.z)

    def addModules(self, *modules):
        for module in modules:
            self.addModule(module)

    def stop(self):
        self.stopRunning = True

    def minimise(self):
        pygame.display.iconify()

    def draw_all(self):
        self.screen.fill(BLACK)
        for module in self.modules:
            module.draw(self.screen)
        pygame.display.update()

    # def draw_behind(self, module: BaseModule, area):
    #     for other_module in (mod for mod in self.modules if mod.z < module.z):
    #         if other_module.bounds.colliderect(area):
    #             if other_module.transparent:
    #                 self.draw_behind(other_module, other_module.bounds.clip(area))
    #             other_module.draw_portion(self.screen, other_module.bounds.clip(area))

    def draw_behind(self, z:int, area:Rect):
        for module in self.modules:
            if module.z < z:
                if module.bounds.colliderect(area):
                    module.draw_portion(self.screen, module.bounds.clip(area))
            else:
                break



    def run(self):
        while not self.stopRunning:
            for event in pygame.event.get():
                for module in self.modules:
                    module.dispatch(event)

                # handle exit events
                if event.type == KEYDOWN and (event.key == K_q or event.key == K_ESCAPE):
                    self.stop()

            dirtyRects = []
            for module in self.modules:
                if module.changed or module.bounds.collidelistall(dirtyRects):
                    if module.transparent:
                        self.draw_behind(module.z, module.bounds)
                    else:
                        self.screen.fill(BLACK, module.bounds)
                    dirtyRects.append(module.draw(self.screen))
                    module.reset()

            pygame.display.update(dirtyRects)

            self.clock.tick(self.target_fps)
        pygame.quit()