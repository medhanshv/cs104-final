'''Import required modules'''
import json
import math

file_path = '/home/labDirectory/main.py'  # Replace with the actual path to your file
target_string = 'import Polar'  # Replace with the string you're looking for
target_string2 = 'import Complex'
try:
    print("hello")
    with open(file_path, 'r', encoding='utf-8') as file:
        file_contents = file.read()

        if target_string and target_string2 in file_contents:
            print(f"Success: '{target_string}' found in the file.")
        else:
            overall = {"data": []}
            data = []
            result = {
            "testid": "Import Classes",
            "status": "failed",
            "score": 0,
            "maximum marks" : 1,
            "message": "Please import the classes properly"
            }
            data.append(result)
            overall['data'] = data
            print(json.dumps(overall, indent=4))
            with open('../evaluate.json', 'w') as f:
                json.dump(overall,f,indent=4)
            print(f"Error: '{target_string}' not found in the file.")
            exit()
except FileNotFoundError:
    print(f"Error: File not found at {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")
from main import *
# try:
#     print("check")
#     from polar import Polar
#     from complex import Complex
# except ImportError:
#     print("hello")
#     overall = {"data": []}
#     data = []
#     result = {
#     "testid": "1",
#     "status": "failed",
#     "score": 0,
#     "maximum marks" : 1,
#     "message": "Please import the classes properly"
#     }
#     data.append(result)
#     overall['data'] = data
#     print(json.dumps(overall, indent=4))
#     with open('../evaluate.json', 'w') as f:
#         json.dump(overall,f,indent=4)


overall = {"data": []
}
epsilon = 1e-2
data = []
msg = ""
total = 0
result = {
    "testid": "1",
    "status": "success",
    "score": 0,
    "maximum marks" : 1,
    "message": ""
    }

marks = {
    'modulus': 0,
    'arg': 0,
    'abscissa': 0,
    'ordinate': 0,
    'distance': 0
}


# --------------------------- modulus ---------------------------
result = {
    "testid": "1",
    "status": "success",
    "score": 0,
    "maximum marks" : 1,
    "message": ""
    }
output = {}
with open('./test/modulus.txt', 'r', encoding='utf-8') as f:
    n = int(f.readline())
    for i in range(n):
        a, b = map(float, f.readline().split())
        try:
            output[i] = modulus(Complex(a, b))
        except:
            output[i] = -1

score = 0
with open('./test/out/modulus.txt', 'r', encoding='utf-8') as f:
    for i, o in output.items():
        c = f.readline()
        if o != None and (abs(float(c)-o) < epsilon):
            score += 1

result["testid"] = "modulus"
result["score"] = score / len(output)
if score == 0:
    result["status"] = "failed"
data.append(result)
# marks['modulus'] = 0.5 * score / len(output)

# --------------------------- arg ---------------------------
result = {
    "testid": "1",
    "status": "success",
    "score": 0,
    "maximum marks" : 1,
    "message": ""
    }
output = {}
with open('./test/arg.txt', 'r', encoding='utf-8') as f:
    n = int(f.readline())
    for i in range(n):
        a, b = map(float, f.readline().split())
        try:
            output[i] = arg(Complex(a, b))
        except:
            output[i] = -1

score = 0
with open('./test/out/arg.txt', 'r', encoding='utf-8') as f:
    for i, o in output.items():
        c = f.readline()
        # print(abs(float(c)-o))
        if o != None and (abs(float(c)-o) < epsilon):
            score += 1

result["testid"] = "arg"
result["score"] = score / len(output)
if score == 0:
    result["status"] = "failed"
data.append(result)

# --------------------------- abscissa ---------------------------
result = {
    "testid": "1",
    "status": "success",
    "score": 0,
    "maximum marks" : 1,
    "message": ""
    }
output = {}
with open('./test/abscissa.txt', 'r', encoding='utf-8') as f:
    n = int(f.readline())
    for i in range(n):
        a, b = map(float, f.readline().split())
        try:
            output[i] = abscissa(Polar(a, b))
        except:
            output[i] = -1

score = 0
with open('./test/out/abscissa.txt', 'r', encoding='utf-8') as f:
    for i, o in output.items():
        c = f.readline()
        if o != None and (abs(float(c)-o) < epsilon):
            score += 1
# print(score)
result["testid"] = "abscissa"
result["score"] = score / len(output)
if score == 0:
    result["status"] = "failed"
data.append(result)

# --------------------------- ordinate ---------------------------
result = {
    "testid": "1",
    "status": "success",
    "score": 0,
    "maximum marks" : 1,
    "message": ""
    }
output = {}
with open('./test/ordinate.txt', 'r', encoding='utf-8') as f:
    n = int(f.readline())
    for i in range(n):
        a, b = map(float, f.readline().split())
        try:
            output[i] = ordinate(Polar(a, b))
        except:
            output[i] = -1

score = 0
with open('./test/out/ordinate.txt', 'r', encoding='utf-8') as f:
    for i, o in output.items():
        c = f.readline()
        if o != None and (abs(float(c)-o) < epsilon):
            score += 1

result["testid"] = "ordinate"
result["score"] = score / len(output)
if score == 0:
    result["status"] = "failed"
data.append(result)

# --------------------------- distance ---------------------------
result = {
    "testid": "1",
    "status": "success",
    "score": 0,
    "maximum marks" : 1,
    "message": ""
    }
output = {}
with open('./test/distance.txt', 'r', encoding='utf-8') as f:
    n = int(f.readline())
    for i in range(n):
        a, b, c, d = map(float, f.readline().split())
        try:
            output[i] = distance(Complex(a, b), Complex(c, d))
        except:
            output[i] = -1

score = 0
with open('./test/out/distance.txt', 'r', encoding='utf-8') as f:
    for i, o in output.items():
        c = f.readline()
        if o != None and  (abs(float(c)-o) < epsilon):
            score += 1

result["testid"] = "distance"
result["score"] = score / len(output)
if score == 0:
    result["status"] = "failed"
data.append(result)

# --------------------------- Record ---------------------------
overall['data'] = data
print(json.dumps(overall, indent=4))
with open('../evaluate.json', 'w') as f:
	json.dump(overall,f,indent=4)
