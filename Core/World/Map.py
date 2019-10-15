import pygame
import random

#pygame should be initialized already

class Position ():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def Increment (self, i, weight):
        if i < 0 or i > 1:
            i = 0

        if i == 0:
            self.x = self.x + weight
        else:
            self.y = self.y + weight

    def Change (self, DeltaTime, i, weight):
        if i < 0 or i > 1:
            i = 0

        if i == 0:
            self.x = self.x + (weight * DeltaTime)
        else:
            self.y = self.y + (weight * DeltaTime)

class Tile (Position):

    def __init__(self, x ,y, proximityRadius = 0):
        super().__init__(x, y)

        self.CachedImages = []
        self.AnimationCount = 0

        self.AnimationTransitionTime = 3 # .3s between each animation  change
        self.AnimationTick = 0

        self.Proximity = [] # Other tiles near by
        self.ProximityRadius = proximityRadius or 0

        self.RelativePositionToWorld = Position(self.x * 32, self.y * 32)


    def Update (self, DeltaTime):

        if len(self.CachedImages) >= 2:
            self.AnimationTick = self.AnimationTick + DeltaTime
            if self.AnimationTick  >= self.AnimationTransitionTime:
                self.AnimationTick = 0
                self.AnimationCount = self.AnimationCount + 1

                if self.AnimationCount >= len(self.CachedImages):
                    self.AnimationCount = 0

                print("Animation Update")

class TileCache ():

    AllExistingTiles = [] # all tiles can be found here

    def __init__(self, Game):
        self.Cache = [] # Tiles in render distance are put here
        self.Gache = [] # Tiles not in render distance are put here
        self.Game = Game

    def Draw (self, Window, PositionOffset):


        for tile in self.Cache:
            print("t")

            if len(tile.CachedImages) == 0:
                pygame.draw.rect(Window, (
                    random.randint(0, 100),
                    random.randint(0, 100),
                    random.randint(0, 100)),
                    (tile.x * 32 - (PositionOffset[0]),
                     tile.y * 32 - (PositionOffset[1]),
                     32,
                     32
                     ))
            elif len(tile.CachedImages) >= 1:
                self.Game.Display.blit(tile.CachedImages[tile.AnimationCount], (tile.x * 32 - (PositionOffset[0]),
                                                              tile.y * 32 - (PositionOffset[1])))

        pygame.display.flip()
        self.Update(PositionOffset)




    def Update (self, RelativePlayerPosition):

        self.Cache = []
        self.Gache = []
        # Update gache/cache #

        for tile in TileCache.AllExistingTiles:
            tile.Update(self.Game.DeltaTime)
            if tile.RelativePositionToWorld.x + RelativePlayerPosition[0] < -31 or tile.RelativePositionToWorld.x + RelativePlayerPosition[0] > 640:
                self.Gache.append(tile)
                print("Gached")
            elif tile.RelativePositionToWorld.y + RelativePlayerPosition[1] < -31 or tile.RelativePositionToWorld.y + RelativePlayerPosition[1] > 640:
                print("Gached")
                self.Gache.append(tile)
            else:
                self.Cache.append(tile)


    def CheckCache (self, p):

        for cache in self.Cache:

            if cache.x == p[0] and cache.y == p[1]:
                return cache

        return None

    def CheckGache (self, p):

        for gache in self.Gache:

            if gache.x == p[0] and gache.y == [1]:
                return gache

        return None


