import pygame
import random
import os
import Core.Main as Main

pygame.font.init()
print(os.curdir)
Content = Main.CoreDirectory+"\\Content\\"

Font = pygame.font.SysFont("Times New Roman", 18, 2, 0)
BigFont = pygame.font.SysFont("Times New Roman", 36, 2, 0)
Background1 = pygame.image.load(Content+"Background1.png")
PB1 = pygame.image.load(Content+"PlayButton1.png")
PB2 = pygame.image.load(Content+"PlayButton2.png")

def PromptMenu (Game):

    while Game.Running:

        MouseX, MouseY = Game.GetMousePosition()

        Game.Display.fill( (0, 0, 0 ) )

        Game.Display.blit(Background1, (13, 21))
        Header = Font.render("Main Menu : Build 0", 1, (255, 255, 255), None)
        Game.Display.blit(Font.render("Main Menu : Build 0", 1, (0, 0, 0), None), (21, 37))
        Game.Display.blit(Header, (20, 36))

        Game.Display.blit(BigFont.render("Play", 1, (255,255,255), None), (76, 106))

        PBToBlit = PB1
        if MouseX > 8 and MouseX < 72:
            if MouseY > 96 and MouseY < 160:
                PBToBlit = PB2

        Game.Display.blit(PBToBlit, (8, 96))

        Game.OnUpdate()
        for event in Game.Events():

            if event.type == pygame.QUIT:
                Game.Running = False
                print("User exited in menu prompt!")

            if event.type == pygame.MOUSEBUTTONDOWN:
                print(event)
                if event.button == 1 and PBToBlit == PB2:
                    return "prompt-play"

