#!/usr/bin/env python3
from brain_games.engine import play
from brain_games.games import calc


def main():
    print("Welcome to the Brain Games!")
    play(calc)


if __name__ == '__main__':
    main()
