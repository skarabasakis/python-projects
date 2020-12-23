import random

def matches(teams):
    return [(home, visitor) for i, home in enumerate(teams) for visitor in teams[i+1:]]


def random_result():
    return tuple(random.choices([0,1,2,3,4], weights=[40,30,20,8,2], k=2))


def results(matches):
    return { match: random_result() for match in matches}


def format_result(match, score):
    return "%s %d - %d %s" % (match[0], *score, match[1])

TEAMS = [
    'Game of Throw-Ins',
    'Elemonators',
    'Toothless Crocodiles',
    'Screaming Nachos',
    'Formerly in Shape Stars',
    'Two Left Feet'
]

with open("scores.txt", "w") as f:
    for match, score in results(matches(TEAMS)).items():
        f.write(format_result(match,score) + '\n')
