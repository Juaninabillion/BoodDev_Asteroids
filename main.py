# this allows us to use code from 
# the open-source pygame library
# throughout this file

import pygame
from constants import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return       
        
        screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))    
        screen.fill((255,255,255))
        pygame.display.update()
        pygame.time.delay(10)
            
if __name__ == "__main__":
    main()
