from Include.control.mainController import mainController
from Include.modele.player import Player
from Include.view.view import View
import random


view = View()
controller = mainController(view)


if __name__ == "__main__":

    controller.run()
