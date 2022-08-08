class Match:

    def __init__(self, player1, player2):

        self.player1 = player1
        self.player2 = player2

    def match_result(self, state):

        if (state == 1):

            score1 = 1
            score2 = 0

        elif (state == 2):

            score1 = 0
            score2 = 1

        else:

            score1 = 0.5
            score2 = 0.5

        return ([self.player1, score1], [self.player2, score2])
