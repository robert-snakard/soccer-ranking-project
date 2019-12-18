#!/usr/bin/env python

import re
from collections import defaultdict, namedtuple

class App:
    
    pattern = re.compile(r"(?P<teama>.*) (?P<scorea>\d+), (?P<teamb>.*) (?P<scoreb>\d+)")

    def __init__(self):
        self.team_scores = defaultdict(lambda: 0)

    def add_game(self, score):
        match = self.pattern.match(score)
        if not match:
            raise InvalidScore

        results = match.groupdict()
        if int(results["scorea"]) > int(results["scoreb"]):
            self.team_scores[results["teama"]] += 3;
            self.team_scores[results["teamb"]] += 0;
        elif int(results["scorea"]) < int(results["scoreb"]):
            self.team_scores[results["teamb"]] += 3;
            self.team_scores[results["teama"]] += 0;
        else:
            self.team_scores[results["teama"]] += 1;
            self.team_scores[results["teamb"]] += 1;

    def get_rankings(self):
        Team = namedtuple('Team', ['score', 'name'])
        return sorted([Team(v, k) for (k, v) in self.team_scores.items()],
                          key=team_to_string)

    def run():
        print("Hello World")

# helper function
def team_to_string(team):
    # have to sort by negative score because 5 > 1 but a < z. This way -5 < 1 and a < z. 
    return (-team.score, team.name)
