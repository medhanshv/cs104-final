import numpy as np
import os
import json
from main import *

os.system("rm -rf ../evaluate.json")

overall = {"data": []}
data = []

matrix = np.array(
    [
        [5, 5, 84, 3, 9],
        [6, 11, 1, 55, 58],
        [1, 20, 48, 12, 36],
        [8, 4, 41, 93, 98],
        [6, 17, 64, 0, 13],
    ]
)

### Task 1

result = {
    "testid": 1,
    "status": "success",
    "score": 0,
    "maximum marks": 1,
    "message": "",
}

task1_result = task1(matrix)
expected_result = np.array(
    [
        [5, 0, 0, 0, 0],
        [5, 11, 0, 0, 0],
        [84, 1, 48, 0, 0],
        [3, 55, 12, 93, 0],
        [9, 58, 36, 98, 13],
    ]
)

try:
    if np.array_equal(task1_result, expected_result):
        result["message"] = "Task 1 successful"
        result["score"] = 1
    else:
        result["message"] = "Task 1 failed"
        result["status"] = "failed"
except Exception as e:
    result["message"] = "Task 1 failed"
    result["status"] = "failed"

data.append(result)

### Task 2

result = {
    "testid": 2,
    "status": "success",
    "score": 0,
    "maximum marks": 1,
    "message": "",
}

mean, median, std, det, inv, pinv = task2(matrix)
expected_mean = np.array([5.2, 11.4, 47.6, 32.6, 42.8])
expected_median = np.array([6.0, 11.0, 48.0, 12.0, 36.0])
expected_std = np.array([2.31516738, 6.34350061, 27.60144924, 36.0921044, 32.72552521])
expected_det = 1821200.9999999853
expected_inv = np.array(
    (
        [
            [-0.58373129, -0.52849521, -0.26407794, 0.36545554, 0.73834354],
            [0.22828782, 0.28887256, 0.07659781, -0.18808632, -0.24109695],
            [0.05239894, 0.034866, 0.01394959, -0.02410991, -0.04871016],
            [0.31980819, 0.33957372, 0.06275584, -0.2084844, -0.33856065],
            [-0.28707979, -0.30548358, -0.04695912, 0.19598221, 0.29123364],
        ]
    )
)
expected_pinv = np.array(
    [
        [-0.58373129, -0.52849521, -0.26407794, 0.36545554, 0.73834354],
        [0.22828782, 0.28887256, 0.07659781, -0.18808632, -0.24109695],
        [0.05239894, 0.034866, 0.01394959, -0.02410991, -0.04871016],
        [0.31980819, 0.33957372, 0.06275584, -0.2084844, -0.33856065],
        [-0.28707979, -0.30548358, -0.04695912, 0.19598221, 0.29123364],
    ]
)

try:
    if np.array_equal(mean, expected_mean):
        result["message"] += "Mean successful."
        result["score"] += 1
    else:
        result["message"] += "Mean failed."
        result["status"] = "failed"
except Exception as e:
    result["message"] += "Mean failed."
    result["status"] = "failed"

data.append(result)

result = {
    "testid": 3,
    "status": "success",
    "score": 0,
    "maximum marks": 1,
    "message": "",
}

try:
    if np.array_equal(median, expected_median):
        result["message"] += "Median successful."
        result["score"] += 1
    else:
        result["message"] += "Median failed."
        result["status"] = "failed"
except Exception as e:
    result["message"] += "Median failed."
    result["status"] = "failed"

data.append(result)

result = {
    "testid": 4,
    "status": "success",
    "score": 0,
    "maximum marks": 1,
    "message": "",
}

try:
    # if norm of difference is less than 1e-4
    if np.linalg.norm(np.round(std, 2) - np.round(expected_std, 2)) < 1e-4:
        result["message"] += "Standard deviation successful."
        result["score"] += 1
    else:
        result["message"] += "Standard deviation failed."
        result["status"] = "failed"
except Exception as e:
    result["message"] += "Standard deviation failed."
    result["status"] = "failed"

data.append(result)

result = {
    "testid": 5,
    "status": "success",
    "score": 0,
    "maximum marks": 1,
    "message": "",
}


try:
    # if abs difference is less than 1e-4
    if abs(np.round(det, 2) - np.round(expected_det, 2)) < 1e-4:
        result["message"] += "Determinant successful."
        result["score"] += 1
    else:
        result["message"] += "Determinant failed."
        result["status"] = "failed"
except Exception as e:
    result["message"] += "Determinant failed."
    result["status"] = "failed"

data.append(result)

result = {
    "testid": 6,
    "status": "success",
    "score": 0,
    "maximum marks": 1,
    "message": "",
}

try:
    # if norm of difference is less than 1e-4
    if np.linalg.norm(np.round(inv, 2) - np.round(expected_inv, 2)) < 1e-4:
        result["message"] += "Inverse successful."
        result["score"] += 1
    else:
        result["message"] += "Inverse failed."
        result["status"] = "failed"
except Exception as e:
    result["message"] += "Inverse failed."
    result["status"] = "failed"

data.append(result)

result = {
    "testid": 7,
    "status": "success",
    "score": 0,
    "maximum marks": 1,
    "message": "",
}

try:
    # if norm of difference is less than 1e-4
    if np.linalg.norm(np.round(pinv, 2) - np.round(expected_pinv, 2)) < 1e-4:
        result["message"] += "Pseudo-inverse successful."
        result["score"] += 1
    else:
        result["message"] += "Pseudo-inverse failed."
        result["status"] = "failed"
except Exception as e:
    result["message"] += "Pseudo-inverse failed."
    result["status"] = "failed"

data.append(result)

### Task 3
result = {
    "testid": 8,
    "status": "success",
    "score": 0,
    "maximum marks": 1,
    "message": "",
}

task3_result = task3(matrix, num=1, padding=2)
expected_result = np.array(
    [
        [1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 5, 5, 84, 3, 9, 1, 1],
        [1, 1, 6, 11, 1, 55, 58, 1, 1],
        [1, 1, 1, 20, 48, 12, 36, 1, 1],
        [1, 1, 8, 4, 41, 93, 98, 1, 1],
        [1, 1, 6, 17, 64, 0, 13, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1],
    ]
)

try:
    if np.array_equal(task3_result, expected_result):
        result["message"] = "Task 3 successful"
        result["score"] = 1
    else:
        result["message"] = "Task 3 failed"
        result["status"] = "failed"
except Exception as e:
    result["message"] = "Task 3 failed"
    result["status"] = "failed"

data.append(result)

overall["data"] = data
print(json.dumps(overall, indent=4))
with open("../evaluate.json", "w") as outfile:
    json.dump(overall, outfile)
