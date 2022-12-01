#!/bin/python

def task1(data):
    res = []
    for elem in data:
        res.append(sum(map(int, elem.split())))
    return max(res)


def task2(data):
    res = []
    for elem in data:
        res.append(sum(map(int, elem.split())))
    res.sort(reverse=True)
    return sum(res[:3])


def main():
    with open('./data/01.txt') as f:
        data = list(f.read().split("\n\n"))
    t1 = task1(data)
    t2 = task2(data)
    print(f"task1: {t1}\ntask2: {t2}")


if __name__ == "__main__":
    main()
