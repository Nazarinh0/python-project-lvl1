#!/usr/bin/env python3.10
from brain_games.games import calc
from brain_games.games.engine import play


def main():
    print(f'Welcome to the Brain Games!')
    play(calc)


if __name__ == '__main__':
    main()
