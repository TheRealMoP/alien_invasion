import pygame
import time

def render_image(screen, img_path, image = None, rect = None):
    if image == None: 
        image = pygame.image.load(img_path)

    if rect == None:
        rect = image.get_rect()
        rect.left = left
        rect.top = top

    screen.blit(image, rect)

def render_image_centered(screen, img_path, waiting_time = 1):
    image = pygame.image.load(img_path)
    rect = image.get_rect()
    rect.center = screen.get_rect().center
    render_image(screen, img_path, image, rect)
    pygame.display.flip()
    time.sleep(waiting_time)

def render_text(screen, text, positon = (0, 0), font_size = 24, color = (0, 0, 0), font_name = 'Times New Roman'):
    font = pygame.font.SysFont(font_name, font_size)
    pygame.font.init()
    surface = font.render(text, False, color)
    screen.blit(surface, positon)