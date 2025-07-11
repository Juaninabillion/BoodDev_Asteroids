# this allows us to use code from 
# the open-source pygame library
# throughout this file
import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT)) 

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids,updateable,drawable)
    AsteroidField.containers = (updateable)
    asteroid_field = AsteroidField()
    Shot.containers = (updateable,drawable,shots)
    
    Player.containers = (updateable, drawable)
    
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    
    dt = 0
   
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return      
        updateable.update(dt)
        screen.fill("black")

        for u in asteroids:
            if u.collides_with(player):
                print("you died")
                sys.exit()
            for shot in shots:
                if u.collides_with(shot):
                    shot.kill()
                    u.split()

        for d in drawable:
            d.draw(screen)

        
        pygame.display.flip()
        dt = clock.tick(60) / 1000
            
if __name__ == "__main__":
    main()
