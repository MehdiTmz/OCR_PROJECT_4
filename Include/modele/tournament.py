from .round import Round
class Tournament:

    def __init__(self, name: str = 'unknown', place: str = 'unknown',
                 date='unknown', nOfTurns : int = 4,
                 timeControls: str = 'unknown', description: str = 'unknown'):

        self.name = name
        self.place = place
        self.date = date
        self.nOfTurns = nOfTurns
        self.rounds = []
        self.players = []
        self.timeControls = timeControls
        self.description = description
        self.tournament_score = []
        #implementer 
        self.pair_list = []
    
    def create_tournament_score_list(self):

        self.players.sort(key=lambda x: x.rank, reverse=False)
        score_list = []
        for x in self.players:
            player_with_score = [x, 0]
            score_list.append(player_with_score)

        self.tournament_score = score_list
    
    def update_score_list(self):
        self.tournament_score.sort(key=lambda x: x[1], reverse=True)
        #print('Debug : test -->',[i[0] for i in self.tournament_score])
        self.players = [i[0] for i in self.tournament_score]

    def create_pair_list(self,round_1 = True):
        self.pair_list = []
        if round_1 :
            for pairs_round_1 in range(4):
                pair = []
                pair.append(self.players[pairs_round_1])
                pair.append(self.players[pairs_round_1+4])
                self.pair_list.append(pair)
        if (not round_1) :
            for pairs_round_X in range(0,8,2):
                pair = []
                pair.append(self.players[pairs_round_X])
                pair.append(self.players[pairs_round_X])
                self.pair_list.append(pair)
