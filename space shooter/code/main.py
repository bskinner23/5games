import pygame
from os.path import join
import random

#general setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
running = True


# importing an image
path = join('images', 'player.png')


star_surf = pygame.image.load(join('images', 'star.png')).convert_alpha()
star_pos = []
for pos in range(0, 20):
    star_x = random.randint(0,1220)
    star_y = random.randint(0,660)
    star_pos.append((star_x, star_y))

player_surf = pygame.image.load(join('images', 'player.png')).convert_alpha()

while running:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # draw the game
    display_surface.fill('darkgray')

    
    for pos in star_pos:
        display_surface.blit(star_surf, pos)
        
    display_surface.blit(player_surf, (200,500))
    
    pygame.display.update()
    
pygame.quit()