import modele.player as player
import modele.match as match
import modele.tour as tour
from datetime import datetime

STATIC_LIST_PLAYER = [
                        player.Player('player'+str(1), 'name', 'test', 'H', 1),
                        player.Player('player'+str(2), 'name', 'test', 'H', 2),
                        player.Player('player'+str(3), 'name', 'test', 'H', 3),
                        player.Player('player'+str(4), 'name', 'test', 'H', 8),
                        player.Player('player'+str(5), 'name', 'test', 'H', 5),
                        player.Player('player'+str(6), 'name', 'test', 'H', 6),
                        player.Player('player'+str(7), 'name', 'test', 'H', 7),
                        player.Player('player'+str(8), 'name', 'test', 'H', 4)]
print('List_OK')
'''test = tour.Tour(STATIC_LIST_PLAYER, 'round 1')
list_of_ranks = test.list_player_round(True)
test.temp_list_rank = list_of_ranks

result_tour1 = test.tour()
print(test.date_round_begin)
print(test.date_round_end)
print(result_tour1)'''

    '''def list_player_round(self,check_tour1):

        LIST_player = self.players
        if (check_tour1 == True):

            LIST_player.sort(key=lambda x: x.rank, reverse=False)
            self.temp_list_rank = LIST_player
            return LIST_player

        else:

            LIST_player.sort(key=lambda x: x.score, reverse=True)
            self.temp_list_rank = LIST_player
            return LIST_player

    def tour(self,n_of_match=4, check_tour1 = True):

        tour_match_list = []
        for x in range(n_of_match):
            state = int(input())
            temp_match = Match(self.temp_list_rank[x],self.temp_list_rank[x+n_of_match])
            tour_match_list.append(temp_match.result(state))
        self.date_round_end = datetime.today()
        return tour_match_list'''