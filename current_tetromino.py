import numpy as np

shapes = np.array([
    [
        [0,1,1,0],
        [0,1,1,0]
    ],[
        [0,1,1,0],
        [1,1,0,0]
    ],[
        [1,1,1,0],
        [0,0,1,0]
    ],[
        [1,1,0,0],
        [0,1,1,0]
    ],[
        [1,1,1,0],
        [1,0,0,0]
    ],[
        [1,1,1,0],
        [0,1,0,0]
    ],[
        [1,1,1,1],
        [0,0,0,0]
    ]
], dtype="bool")
shape_names = ["O","S","J","Z","L","T","I"]

def current_tetromino(tetris):
    roi = tetris.game_area().base[1:3,3:7] != 47
    matching = np.all(shapes == roi, axis=(1,2))
    if matching.sum() < 1:
        return None
    return shape_names[np.argmax(matching)]