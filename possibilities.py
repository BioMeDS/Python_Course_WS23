import numpy as np
import current_tetromino as ct

def get_possibilities(tetris):
    tetro = ct.current_tetromino(tetris)
    binary_game_area = tetris.game_area().base != 47
    binary_game_area[1:3,3:7] = False
    original_shape = ct.get_shape(tetro, crop=True)
    expected_sum = binary_game_area.sum() + original_shape.sum()
    possibilities = []
    for rotation in range(4):
        shape = original_shape.copy()
        for i in range(rotation):
            shape = np.rot90(shape, k=-1)
        h,w = shape.shape
        for c in range(10 - w + 1):
            best = binary_game_area.copy()
            for r in range(18 - h + 1):
                ga = binary_game_area.copy()
                ga[r:r+h,c:c+w] = np.logical_or(ga[r:r+h,c:c+w], shape)
                if ga.sum() != expected_sum:
                    break
                best = ga
            possibilities.append([best, c, rotation])
    return possibilities