#!/usr/bin/env python
# coding: utf-8

from pyboy import PyBoy, WindowEvent
import numpy as np
import current_tetromino as ct
from possibilities import get_possibilities
import scoring_functions as sf
import moving_instructions as mi

def game_over(tetris):
    return tetris.game_area().base[-2,-2] == 39

def play_until_next_tetro(pyboy, tetris):
    while not ct.current_tetromino(tetris):
        pyboy.tick()
        if game_over(tetris):
            break

def score(possibility):
    field = possibility[0]
    return 4*sf.recognize_holes(field)+max(sf.get_heights(field))-10*sf.lines_cleared_at_same_time(field)

def get_starting_col(tetris, rotations):
    current = ct.current_tetromino(tetris)
    start_col = 3
    if current=="O":
        start_col = 4
    if current in "I" and rotations==1:
        start_col = 4
    if current in "TLJ" and rotations==3:
        start_col = 4
    return start_col

pyboy = PyBoy("Tetris.gb", game_wrapper=True)#, sound=True)
pyboy.set_emulation_speed(10)
tetris = pyboy.game_wrapper()
tetris.start_game()
tetris.reset_game()#timer_div=0)

while not game_over(tetris):
    possibilities = get_possibilities(tetris)
    possibilities.sort(key=score)
    start_col = get_starting_col(tetris, possibilities[0][2])
    mi.piece_positioning(start_col-possibilities[0][1],possibilities[0][2],pyboy,delay=10)
    [pyboy.tick() for _ in range(30)]
    play_until_next_tetro(pyboy,tetris)

pyboy.set_emulation_speed(1)
print(tetris.score)

# Keep the game running forever
while True:
    pyboy.tick()
