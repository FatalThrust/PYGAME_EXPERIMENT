import pygame
import random
import Core.Meta.Menu as Menu
import time
import os
import Core.World.Map as Map
CoreDirectory = os.getcwd()[:35]

class Humanoid ():

    def __init__(self, x, y):
        self.x = x
        self.y = y

class Player (Humanoid):

    def __init__(self, x, y):
        super().__init__(x, y)

if __name__ == "__main__":
    pygame.init()


    class Game():

        Display = pygame.display.set_mode( (640, 640) )

        @classmethod
        def Update (cls):
            pygame.display.flip()

        @classmethod
        def UpdateRegion (cls, rect):
            pygame.display.update(rect)

        @classmethod
        def Events (cls):
            return pygame.event.get()

        def GetPressedKeys (self):
            return pygame.key.get_pressed()

        def GetMouseButtonsPressed (self):
            return pygame.mouse.get_pressed()

        def MouseFocused (self):
            return pygame.mouse.get_focused()

        def GetMousePosition (self):
            return pygame.mouse.get_pos()

        def __init__(self):
            self.GameEvents = []
            self.PyEvents = []

            self.Running = False

            self.MousePosition = self.GetMousePosition()
            self.Keys = self.GetPressedKeys()

            self.InternalClockLast = time.time()
            self.InternalClockNew = time.time()
            self.DeltaTime = 0

        def Run (self):

            self.Running = True
            while self.Running:

                Selection = Menu.PromptMenu(self)

                if Selection == "prompt-play":
                    world = Map.TileCache(self)
                    Grasses = []
                    for i in range(3):
                        Grasses.append(pygame.image.load(CoreDirectory + "\\Content\\Grass"+str(i+1)+".png"))

                    for x in range(32):
                        for y in range(32):
                            tile = Map.Tile(x, y)
                            tile.CachedImages.append(Grasses[0])
                            tile.CachedImages.append(Grasses[1])
                            tile.CachedImages.append(Grasses[2])
                            world.AllExistingTiles.append(tile)

                    player = Player(random.randint(0, 32), random.randint(0, 32))
                    while self.Running:
                        Game.Display.fill( (255,255,255) )

                        world.Draw(Game.Display, [player.x, player.y])

                        for event in Game.Events():
                            if event.type == pygame.QUIT:
                                self.Running = False

                        self.OnUpdate()

            pygame.quit()

        def OnUpdate (self):
            self.InternalClockNew = time.time()
            self.DeltaTime = self.InternalClockNew - self.InternalClockLast
            self.InternalClockLast = self.InternalClockNew
            Game.Update()

    Session = Game()
    Session.Run()