"""Define tournament """

def comp(x):
    """order the list of player by score then by rank if they have the same score"""
    return -x[1], x[0].rank

class Tournament:
    """Tournament class
    has the attribute: name, date, numbers_of_turns, rounds, type of time control, a descrption
    additional attribute : list of player pair
    """

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

    def create_tournament_score_list(self):
        """Create the first player list with a score an sorted by rank"""
        #print(self.players)
        for player in self.players:
            self.players[self.players.index(player)] = [player, 0]
            print(player)
        self.players.sort(key=lambda x: x[0].rank, reverse=False)

    def update_score_list(self):
        """Update the player list
            sorted by score and ther by rank
        """
        #self.tournament_score.sort(key=lambda x: x[1], reverse=True)
        #print('Debug : test -->',[i[0] for i in self.tournament_score])
        #self.players = [i[0] for i in self.tournament_score]
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

                for player in self.players:
                    if len(pair) == 2:
                        break
                    if player[0] not in player_used and player[0] not in player[0].played_with:
                        pair.append(player[0])
                        player_used.append(player[0])
                    else:
                        pass

                self.pair_list.append(pair)
