"""Define tournament """

from os import name


def comp(player_to_order):
    """order the list of player by score then by rank if they have the same score"""
    return -player_to_order[1], player_to_order[0].rank

class Tournament:
    """Tournament class
    has the attribute: name, date, numbers_of_turns, rounds, type of time control, a descrption
    additional attribute : list of player pair
    """
    def __repr__(self):

        return self.name + ' - Lieu : ' + str(self.place) + ' - Date : ' + str(self.date)

    def __str__(self):

        return self.name + ' - Lieu : ' + str(self.place) + ' - Date : ' + str(self.date)

    def __init__(self, name: str = 'unknown', place: str = 'unknown',
                 date='unknown', n_of_turns : int = 4,
                 time_controls: str = 'unknown', description: str = 'unknown'):

        self.name = name
        self.place = place
        self.date = date
        self.n_of_turns =  n_of_turns
        self.rounds = []
        self.players = []
        self.time_controls = time_controls
        self.description = description
        self.pair_list = []
        self.serialized_tournament = {}

    def create_tournament_score_list(self):
        """Create the first player list with a score an sorted by rank"""
        #print(self.players)
        for player in self.players:
            self.players[self.players.index(player)] = [player, 0]
            #print(player)
        self.players.sort(key=lambda x: x[0].rank, reverse=False)

    def update_score_list(self):
        """Update the player list
            sorted by score and ther by rank
        """
        self.players.sort(key = comp)

    def create_pair_list(self,round_1 = True):
        """create the pair list for rounds based on swiss system"""

        self.pair_list = []

        if round_1 :
            for pairs_round_1 in range(4):

                pair = []
                pair.append(self.players[pairs_round_1][0])
                pair.append(self.players[pairs_round_1+4][0])
                self.pair_list.append(pair)

        if not round_1 :

            player_used = []

            while len(self.pair_list)<4:

                pair = []
                #print(player_used)
                for player in self.players:

                    # if player[0] not in player_used and player[0] not in player[0].played_with:
                    #     print(player[0].name, 'Already played with', player[0].played_with)
                    #     pair.append(player[0])
                    #     player_used.append(player[0])
                    if len(pair) == 0:
                        if player[0] not in player_used:
                            pair.append(player[0])
                            player_used.append(player[0])
                    if len(pair) == 1:
                        if pair[0] not in player[0].played_with and pair[0] != player[0] and player[0] not in player_used:
                            # if (pair[0] != player[0]):
                            #     print(player[0])
                            pair.append(player[0])
                            player_used.append(player[0])
                    if len(pair) == 2:
                        break

                self.pair_list.append(pair)
                print(self.pair_list)

    def serialize_tournament(self,players):
        """Serialization of the tournament data"""
        self.serialized_tournament['name'] = self.name
        self.serialized_tournament['date'] = self.date
        self.serialized_tournament['place'] = self.place
        self.serialized_tournament['rounds'] = self.rounds
        self.serialized_tournament['players'] = players
        self.serialized_tournament['time_controls'] = self.time_controls
        self.serialized_tournament['description'] = self.description
