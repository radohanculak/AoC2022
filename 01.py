#!/bin/python

def task1():
    ...


def task2():
    ...


def main():
    with open('./data/01.txt') as f:
        data = list(map(int, f.read().split()))
    print(data)


if __name__ == "__main__":
    main()
