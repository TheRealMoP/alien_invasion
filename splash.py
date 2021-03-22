import pygame

class Splash(object):
    """Represents the splash while shooting"""
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.game_state = ai_game.game_state
        self.visible = False

        # Load splash image
        self.image = pygame.image.load("images/splash_mod_48.png")
        self.rect = self.image.get_rect()

    def blitme(self, ship_rect):
        """Draw the splash at it's current location"""
        if self.game_state.started and self.visible:
            self.rect.left = ship_rect.left + ship_rect.width / 2 - self.rect.width / 2 + 4
            self.rect.bottom = ship_rect.top
            self.screen.blit(self.image, self.rect)