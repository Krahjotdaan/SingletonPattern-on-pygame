import pygame as pg


class Game:
    instance = None

    def __init__(self):
        if Game.instance is not None:
            raise ReferenceError("Вы пытаетесь создать второе окно")
        else:
            Game.instance = self

        pg.init()
        self.screen = pg.display.set_mode((800, 600))
        self.clock = pg.time.Clock()
        self.flag = True
        self.obj = Object(200, 300)

    @staticmethod
    def get():
        if not Game.instance:
            Game()
        
        return Game.instance
    
    def play(self):
        while self.flag:
            self.clock.tick(30)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.flag = False

            self.obj.draw()
                
            pg.display.update()


class Object:
    def __init__(self, x, y):
        self.rect = (x, y, 200, 300)

    def draw(self):
        pg.draw.rect(Game.get().screen, (255, 255, 255), self.rect)

# game = Game()
game = Game.get()
game = Game.get()
game = Game.get()
game.play()
        