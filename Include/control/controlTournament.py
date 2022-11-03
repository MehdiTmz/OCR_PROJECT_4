"""Define controller """
# import random
# from Include.modele.player import Player
# from Include.view.view import View
from Include.modele.match import Match
from Include.modele.round import Round
from Include.modele.tournament import Tournament
from datetime import datetime


def round_match(view, round, tournament):
    """ Function to play the match in a round"""
    match: Match

    for actual_match in range(tournament.n_of_turns):

        match_player_1 = round.list_player_pair[actual_match][0]
        match_player_2 = round.list_player_pair[actual_match][1]

        match = Match(match_player_1, match_player_2)
        result = view.input_match_result_view(match_player_1, match_player_2)

        round.list_matches.append(match.match_result(result))

        for player in tournament.players:

            if player[0] == match.player_and_score[0][0]:
                player[1] = player[1] + match.player_and_score[0][1]

            if player[0] == match.player_and_score[1][0]:
                player[1] = player[1] + match.player_and_score[1][1]

        round.serialize_round()


class ControlTournament:
    """ControlTournament Class
    has the attribute :view
    """

    def __init__(self, view):

        self.tournament = Tournament()
        self.view = view

    def get_tournament_info(self, players: list = []):
        """Get the information of the tournament"""

        tournament_info = self.view.get_tournament_info()
        self.tournament.name = tournament_info[0]
        self.tournament.place = tournament_info[1]
        self.tournament.date = tournament_info[2]
        self.tournament.time_controls = tournament_info[3]
        self.tournament.descrtipion = tournament_info[4]

        if players:
            # print("Debug : La liste des joueurs a bien été moddifiée")
            self.tournament.players = players.copy()
            self.tournament.create_tournament_score_list()

    def round_1(self, name):
        """Create round 1"""

        round: Round
        self.tournament.create_pair_list()
        round = Round(name=name, list_player_pair=self.tournament.pair_list)
        print("Debut du ", name, 'à ', round.date_round_begin)
        input_text = "Veuillez appyer sur une touche appuyer sur enter"
        input(input_text)
        round.date_round_end = datetime.today()
        round_match(self.view, round, self.tournament)
        self.tournament.rounds.append(round)

    def round_x(self, name):
        """Create other rounds"""

        self.tournament.update_score_list()
        self.tournament.create_pair_list(False)
        round: Round
        round = Round(name=name, list_player_pair=self.tournament.pair_list)
        print("Debut du ", name, 'à ', round.date_round_begin)
        input_text = "Veuillez appyer sur une touche appuyer sur enter"
        input(input_text)
        round.date_round_end = datetime.today()
        round_match(self.view, round, self.tournament)
        self.tournament.rounds.append(round)
