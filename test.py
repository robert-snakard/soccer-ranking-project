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
    for idx, team in enumerate(rankings):
        assert expected_rankings[idx] == team.name
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
print("Test ranking no teams -", test_ranking({}, []))
print("Test ranking one team -", test_ranking({'a': 3}, ['a']))
print("Test ranking two teams -", test_ranking({'a': 3, 'b': 0}, ['a', 'b']))
print("Test ranking six teams -", test_ranking({'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5}, ['f', 'e', 'd', 'c', 'b', 'a']))
print("")
print("Test ranking with tie -", test_ranking({'a': 3, 'b': 3}, ['a', 'b']))
print("Test ranking with tie swap -", test_ranking({'b': 3, 'a': 3}, ['a', 'b']))
print("Test ranking with tie and matching names -", test_ranking({'a': 3, 'aa': 3}, ['a', 'aa']))
print("")
print("Test print empty input -", test_print([], ""))
print("Test print one game -", test_print(['a 3, b 2'], "1. a, 3 pts\n2. b, 0 pts\n"))
print("Test print with tie -", test_print(['a 3, b 3', 'a 3, b 3'], "1. a, 2 pts\n1. b, 2 pts\n"))
print("Test print with one point -", test_print(['a 3, b 3'], "1. a, 1 pt\n1. b, 1 pt\n"))
print("")
print("Test run -", test_run(open('sample_input.txt', 'r'), open('expected_output.txt', 'r').read()))
print("")
