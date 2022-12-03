#!/bin/python


def get_priority(char: str) -> int:
    return ord(char) - 38 if char.isupper() else ord(char) - 96


def task1(data):
    counter = 0
    for elem in data:
        a, b = elem[len(elem) // 2:], elem[:len(elem) // 2]
        intersect = set(a).intersection(set(b)).pop()
        counter += get_priority(intersect)
    return counter


def task1_oneliner(data):
    return sum(map(lambda elem: get_priority(set(elem[len(elem) // 2:]).intersection(set(elem[:len(elem) // 2])).pop()), data))


def task2(data):
    counter = 0
    for i in range(0, len(data) - 1, 3):
        a, b, c = set(data[i]), set(data[i+1]), set(data[i+2])
        intersect = a.intersection(b).intersection(c).pop()
        counter += get_priority(intersect)
    return counter


def main():
    with open('./data/03.txt') as f:
        data = list(f.read().split("\n"))
    t1 = task1(data)
    t2 = task2(data)
    print(f"task1: {t1}\ntask2: {t2}")
    assert t1 == task1_oneliner(data)


if __name__ == "__main__":
    main()
