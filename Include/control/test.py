from mainController import mainController
from Include.modele.player import Player
from Include.view.view import View
import random



RANK = [
    1, 2, 3, 4, 5, 6, 7, 8
]

random.shuffle(RANK)

STATIC_LIST_PLAYER = [
                        Player('player'+str(1), 'name', 'test', 'H', RANK[0]),
                        Player('player'+str(2), 'name', 'test', 'H', RANK[1]),
                        Player('player'+str(3), 'name', 'test', 'H', RANK[2]),
                        Player('player'+str(4), 'name', 'test', 'H', RANK[3]),
                        Player('player'+str(5), 'name', 'test', 'H', RANK[4]),
                        Player('player'+str(6), 'name', 'test', 'H', RANK[5]),
                        Player('player'+str(7), 'name', 'test', 'H', RANK[6]),
                        Player('player'+str(8), 'name', 'test', 'H', RANK[7])]
# view = View()
# main = mainController(view)
# main.run()
while True:
    user_input = input("Enter something:")

    if user_input.isnumeric():
        print("Is a number")
    else:
        print("Not a number")
