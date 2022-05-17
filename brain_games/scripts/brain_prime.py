#!/usr/bin/env python3.10
from brain_games.games import prime
from brain_games.games.engine import play


def main():
    print('Welcome to the Brain Games!')
    play(prime)


if __name__ == '__main__':
    main()
