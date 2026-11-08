import pygame

from code.const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.level import Level
from code.menu import Menu


#!/usr/bin/python
# -*- coding: utf-8 -*-

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))
        self.menu = Menu(self.window)


    def run(self):
        menu_return = self.menu.run() # MENU_OPTION return

        if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
            level = Level(self.window, "Level1", menu_return)
            level_return = level.run()
        if menu_return == MENU_OPTION[3]:
            pass
        if menu_return == MENU_OPTION[4]:
            pygame.quit()
            quit()

