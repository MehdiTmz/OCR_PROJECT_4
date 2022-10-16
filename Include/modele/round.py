"""Define a round"""

from datetime import datetime


class Round:
    """ Round Class

    data : name, date when the round begin, date when the round finish
    additional data : list of pair, list of match result
    """

    def __init__(self, name: str = 'unknown',
                 list_player_pair: list = []):

        self.name = name
        self.date_round_begin = datetime.today()
        self.date_round_end: datetime
        self.list_player_pair = list_player_pair
        self.list_matches = []

    def serialize_round(self):
        """Serialize a round"""

        serialized_round = {}
        count = 1
        for match in self.list_matches:

            serialized_round["Match" + str(count)] = {}
            player1 = {'player': match[0][0].name,
                       'score': match[0][1]}
            player2 = {'player': match[1][0].name,
                       'score': match[1][1]}
            serialized_round["Match" + str(count)]['player1'] = player1
            serialized_round["Match" + str(count)]['player2'] = player2
            count += 1

        serialized_round['name'] = self.name
        serialized_round['date_round_begin'] = str(self.date_round_begin)
        serialized_round['date_round_end'] = str(self.date_round_end)
        return serialized_round
