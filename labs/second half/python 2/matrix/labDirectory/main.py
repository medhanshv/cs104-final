'''
    NumPy and The Matrix
'''

import numpy as np

def task1(matrix):
    '''return the upper diagonal matrix in column-wise fashion'''
    upper=np.triu(matrix)
    return upper.T

def task2(matrix):
    '''return mean, median, std (precision 2), all along x, determinant, inverse, pseudo-inverse'''
    mean = np.round((np.mean(matrix,axis=0)),2)
    median = np.round((np.median(matrix,axis=0)),2)
    std = np.round((np.std(matrix,axis=0)),2)
    det =  np.round((np.linalg.det(matrix)),2)
    inv_rounded = None
    if det != 0:
        inv = np.linalg.inv(matrix)
        inv_rounded = np.round(inv, 2)
    else:
        inv_rounded = None
    pseudoinv = np.linalg.pinv(matrix)
    pseudoinv_rounded = np.round(pseudoinv, 2)
    return mean, median, std, det, inv_rounded, pseudoinv_rounded

def task3(matrix, num = 0, padding = 3):
    return np.pad(matrix, pad_width=padding, mode='constant', constant_values=num)

if __name__ == '__main__':

    matrix = np.array([
        [5,5,84,3,9],
        [6,11,1,55,58],
        [1,20,48,12,36],
        [8,4,41,93,98],
        [6,17,64,0,13]
    ])


    print(task1(matrix))


    mean, median, std, det, inv, pseudoinv = task2(matrix)
    print("Mean: ", mean)
    print("Median: ", median)
    print("Standard Deviation: ", std)
    print("Determinant: ", det)
    print("Inverse: ", inv)
    print("Pseudo-Inverse: ", pseudoinv)

    print(task3(matrix)) # default padding