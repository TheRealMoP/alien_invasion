import sys
import pygame
from  settings import Settings
from ship import Ship

class AlienInvasion:
    """Overall game class"""
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.fullscreen = False

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien invasion")

        self.ship = Ship(self)

    def run_game(self):
        """Start the main loop"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
    
    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN: 
                self._check_key_down_events(event)
            elif event.type == pygame.KEYUP:
                self._check_key_up_events(event)

    def _check_key_down_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right= True              
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_ESCAPE:
            sys.exit()
        #elif event.key == pygame.K_f:
        #    self._toggle_fullscreen()

    def _check_key_up_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right= False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left= False

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        pygame.display.flip()

    def _toggle_fullscreen(self):
        if self.fullscreen:
            self.screen = pygame.display.set_mode(
                (self.settings.SCREEN_WIDTH, self.settings.SCREEN_HEIGHT), pygame.RESIZABLE)
            self.settings.screen_width = self.settings.SCREEN_WIDTH
            self.settings.screen_height = self.settings.SCREEN_HEIGHT
        else:
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            self.settings.screen_width = self.screen.get_rect().width
            self.settings.screen_height = self.screen.get_rect().height

        self.fullscreen = not self.fullscreen;


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()