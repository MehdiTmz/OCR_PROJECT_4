"""Define the players"""

class Player:
    """Player Class.
    has the followings attributes : name,fisrtname,brithdate,sex,rank.
    two additional atrributes: list of the player already met, dictionnary of serialized data.
    """

    def __repr__(self):

        return self.name + ' (Rang : ' + str(self.rank) + ')'

    def __str__(self):

        return self.name + ' (Rang : ' + str(self.rank) + ')'

    def __init__(self, name: str ='unknown', firstname: str ='unknown',
                 birthdate: str ='unknown', sex: str ='unknown', rank: int = 0):

        self.name = name
        self.firstname = firstname
        self.birthdate = birthdate
        self.sex = sex
        self.rank = rank
        self.played_with = []

    def serial_player(self):
        """Serialization of the player data"""
        serialized_player = {}
        serialized_player['name'] =  self.name
        serialized_player['firstname'] =  self.firstname
        serialized_player['birthdate'] = self.birthdate
        serialized_player['sex'] = self.sex
        serialized_player['rank'] = self.rank

        return serialized_player
