import pygame

import game as gamelib

game = gamelib.Game()
game.run()

results = game.quit()

print("Score : " + str(results[0]) + "\n" +
      "Max achievable : " + str(results[1]) + "\n"
      "Time : " + str(results[2]) + "sec" + "\n")