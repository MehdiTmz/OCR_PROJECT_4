from Include.modele.player import Player
START_MENU_TEXT = {
    'Description': 'Bienvenue dans le menu principale',
    'Option1' : "1 : Créez un tournoi",
    'Option2' : "2 : Changer le rang d'un joueur",
    'Option3' : "3 : Quittez",
    'MessageInput' : "Veuillez entrer le numéro de l'option que vous désiré choisir :"
}
def print_menu(message_dict):
    for k in message_dict.keys():
        print(message_dict[k])
class View :

    def player_input_view(self):

        print('Please enter the data of the player : ')
        name = input('Name : ')
        firstname = input('Firstname : ')
        birthdate = input('Birthdate : ') 
        sex = input('Sex : ')
        rank = int(input('Rank : '))
        return Player(name,firstname,birthdate,sex,rank)
    
    def match_result_view(self):

        result = int(input('Veuillez entre le vainqueur du match (1 = Joueur1, 2 = Joueur2, 0 = Egalité) : '))
        return result
    
    def start_menu_display(self):
        print_menu(START_MENU_TEXT)
    
    def get_tournament_info(self):
        name_tournament = input('Please enter the name of the tournament')
        return name_tournament

