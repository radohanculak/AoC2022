#!/bin/python

def task1(data):
    res = []
    for elem in data:
        res.append(sum(map(int, elem.split())))
    return max(res)


def task1_oneliner(data):
    return max(map(lambda x: sum(map(int, x.split())), data))


def task2(data):
    res = []
    for elem in data:
        res.append(sum(map(int, elem.split())))
    res.sort(reverse=True)
    return sum(res[:3])


def task2_oneliner(data):
    return sum(sorted(map(lambda x: sum(map(int, x.split())), data))[-3:])


def main():
    with open('./data/01.txt') as f:
        data = list(f.read().split("\n\n"))
    t1 = task1(data)
    t2 = task2(data)
    print(f"task1: {t1}\ntask2: {t2}")

    assert task1(data) == task1_oneliner(data)
    assert task2(data) == task2_oneliner(data)


if __name__ == "__main__":
    main()
