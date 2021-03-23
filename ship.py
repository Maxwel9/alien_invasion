import pygame

class Ship:
    """A class to manage the ship."""
    
    def __init__(self, ai_game):
        """Initialize the ship and set itsstarting position."""
        self.screen = ai_game.screen.get_rect()

        # Load the ship image and get its react.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()