from .tour import Tour
class Tournament:

    def __init__(self, name: str = 'unknown', place: str = 'unknown',
                 date='unknown', nOfTurns : int = 4,
                 ronde : list = [], players : list = [],
                 timeControl: str = 'unknown', description: str = 'unknown'):

        self.name = name
        self.place = place
        self.date = date
        self.nOfTurns = nOfTurns
        self.ronde = ronde
        self.players = players
        self.timeControls = timeControl
        self.description = description
