import sys
import pygame
import time
import threading
from  settings import Settings
from ship import Ship
from splash import Splash
from bullet import Bullet
from hint import Hint
from screen_operations import render_image_centered, render_text
import strings

class AlienInvasion:
    """Overall game class"""
    def __init__(self):
        pygame.init()

        self.settings = Settings()
        self.game_state = GameState()
        self.fullscreen = False

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Peace-Death")

        self.ship = Ship(self)
        self.splash = Splash(self)
        self.bullets = pygame.sprite.Group()
        self.hint = Hint(self)
        
        self.current_hint = self.hint.get_current_hint()
        
        # Media
        self.pew_sound = pygame.mixer.Sound("sounds/pew.wav")
        self.exit_sound = pygame.mixer.Sound("sounds/exit_sound.wav")

    def run_game(self):
        """Start the main loop"""
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_screen()
    
    def _welcome_message(self):
        self.hint.display_text_centered(strings.WELCOME_FIRST_LINE, -32, 48, (100, 100, 150))
        self.hint.display_text_centered(strings.WELCOME_SECOND_LINE, 32, 64, (150, 100, 100))
    
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
        elif event.key == pygame.K_RETURN:
            self.game_state.started = True
        elif event.key == pygame.K_ESCAPE:
            self._exit_game()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_TAB:
            self.current_hint = self.hint.get_current_hint(1)


        #elif event.key == pygame.K_f:
        #    self._toggle_fullscreen()

    def _exit_game(self):
        self.game_state.running = False
        self.game_state.started = False
        self._update_screen()
        self.exit_sound.play()
        render_image_centered(self.screen, "images/exit_splash.png", 2)
        sys.exit()

    def _check_key_up_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right= False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left= False

    def _fire_bullet(self):
        if not self.game_state.started:
            return

        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)
        self._splash()
        self.pew_sound.play()

    def _splash(self):
        event = threading.Event()
        thread = threading.Thread(target=self.splash_timer, args=(event,))
        thread.start()

    def splash_timer(self, event, seconds = 0.3):
        self.splash.visible = True
        event.wait(seconds)
        self.splash.visible = False

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        self.splash.blitme(self.ship.rect)
        for bullet in self.bullets:
            bullet.draw_bullet()

        self.hint.display_text(self.current_hint, 20, 20)

        if not self.game_state.started and self.game_state.running:
            self._welcome_message()

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


class GameState():
    def __init__(self):
        self.running = True
        self.started = False

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()