#!/bin/python

POINTS = {'X': 1, 'Y': 2, 'Z': 3}
RESULT = {
    ('A', 'X'): 3,
    ('B', 'Y'): 3,
    ('C', 'Z'): 3,

    ('A', 'Z'): 0,
    ('B', 'X'): 0,
    ('C', 'Y'): 0,

    ('A', 'Y'): 6,
    ('B', 'Z'): 6,
    ('C', 'X'): 6,
    }

LOSE = {
    'A': 3,
    'B': 1,
    'C': 2,
}

DRAW = {
    'A': 1,
    'B': 2,
    'C': 3,
}

WIN = {
    'A': 2,
    'B': 3,
    'C': 1,
}


def task1(data):
    res = 0
    for x, y in data:
        res += POINTS[y] + RESULT[(x, y)]
    return res


def task2(data):
    res = 0
    for x, y in data:
        match x, y:
            case opp, 'X':  # lose
                res += 0 + LOSE[opp]
            case opp, 'Y':  # draw
                res += 3 + DRAW[opp]
            case opp, 'Z':  # win
                res += 6 + WIN[opp]
    return res


def main():
    with open('./data/02.txt') as f:
        data = list(map(lambda x: (x[0], x[-1]), f.read().split("\n")))
    t1 = task1(data)
    t2 = task2(data)
    print(f"task1: {t1}\ntask2: {t2}")

    # assert task1(data) == task1_oneliner(data)
    # assert task2(data) == task2_oneliner(data)


if __name__ == "__main__":
    main()
