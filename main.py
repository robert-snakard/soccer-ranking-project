#!/usr/bin/env python

from app import App
import argparse


parser = argparse.ArgumentParser("Rank soccer teams")
parser.add_argument("-f", dest="input_file", type=argparse.FileType('r'), default='-');

app = App()
args = parser.parse_args()

app.run(args.input_file)
    
#with open('sample_input.txt', 'r') as input_file:
#    for _,line in enumerate(input_file):
#        app.add_game(line)

#rankings = app.get_rankings()

#for team in rankings:
#    print("{}, {} pts".format(team.name, team.score))
