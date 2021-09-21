import pygame
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Space Game")
WHITE = (255,255,255)
BLACK = (0,0,0)

def redraw_window():
    WIN.fill(WHITE)
    pygame.display.update()

def main():

    run = True
    while run:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        redraw_window()

    
    pygame.quit()