class Match:
    def __init__(self, home: str, away: str, home_score: int, away_score: int):
        self.home = home
        self.away = away
        self.home_score = home_score
        self.away_score = away_score
        if self.home_score >= self.away_score:
            self.win_team = self.home
        else:
            self.win_team = self.away

    def adv(self):
        return self.win_team


class Matches:
    def __init__(self):


teams = [Team('aardvarks'), Team('bats'), Team('chinchillas'), Team('dingoes'), Team('elephants'), Team('foxes'), Team('geckos')]
round0 = [Match(Team('aardvarks'), Team('bats'), 10, 5), Match(Team('chinchillas'), Team('dingoes'), 7, 7), Match(Team('Foxes'), Team('geckos'), 2, 3)]
round1 = [ Match(round0[0].adv, round0[1].adv, 9, 6), Match(Team('elephants'), round0[2].adv, 18, 0)]
# round2 = [Match(round1[0].adv), ]


class Bracket:
    def __init__(self):
        self.teams = []
        self.rounds = [[]]
        self.current_round = 0

    def add_team(self, name):
        self.teams.append(name)

    def add_match(self, home, away, h_score, a_score):
        if home not in self.teams:
            self.teams.append(home)
        if away not in self.teams:
            self.teams.append(away)
        self.rounds[self.current_round].append(Match(home, away, h_score, a_score))

    def round_advance(self):
        self.current_round += 1
        self.rounds.append([])

T = Bracket()
T.add_match('aardvarks', 'bats', 10, 5)
T.add_match('chinchillas', 'dingoes', 7, 7)
T.add_match('foxes', 'geckos', 2, 3)

T.round_advance()
T.add_match(T.round[0][0].adv, T.round[0][1].adv, 9, 6)
T.add_match('elephants', T.round[0][2].adv, 18, 0)

T.round_advance()
T.add_match(T.round[1][0], T.round[1][1], 4, 1)



