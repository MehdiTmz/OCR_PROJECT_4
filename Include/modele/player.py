class Player:

    def __repr__(self):

         return self.name

    def __str__(self):

        return "2"

    def __init__(self, name ='unknown', firstname='unknown', birthdate='unknown', sex='unknown', rank='unknown'):

        self.name = name
        self.firstname = firstname
        self.birthdate = birthdate
        self.sex = sex
        self.rank = rank

    def set_player_data(self, list):

        self.name = list[0]
        self.firstname = list[1]
        self.birthdate = list[2]
        self.sex = list[3]
        self.rank = list[4]