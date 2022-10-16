from Include.modele.player import Player
from Include.modele.match import Match
from Include.modele.round import Round
from Include.modele.tournament import Tournament
from datetime import datetime
from Include.view.view import View
import random


def round_match(round,tournament):
    match : Match
    #changer les x,y,etc avec des nomns claire + ne pas mettre directement des chiffres/nombres dans le code
    for x in range(4):
        result = random.randint(0,2)
        print(result)
        match = Match(round.list_player_pair[x][0],round.list_player_pair[x][1])
        print('Veuillez entrez le resultat du match entre ', match.player1,' et ', match.player2, ': ')
        round.list_matches_result.append(match.match_result(result))

        for y in tournament.tournament_score:

            if y[0] == match.player_and_score[0][0]:
                y[1] = y[1] + match.player_and_score[0][1]
            if y[0] == match.player_and_score[1][0]:
                y[1] = y[1] + match.player_and_score[1][1]

    print(tournament.tournament_score)

class CreateTournamentMenu:
    """CreateTournamentMenu class """

    def __init__(self,view):

        self.tournament = Tournament()
        self.view = view

    def get_tournament_info(self, players : list = []):
        """Get the information needed to create a new tournament"""

        self.tournament.name = self.view.get_tournament_info()

        if players:
            print("Debug : La liste des joueurs a bien été moddifiée")
            self.tournament.players = players
            self.tournament.create_tournament_score_list()

    def round_1(self,name):
        """Create the first round of the tournament"""

        round : Round
        self.tournament.create_pair_list()
        round = Round(name=name,list_player_pair=self.tournament.pair_list)
        print("Debut du ", name, 'à ', round.date_round_begin)
        input("Veuillez appyer sur une touche 'enter' quand le round est terminé. ")
        round.date_round_end = datetime.today()
        round_match(round,self.tournament)

    def round_x(self, name):
        """Create a new round (not the first one)"""

        self.tournament.update_score_list()
        self.tournament.create_pair_list(False)
        print( 'Debug --> List des score :')
        round : Round
        round = Round(name=name,list_player_pair=self.tournament.pair_list)
        print("Debut du ", name, 'à ', round.date_round_begin)
        input("Veuillez appuyer sur une touche 'enter' quand le round est terminé. ")
        round.date_round_end = datetime.today()
        round_match(round,self.tournament)
            