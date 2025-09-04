import pygame
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN
from circleshape import CircleShape
from shot import Shot

class Player(CircleShape, pygame.sprite.Sprite):
    containers = () # set by main
    def __init__(self, x, y, radius, shots):
        pygame.sprite.Sprite.__init__(self)
        CircleShape.__init__(self, x, y, radius)
        self.rotation = 0
        self.shoot_timer = 0.0
        self.shots = shots
        self.add(*self.containers)
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, (255,255,255), self.triangle(), 2) 

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def update(self, dt):
        if self.shoot_timer > 0:
            self.shoot_timer -= dt

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.shoot_timer > 0:
            return
        direction = pygame.Vector2(0, 1).rotate(self.rotation)
        velocity = direction * PLAYER_SHOOT_SPEED

        shot = Shot(self.position.x, self.position.y)
        shot.velocity = velocity
        self.shots.add(shot)
        self.shoot_timer = PLAYER_SHOOT_COOLDOWN

        