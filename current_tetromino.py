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

def get_shape(shape_name, crop=False):
    ind = shape_names.index(shape_name)
    if ind < 0:
        return None
    shape = shapes[ind]
    if crop:
        if shape[:,3].sum() == 0:
            shape = shape[:,:3]
        if shape[:,0].sum() == 0:
            shape = shape[:,1:]
        if shape[1,:].sum() == 0:
            shape = shape[:1,:]
    return shape