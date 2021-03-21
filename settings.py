class Settings:
    """Class storing all game settings"""

    def __init__(self):
        """Init game settings"""

        # Constant Values
        self.SCREEN_WIDTH = 1200
        self.SCREEN_HEIGHT = 800

        # Screen settings        
        self.screen_width = self.SCREEN_WIDTH
        self.screen_height = self.SCREEN_HEIGHT
        self.bg_color = (210, 220, 230)

        # Ship settings
        self.step_size = 1.5

        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (220, 150, 100)