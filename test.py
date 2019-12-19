import sys, io
from app import App
import main

# game_list should be a list of game strings "teama scorea, teamb scoreb"
# expected scores should be a dict - {'team name' : 'score'}
def test_insert(game_list, expected_scores):
    app = App()
    for game in game_list:
        app.add_game(game_list)
    assert app.team_scores == expected_scores

# team_scores should be a dict - {'team name' : 'score'}
# expected_rankings should be a list - ['first place name', 'second place name', ...]
def test_ranking(team_scores, expected_ranking):
    app = App()
    app.team_scores = team_scores
    rankings = app.get_rankings()
    for idx, name in enumerate(rankings):
        assert expected_rankings[i] == name

# expected output should be the expected std output
def test_print(game_list, expected_output):
    stdout = sys.stdout
    sys.stdout = io.StringIO()

    app = App()
    for game in game_list:
        app.add_game(game)
    app.print_rankings()

    output = sys.stdout.getvalue()
    sys.stdout = stdout

    assert output == expected_output

# file should be an opened file
# expected output should be the expected std output
def test_run(file, expected_output):
    stdout = sys.stdout
    sys.stdout = io.StringIO()

    app = App()
    app.run(file)

    output = sys.stdout.getvalue()
    sys.stdout = stdout

    assert output == expected_output

#############################################
#### TESTS BELOW ####
#############################################

