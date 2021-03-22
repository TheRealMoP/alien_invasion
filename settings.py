class Settings:
    """Class storing all game settings"""

    def __init__(self):
        """Init game settings"""

        # Constant Values
        self.SCREEN_WIDTH = 1080
        self.SCREEN_HEIGHT = 720

        # Screen settings        
        self.screen_width = self.SCREEN_WIDTH
        self.screen_height = self.SCREEN_HEIGHT
        self.bg_color = (180, 200, 240)

        # Ship settings
        self.step_size = 1.5

        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 6
        self.bullet_height = 12
        self.bullet_color = (190, 190, 130)