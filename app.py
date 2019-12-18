#!/usr/bin/env python

import re
from collections import defaultdict

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
        elif int(results["scorea"]) < int(results["scoreb"]):
            self.team_scores[results["teamb"]] += 3;
        else:
            self.team_scores[results["teama"]] += 1;
            self.team_scores[results["teamb"]] += 1;

    def run():
        print("Hello World")
