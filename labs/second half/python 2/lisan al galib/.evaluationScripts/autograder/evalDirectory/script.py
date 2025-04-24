from spice import *
import numpy as np
import os
import json
import matplotlib.pyplot as plt

os.environ["XDG_SESSION_TYPE"] = "xcb"
# BUILDING AN AUTOGRADER TO TEST THE FUNCTION IMPLEMENTATIONS IN SPICE.PY FILE
os.system("rm -f ../../evaluate.json")

overall = {"data": []
}
data = []

testcase_ids = 0
def get_testcase_id():
    global testcase_ids
    testcase_ids += 1
    return testcase_ids

### -----------------------------------------------------------
### -----------EVALUATING TODO 2--------------
### ------------Testcase 1-----------------
result = {
    "testid": str(get_testcase_id()),
    "status": "success",
    "score": 0,
    "maximum marks" : 1,
    "message": ""
    }

data_sample1 = load_data('testcases/sample1.txt')
if data_sample1 is not None:
    if type(data_sample1) == np.ndarray:
        if data_sample1.shape == (60,2):
            result["score"] = 1
            result["message"] = "TODO 2: load_data passed testcase 1."

if result["score"] != 1:
    result["status"] = "failed"
    result["message"] = "TODO 2: load_data failed testcase 1."

loading_testscore = result["score"]

data.append(result)
# print(result)

### ------------Testcase 2-----------------
result = {
    "testid": str(get_testcase_id()),
    "status": "success",
    "score": 0,
    "maximum marks" : 1,
    "message": ""
    }

data_sample2 = load_data('testcases/sample2.txt')
if data_sample2 is not None:
    if type(data_sample2) == np.ndarray:
        if data_sample2.shape == (120,2):
            result["score"] = 1
            result["message"] = "TODO 2: load_data passed testcase 2."

if result["score"] != 1:
    result["status"] = "failed"
    result["message"] = "TODO 2: load_data failed testcase 2."

loading_testscore += result["score"]

data.append(result)
# print(result)

### -----------------------------------------------------------
### -----------EVALUATING TODO 3.1--------------
### ------------Testcase 1-----------------
result = {
    "testid": str(get_testcase_id()),
    "status": "success",
    "score": 0,
    "maximum marks" : 1,
    "message": ""
    }

data_sample = np.random.rand(100,2)
centers = initialise_centers(data_sample, K = 3)

if centers is not None:
    if type(centers) == np.ndarray:
        if centers.shape == (3,2):
            all_true = True
            for center in centers:
                if center not in data_sample:
                    all_true = False
                    break
            if all_true:
                result["score"] = 1
                result["message"] = "TODO 3.1: initialise_centers passed when init_centers is None."

if result["score"] != 1:
    result["status"] = "failed"
    result["message"] = "TODO 3.1: initialise_centers failed when init_centers is None."

data.append(result)
# print(result)

### ------------Testcase 2-----------------
result = {
    "testid": str(get_testcase_id()),
    "status": "success",
    "score": 0,
    "maximum marks" : 1,
    "message": ""
    }

centers = initialise_centers(data_sample, K = 3, init_centers = data_sample[[3,12,21]])
if centers is not None:
    if type(centers) == np.ndarray:
        if centers.shape == (3,2):
            # Check if centers and init_centers are same
            all_true = True
            for center in centers:
                if center not in data_sample[[3,12,21]]:
                    all_true = False
                    break
            for center in data_sample[[3,12,21]]:
                if center not in centers:
                    all_true = False
                    break
            if all_true:
                result["score"] = 1
                result["message"] = "TODO 3.1: initialise_centers passed when init_centers is not None."

if result["score"] != 1:
    result["status"] = "failed"
    result["message"] = "TODO 3.1: initialise_centers failed when init_centers is not None."

data.append(result)
# print(result)

### -----------------------------------------------------------
### -----------EVALUATING TODO 3.2--------------
result = {
    "testid": str(get_testcase_id()),
    "status": "success",
    "score": 0,
    "maximum marks" : 1,
    "message": ""
    }

labels = initialise_labels(data_sample)
if labels is not None:
    if type(labels) == np.ndarray:
        if labels.shape == (100,):
            if np.all(labels == 0):
                result["score"] = 1
                result["message"] = "TODO 3.2: initialise_labels passed."

if result["score"] != 1:
    result["status"] = "failed"
    result["message"] = "TODO 3.2: initialise_labels failed."

data.append(result)
# print(result)

### -----------------------------------------------------------
### -----------EVALUATING TODO 4.1--------------
result = {
    "testid": str(get_testcase_id()),
    "status": "success",
    "score": 0,
    "maximum marks" : 2,
    "message": ""
    }

data_sample1 = np.loadtxt('testcases/sample1.txt', delimiter=',')
centers = data_sample1[[0,15,30]]
distances = calculate_distances(data_sample1, centers)
if distances is not None:
    if type(distances) == np.ndarray:
        if distances.shape == (60,3):
            if np.all(distances >= 0):
                correct_distances = np.loadtxt('testcases/sample1_distances.txt', delimiter=',')
                if np.all(np.abs(distances - correct_distances) < 1e-5):
                    result["score"] = 2
                    result["message"] = "TODO 4.1: calculate_distances passed testcase."

if result["score"] != 2:
    result["status"] = "failed"
    result["message"] = "TODO 4.1: calculate_distances failed testcase."

data.append(result)
# print(result)

### -----------------------------------------------------------
### -----------EVALUATING TODO 4.2--------------

result = {
    "testid": str(get_testcase_id()),
    "status": "success",
    "score": 0,
    "maximum marks" : 2,
    "message": ""
    }

distances = np.loadtxt('testcases/sample1_distances.txt', delimiter=',')
labels = update_labels(distances)
if labels is not None:
    if type(labels) == np.ndarray:
        if labels.shape == (60,):
            correct_labels = np.loadtxt('testcases/sample1_labels.txt', delimiter=',')
            correct_labels = correct_labels.astype(int)
            if np.all(labels == correct_labels):
                result["score"] = 2
                result["message"] = "TODO 4.2: update_labels passed testcase."

if result["score"] != 2:
    result["status"] = "failed"
    result["message"] = "TODO 4.2: update_labels failed testcase."

data.append(result)
# print(result)

### -----------------------------------------------------------
### -----------EVALUATING TODO 5--------------
result = {
    "testid": str(get_testcase_id()),
    "status": "success",
    "score": 0,
    "maximum marks" : 2,
    "message": ""
    }

labels = np.loadtxt('testcases/sample1_labels.txt', delimiter=',')
labels = labels.astype(int)
centers = update_centers(data_sample1, labels, K=3)
if centers is not None:
    if type(centers) == np.ndarray:
        if centers.shape == (3,2):
            correct_centers = np.loadtxt('testcases/sample1_centers.txt', delimiter=',')
            if np.all(np.abs(centers - correct_centers) < 1e-5):
                result["score"] = 2
                result["message"] = "TODO 5: update_centers passed testcase."

if result["score"] != 2:
    result["status"] = "failed"
    result["message"] = "TODO 5: update_centers failed testcase."

data.append(result)
# print(result)

### -----------------------------------------------------------
### -----------EVALUATING TODO 6--------------

result = {
    "testid": str(get_testcase_id()),
    "status": "success",
    "score": 0,
    "maximum marks" : 2,
    "message": ""
    }

labels1 = np.array([0,1,3,4,4,1,4,0,0,4])
labels2 = np.array([0,1,3,2,4,1,4,0,0,4])
out = check_termination(labels1, labels2)
if out is not None:
    if type(out) == bool or type(out) == np.bool_:
        if not out:
            result["score"] += 1
            result["message"] += "TODO 6: check_termination passed unequal testcase."
if result["score"] != 1:
    result["status"] = "failed"
    result["message"] = "TODO 6: check_termination failed unequal testcase."

equal_tc = 0
out = check_termination(labels1, labels1.copy())
if out is not None:
    if type(out) == bool or type(out) == np.bool_:
        if out:
            result["score"] += 1
            equal_tc += 1
            result["message"] += " check_termination passed equal testcase."
if equal_tc != 1:
    result["status"] = "failed"
    result["message"] += " check_termination failed equal testcase."

data.append(result)
# print(result)

### -----------------------------------------------------------
### -----------EVALUATING TODO 7--------------
result = {
    "testid": str(get_testcase_id()),
    "status": "success",
    "score": 0,
    "maximum marks" : 4,
    "message": ""
    }

if loading_testscore != 2:
    result["status"] = "failed"
    result["message"] = "TODO 7: load_data failed. Fix the errors and try again."
    data.append(result)
else:
    labels = np.loadtxt('testcases/sample1_labels.txt', delimiter=',')
    labels = labels.astype(int)
    centers = np.loadtxt('testcases/sample1_centers.txt', delimiter=',')
    plt_object = visualise('testcases/sample1.txt', labels, centers)
    result["message"] += "TODO 7: "
    if plt_object is not None:
        if type(plt_object) == type(plt):
            # Check the title
            if plt.gca().get_title() == 'K-means clustering':
                result["score"] += 1
            else:
                result["message"] += "Title of the plot is incorrect. "
            # Check the xlabel
            if plt.gca().get_xlabel() == 'Longitude':
                result["score"] += 1
            else:
                result["message"] += "xlabel of the plot is incorrect. "
            # Check the ylabel
            if plt.gca().get_ylabel() == 'Latitude':
                result["score"] += 1
            else:
                result["message"] += "ylabel of the plot is incorrect. "
            # Check if the plot is saved
            if os.path.exists('kmeans.png'):
                result["score"] += 1
            else:
                result["message"] += "Plot is not saved. "

    if result["score"] != 4:
        result["status"] = "failed"
    else:
        result["message"] += "All 4 testcases passed."

    data.append(result)

# print(result)
    
### -----------------------------------------------------------
### -----------CHECKING FOR LOOPS--------------
num_loops = 0
with open("spice.py") as f:
    # number of times for loop is used
    num_loops += f.read().count('for')
    # number of times while loop is used
    f.seek(0)
    num_loops += f.read().count('while')

if num_loops == 1:
    result = {
        "testid": str(get_testcase_id()),
        "status": "success",
        "score": 0,
        "maximum marks" : 0,
        "message": "FINAL CHECK : No loops used in the code."
    }
    data.append(result)
else:
    result = {
        "testid": str(get_testcase_id()),
        "status": "failed",
        "score": -2*(num_loops-1),
        "maximum marks" : 0,
        "message": f"FINAL CHECK : {num_loops-1} Loops used in the code. Try to implement the code without using loops."
    }
    data.append(result)

### -----------------------------------------------------------
### -----------DONE TESTING--------------

overall['data'] = data
print(json.dumps(overall, indent=4))
with open('../../evaluate.json', 'w') as f:
	json.dump(overall,f,indent=4)