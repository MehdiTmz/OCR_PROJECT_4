from datetime import datetime
class Round:

    def __init__(self, name : str = 'unknown',
                 list_player_pair : list = []):

        self.name = name
        self.date_round_begin = datetime.today()
        self.date_round_end : datetime
        self.list_player_pair = list_player_pair
        self.list_matches_result = []
