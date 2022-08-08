from datetime import datetime
class Tour:

    def __init__(self, name : str = 'unknown',
                 list_player_pair : list = [],
                 list_matches_result: list = []):

        self.name = name
        self.date_round_begin = datetime.today()
        self.date_round_end = None
        self.list_player_pair = list_player_pair
        self.list_matches_result = list_matches_result
