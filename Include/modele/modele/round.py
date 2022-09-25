"""Define a round"""

from datetime import datetime

class Round:
    """ Round Class

    data of a round: name, date when the round begin, date when the round finish
    additional data : list of pair, list of match result 
    """

    def __init__(self, name : str = 'unknown',
                 list_player_pair : list = []):

        self.name = name
        self.date_round_begin = datetime.today()
        self.date_round_end : datetime
        self.list_player_pair = list_player_pair
        self.list_matches_result = []