#import sys
#import modele.player as objP
class View :
    def __repr__(self):
         return "1"
    def __str__(self):
        return "2"
    
    def player_data():
        
        print('Please enter the data of the player : ')
        name = input('Name : ')
        firstname = input('Firstname : ')
        birthdate = input('Birthdate : ') 
        sex = input('Sex : ')
        rank = input('Rank : ')
        return [name,firstname,birthdate,sex,rank]
    
    def match_result_view():
        result = int(input('Veuillez entre le vainqueur du match (1 = Joueur1, 2 = Joueur2, 0 = Egalité) : '))
        return result
        
        
        