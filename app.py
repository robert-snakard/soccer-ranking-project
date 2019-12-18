#!/usr/bin/env python

import re

class App:
    
    pattern = re.compile(r"(?P<teama>.*) (?P<scorea>\d+), (?P<teamb>.*) (?P<scoreb>\d+)")

    def __init__(self):
        self.team_scores = {}

    def add_game(self, score):
        match = self.pattern.match(score)
        if not match:
            raise InvalidScore
        print(match.groupdict())

    def run():
        print("Hello World")
