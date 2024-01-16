"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, 
which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation
"""
def rotate(matrix: list[list[int]]) -> list:
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(len(matrix)):
        matrix[i] = matrix[i][::-1]

    return matrix