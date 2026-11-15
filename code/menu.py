#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
import pygame.image
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface

from code.const import WIN_WIDTH, TITLE_COLOR, MENU_OPTION, COLOR_WHITE, COLOR_YELLOW


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png').convert_alpha() # Load image
        self.rect = self.surf.get_rect() # Create rectangle

    def run(self):
        menu_option = 0
        pygame.mixer_music.load('./asset/Menu.mp3') # Load music
        pygame.mixer_music.play(-1) # play music (-1 = loop)

        while True:
            self.window.blit(source=self.surf, dest=self.rect) # Draw image
            self.menu_text(60, "Mountain", TITLE_COLOR, ((WIN_WIDTH / 2), 70))
            self.menu_text(60, "Shooter", TITLE_COLOR, ((WIN_WIDTH / 2), 120))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(30, MENU_OPTION[i], COLOR_YELLOW, ((WIN_WIDTH / 2), 200 + 25 * i))
                else:
                    self.menu_text(30, MENU_OPTION[i] , COLOR_WHITE, ((WIN_WIDTH / 2), 200 + 25 * i))

            pygame.display.flip() # Update display

            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() # Close window
                    quit()  # End pygame
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN: # Down Key
                       if menu_option < len(MENU_OPTION) - 1:
                           menu_option += 1
                       else:
                           menu_option = 0
                    if event.key == pygame.K_UP: # Up Key
                       if menu_option > 0:
                           menu_option -= 1
                       else:
                           menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN: # ENTER
                        return MENU_OPTION[menu_option]

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)