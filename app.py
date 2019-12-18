#!/usr/bin/env python

import re

class App:
    
    pattern = re.compile(r"(.*) (\d+), (.*) (\d+)")

    def __init__(self):
        self.team_scores = {}

    def add_game(self, score):
        match = self.pattern.match(score)
        if not match:
            raise InvalidScore
        print(match.groups())

    def run():
        print("Hello World")
