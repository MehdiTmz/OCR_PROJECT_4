def set_match_score(state):
    if (state == 1):

        score1 = 1
        score2 = 0

    elif (state == 2):

        score1 = 0
        score2 = 1

    else:

        score1 = 0.5
        score2 = 0.5
    
    return score1, score2

class Match:

    def __init__(self, player1, player2):

        self.player1 = player1
        self.player2 = player2
        self.player_and_score = []

    def match_result(self, state):

        score = set_match_score(state)
        result = [[self.player1, score[0]], [self.player2, score[1]]]
        self.player_and_score = result.copy()
        return (result[0], result[1])
 
