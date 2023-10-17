import pygame as pg
import sys
from random import randint
pg.init()

WIN = pg.display.set_mode((800, 800))
pg.display.set_caption("Slide Puzzle")
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)


class Tile():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.img = None
        self.darken = False

    def draw(self, i, j):
        if self.darken:
            pg.draw.rect(WIN, BLACK, (self.x, self.y, 800/width, 800/height))
            pg.draw.rect(WIN, BLACK, (self.x, self.y, 800/width, 800/height), 2)
        else:
            WIN.blit(self.img, (j*(800/width), i*(800/height)))
            pg.draw.rect(WIN, BLACK, (j*(800/width), i*(800/height), 800/width, 800/height), 2)


def draw():
    WIN.fill(BLACK)

    for i, row in enumerate(tiles):
        for j, tile in enumerate(row):
            tile.draw(i, j)

    pg.display.update()


def switch(i, j):

    tile = tiles[i][j]
    if not tile.darken:
        try:
            if tiles[i-1][j].darken and i-1 >= 0:
                tiles[i][j] = tiles[i-1][j]
                tiles[i-1][j] = tile
        except IndexError:
            pass
        try:
            if tiles[i+1][j].darken:
                tiles[i][j] = tiles[i+1][j]
                tiles[i+1][j] = tile

        except IndexError:
            pass
        try:
            if tiles[i][j-1].darken and j-1 >= 0:
                tiles[i][j] = tiles[i][j-1]
                tiles[i][j-1] = tile

        except IndexError:
            pass
        try:
            if tiles[i][j+1].darken:
                tiles[i][j] = tiles[i][j+1]
                tiles[i][j+1] = tile

        except IndexError:
            pass


def scramble():
    for n in range(10000):
        i = randint(0, height-1)
        j = randint(0, width-1)
        switch(i, j)


def get_image():
    img = pg.image.load(image)
    img = pg.transform.scale(img, (800, 800))
    return img


def main():
    global tiles, solved
    clock = pg.time.Clock()

    # Setup Tiles
    tiles = []    
    X = 800/width
    Y = 800/height

    for y in range(height):
        row = []
        for x in range(width):
            tile = Tile(x*X, y*Y)
            row.append(tile)
            tile.img = get_image().subsurface(x*X, y*Y, 800/width, 800/height)

        tiles.append(row)

    tiles[-1][-1].darken = True

    scramble()

    # MAIN LOOP
    while True:
        clock.tick(FPS)

        # EVENTS
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                i = int(event.pos[1]//(800/height))
                j = int(event.pos[0]//(800/width))
                switch(i, j)

        draw()


width = 4
height = 4
image = "Kanye.png"
main()
