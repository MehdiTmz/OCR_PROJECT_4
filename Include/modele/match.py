"""Define a match"""


def set_match_score(state):
    """give a score according to the input given by user"""
    if state == 1:

        score1 = 1.0
        score2 = 0.0

    elif state == 2:

        score1 = 0.0
        score2 = 1.0

    else:
        score1 = 0.5
        score2 = 0.5

    return score1, score2


class Match:
    """ Match class
    has a two player as attribute
    """
    def __init__(self, player1, player2):

        self.player1 = player1
        self.player2 = player2
        self.player_and_score = []

    def match_result(self, state):
        """Return a tuple with players and their result"""

        score = set_match_score(state)
        result = [[self.player1, score[0]], [self.player2, score[1]]]
        self.player_and_score = result.copy()
        self.player1.played_with.append(self.player2)
        self.player2.played_with.append(self.player1)
        return (result[0], result[1])

    def serialize_match(self):
        """ Return a serialized match"""

        player1 = self.player1.serial_player()
        player2 = self.player2.serial_player()
        serialized_match = {}
        serialized_match['players'] = player1, player2
        serialized_match['scores'] = {
                                        'score1': self.player_and_score[0][1],
                                        'score2': self.player_and_score[1][1]
                                        }
        return serialized_match
