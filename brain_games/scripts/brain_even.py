#!/usr/bin/env python3
from brain_games.engine import play
from brain_games.games import even


def main():
    print("Welcome to the Brain Games!")
    play(even)


if __name__ == '__main__':
    main()
