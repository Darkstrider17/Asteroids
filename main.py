import pygame
import sys
from constants import *
from player import *
from circleshape import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, PLAYER_RADIUS, shots)
    asteroid_field = AsteroidField()

    while True:
        dt = clock.tick(60) / 1000  # limits the framerate to 60 fps

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill((0,0,0))
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game Over!")
                sys.exit(0)

        for shot in shots:
            shot.draw(screen)
        
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()
        

if __name__ == "__main__":
    main()
