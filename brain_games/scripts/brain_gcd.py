#!/usr/bin/env python3
import importlib
from brain_games.engine import play


def main():
    print("Welcome to the Brain Games!")
    gcd_fun()


def gcd_fun():
    game_module_name = 'brain_games.games.gcd'
    game_module = importlib.import_module(game_module_name)
    play(game_module)


if __name__ == '__main__':
    main()
