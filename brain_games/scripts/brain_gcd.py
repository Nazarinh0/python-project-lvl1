#!/usr/bin/env python3.10
from brain_games.games import gcd
from brain_games.games.engine import play


def main():
    print(f'Welcome to the Brain Games!')
    play(gcd)


if __name__ == '__main__':
    main()