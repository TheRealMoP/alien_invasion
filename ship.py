import pygame

class Ship():
    """Represents player's ship"""

    def __init__(self, ai_game):
        """Init the ship's starting position"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load ship's image
        self.image = pygame.image.load("images/ship_color_64.png")
        self.rect = self.image.get_rect()

        # Start ship at the bottom
        self.rect.midbottom = self.screen_rect.midbottom
        self.rect.bottom -= 10
        
        # Store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)

        # Movement flag
        self.moving_right = False
        self.moving_left = False

        self.game_state = ai_game.game_state

    def blitme(self):
        """Draw the ship at it's current location"""
        if self.game_state.started:
            self.screen.blit(self.image, self.rect)

    def update(self):
        """Ship's position based on movement flag"""
        border_width = 20
        if self.moving_right and self.rect.right < self.screen_rect.right - border_width:
            self.x += self.settings.step_size
        elif self.moving_left and self.rect.left > border_width:
                self.x -= self.settings.step_size

        # Update rect object from self.x.
        self.rect.x = self.x