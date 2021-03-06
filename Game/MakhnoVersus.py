import sys
import os
sys.path.append(os.path.join(sys.path[0], '../'))

import pygame
from pygame.locals import *
from Game.Shared.GameConstants import *


class MakhnoVersus:
    def __init__(self):
        self.__lives = 1
        self.__score = 0

        self.__level = Level(self)
        self.__level.load(0)

        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption("Game Programming with Python & PyGame")
        self.__clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(GameConstants.SCREEN_SIZE, pygame.DOUBLEBUF, 32)
        pygame.mouse.set_visible(0)
        pscena = PlayingGameScene(self)
		self.__scenes =  (PlayingGameScene(self)
            , GameOverScene(self), HighscoreScene(self), MenuScene(self)

        self.__currentScene = 3
        self.__sounds = (pygame.mixer.Sound(GameConstants.SOUND_FILE_GAMEOVER))
		
		

    def start(self):
        while 1:
            self.__clock.tick(100)
            self.screen.fill((0, 0, 0))
            pygame.display.update()
    def changeScene(self, scene):
        self.__currentScene = scene

    def getLevel(self):
        return self.__level

    def getScore(self):
        return self.__score

    def increaseScore(self, score):
        self.__score += score

    def getLives(self):
        return self.__lives

    def getBalls(self):
        return self.__balls

    def getPad(self):
        return self.__pad

    def playSound(self, soundClip):
        sound = self.__sounds[soundClip]

        sound.stop()
        sound.play()

    def reduceLives(self):
        self.__lives -= 1

    def increaseLives(self):
        self.__lives += 1

    def reset(self):
        self.__lives = 5
        self.__score = 0
        self.__level.load(0)
		
if __name__ == "__main__":
    MakhnoVersus().start()


