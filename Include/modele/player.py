class Player:

    def __repr__(self):

        return self.name

    def __init__(self, name: str ='unknown', firstname: str ='unknown',
                 birthdate: str ='unknown', sex: str ='unknown', rank: int = 0):

        self.name = name
        self.firstname = firstname
        self.birthdate = birthdate
        self.sex = sex
        self.rank = rank
