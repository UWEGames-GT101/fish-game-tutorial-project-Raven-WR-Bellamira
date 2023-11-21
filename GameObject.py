import pyasge
import math


class GameObject:

    def __init__(self):
        self.sprite = pyasge.Sprite()
        self.move_direction = [0.0, 0.0]


class Asteroid(GameObject):

    def __init__(self):
        super().__init__()
        self.move_speed = 0

    def Move(self):
        self.sprite.x += self.move_direction[0] * self.move_speed
        self.sprite.y += self.move_direction[1] * self.move_speed


class Ship(GameObject):
    def __init__(self):
        super().__init__()
        self.move_speed = 0.0
        self.collisionSprite = pyasge.Sprite()


    def Move(self):
        self.sprite.x += self.move_direction[0] * self.move_speed
        self.sprite.y += self.move_direction[1] * self.move_speed
        self.collisionSprite.x += self.move_direction[0] * self.move_speed
        self.collisionSprite.y += self.move_direction[1] * self.move_speed
        pass


class Projectile(GameObject):

    def __init__(self):
        super(Projectile, self).__init__()

    def Move(self):
        pass