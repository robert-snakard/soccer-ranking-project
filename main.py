#!/usr/bin/env python

from app import App

app = App()

with open('sample_input.txt', 'r') as input_file:
    for _,line in enumerate(input_file):
        app.add_game(line)
