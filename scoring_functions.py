import numpy as np

def get_heights(matrix):
    counts = []
    count = 0
    for i in range(10):
        for n in range(18):
            if matrix[n, i] == 0:
                count += 1
            else:
                if count != 0:
                    count = abs(count - 18)
                    counts.append(count)
                    count = 0
                break
    return counts

def aggregate_height(matrix):
        return sum(get_heights(matrix))

def calculate_bumpiness(matrix):
    counts = get_heights(matrix)
    bumpiness = 0
    for m in range(1, 10):
        bumpiness += abs(counts[m-1]-counts[m])
    return bumpiness

def lines_cleared_at_same_time(matrix):
    lines_cleared = 0
    count = 0
    for n in range(18):
        for i in range(10):
            if matrix[n, i] == 1:
                count += 1
                if count == 10:
                    lines_cleared += 1
                    count = 0
            else:
                count = 0
                break
    return lines_cleared

def recognize_holes(matrix):
    first_block = False
    count = 0
    for i in range(10):
        for n in range(18):
            if matrix[n, i] == 1:
                first_block = True
            if first_block == True:
                if matrix[n, i] == 0:
                    count += 1
        first_block = False
    return count