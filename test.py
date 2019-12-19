import sys, io
from app import App

# game_list should be a list of game strings "teama scorea, teamb scoreb"
# expected scores should be a dict - {'team name' : 'score'}
def test_insert(game_list, expected_scores):
    app = App()
    for game in game_list:
        app.add_game(game)
    assert app.team_scores == expected_scores
    return "success"

# team_scores should be a dict - {'team name' : 'score'}
# expected_rankings should be a list - ['first place name', 'second place name', ...]
def test_ranking(team_scores, expected_rankings):
    app = App()
    app.team_scores = team_scores
    rankings = app.get_rankings()
    for idx, name in enumerate(rankings):
        assert expected_rankings[idx] == name
    return "success"

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
    return "success"

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
    return "success"

#############################################
#### TESTS BELOW ####
#############################################

print("")
print("Testing empty insert -", test_insert('', {}))
print("")
print("Testing single game input: team a wins -", test_insert(['a 5, b 3'], {'a': 3, 'b': 0}))
print("Testing single game input: team b wins -", test_insert(['a 3, b 5'], {'a': 0, 'b': 3}))
print("Testing single game input: tie -", test_insert(['a 5, b 5'], {'a': 1, 'b': 1}))
print("")
print("Testing two games: four teams -", test_insert(['a 5, b 3', 'c 1, d 4'], {'a': 3, 'b': 0, 'c': 0, 'd': 3}))
print("Testing two games: three teams -", test_insert(['a 5, b 3', 'b 1, c 4'], {'a': 3, 'b': 0, 'c': 3}))
print("Testing two games: two teams -", test_insert(['a 5, b 3', 'a 1, b 4'], {'a': 3, 'b': 3}))
print("")
print("Testing three games -", test_insert(['a 5, b 3', 'a 1, b 4', 'a 2, c 2'], {'a': 4, 'b': 3, 'c': 1}))
print("")
