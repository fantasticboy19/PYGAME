import pygame as pg
from pygame.math import Vector2 as vec

Width = 800
Height = 600
Fps = 30

# color
White = (255, 255, 255)
Black = (0, 0, 0)
Red = (255, 0, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)


class platforms(pg.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(Green)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Player(pg.sprite.Sprite):
    def __init__(self, game=None):
        # super(pg.sprite.Sprite, self).__init__()
        # self.game =game
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((50, 50))
        self.image.fill(Green)
        self.rect = self.image.get_rect()
        self.rect.center = (Width // 2, Height // 2)
        # self.vx = 0
        # self.vy = 0
        self.pos = vec(Width // 2, Height // 2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def jump(self):
        self.rect.x += 1
        hits = pg.sprite.spritecollide(self, platfs, False)
        self.rect.x -= 1
        if hits:
            self.vel.y = -20

    def update(self, *args):
        self.acc = vec(0, 0.5)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.acc.x = -0.5
        if keys[pg.K_RIGHT]:
            self.acc.x = 0.5
        # if self.rect.left > Width:
        #     self.rect.left = 0
        # elif self.rect.right < 0:
        #     self.rect.right = Width
        self.acc += self.vel * (-0.12)
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        if self.pos.x > Width:
            self.pos.x = 0
        elif self.pos.x < 0:
            self.pos.x = Width
        self.rect.midbottom = self.pos


pg.init()
pg.mixer.init()
screen = pg.display.set_mode((Width, Height))
pg.display.set_caption('My Game')
clock = pg.time.Clock()

all_sprites = pg.sprite.Group()
platfs = pg.sprite.Group()

player = Player()
all_sprites.add(player)

p1 = platforms(0, Height - 40, Width, 40)
platfs.add(p1)
all_sprites.add(p1)

p2 = platforms(Width // 2 - 50, Height * 3 / 4, 100, 20)
platfs.add(p2)
all_sprites.add(p2)

running = True
while running:
    # keep loop running at the right speed
    clock.tick(Fps)
    # process these events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                player.jump()
    # update
    all_sprites.update()
    hits = pg.sprite.spritecollide(player, platfs, False)
    if hits:
        player.pos.y = hits[0].rect.top
        player.vel.y = 0
    # draw / render
    screen.fill(Black)
    all_sprites.draw(screen)
    # after drawing ,flip the display
    pg.display.flip()
pg.quit()

