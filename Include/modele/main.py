import player as objP
import tournament as objT

#play = objP.Player(1,1,1,1,2)
play = objP.Player(input('Please enter the Name of the player : '),
                    input('Please enter the Surname of the player :'),
                    input('Please enter the Birthdate of the player :'),
                    input('Please enter the Sex of the player :'),
                    input('Please enter the Rank of the player :'))
print(play.rank)