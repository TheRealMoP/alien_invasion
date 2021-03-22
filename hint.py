import pygame
import ressources

class Hint():
    """Displays hints on screen"""

    def __init__(self, ai_game):

        self.DEFAULT_FONT_NAME = 'Times New Roman';
        self.DEFAULT_FONT_SIZE = 32;
        self.DEFAULT_TEXT_COLOR = (40, 100, 160)
        self.DEFAULT_FONT = pygame.font.SysFont(self.DEFAULT_FONT_NAME, self.DEFAULT_FONT_SIZE)
        
        self.modified_font = None
        self.screen = ai_game.screen;

        self.hints = ressources.Ressources().hints
        self.current_hint_idx = 0        

    def _init_font(self, font_name = None, font_size = None):
        if font_name == None:
            font_name = self.DEFAULT_FONT_NAME

        if font_size == None:
            font_size = self.DEFAULT_FONT_SIZE

        return pygame.font.SysFont(font_name, font_size)


    def display_text(self, text, x, y):
        surface = self.DEFAULT_FONT.render(text, True, self.DEFAULT_TEXT_COLOR)
        self.screen.blit(surface, (x, y))

    def display_text_centered(self, text, y_offset = 0, font_size = None, text_color = None):
        if text_color == None:
            text_color = self.DEFAULT_TEXT_COLOR

        if font_size != None:
            self.modified_font = self._init_font(None, font_size)

        text_surface = self.modified_font.render(text, True, text_color)
        screen_center = (self.screen.get_rect().center[0], self.screen.get_rect().center[1] + y_offset)        
        self.screen.blit(text_surface, text_surface.get_rect(center=screen_center))


    def set_font(self, font, size):
        self.DEFAULT_FONT = pygame.font.SysFont(font, size)
        pygame.font.init()

    def get_current_hint(self, increment = 0):
        """
          Returns current hint due to saved index
          If increment is greater 0, the new current hint will be set before return
        """
        self.current_hint_idx += increment
        if increment > 0 and self.current_hint_idx + 1 > len(self.hints):
            self.current_hint_idx = 0

        return self.hints[self.current_hint_idx].rstrip()