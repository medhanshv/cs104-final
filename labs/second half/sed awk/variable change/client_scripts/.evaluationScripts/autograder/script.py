import os
import json

overall = {
    "data": []
}

data = []

result = {
      "testid": "BOSS",
      "status": "failure",
      "score": 0,
      "maximum marks" : 1,
      "message": ""
    }

with open('../evaluate.json', 'w') as f:
    json.dump(overall,f,indent=4)

if not os.path.exists('var_change.sed') :
    result["message"] = "var_change.sed file is not present in the current directory"
    data.append(result)
    overall['data'] = data
    print(json.dumps(overall, indent=4))
    with open('../evaluate.json', 'w') as f:
        json.dump(overall,f,indent=4)
    exit()


#------------------------------test case 1---------------------------
os.system("rm TestCase1/output.txt")

msg = "Correct output."
total = 1
status = "success"

os.system("sed -f var_change.sed TestCase1/test1.cpp > TestCase1/output.txt")
file1 = open('TestCase1/expected_output.txt', 'r')
Lines1 = file1.readlines()
file2 = open('TestCase1/output.txt', 'r')
Lines2 = file2.readlines()

if len(Lines1) < len(Lines2) :
    total = 0
    status = "failure"
    msg = "Wrong output, your output has some extra statements"
elif len(Lines1) > len(Lines2) :
    total = 0
    status = "failure"
    msg = "Wrong output, your output has some missing statements"
else :
    for i in range(len(Lines1)) :
        if Lines1[i].strip() != Lines2[i].strip() :
            total = 0
            status = "failure"
            msg = f"Wrong output, Expected statment {i+1}: '" + Lines1[i].strip() + "' Your output : '" + Lines2[i].strip() + "'"
            break

cr = result.copy() 
cr["testid"] = "1"
cr["score"] = total
cr["message"] = msg
cr["status"] = status

data.append(cr)
os.system("rm TestCase1/output.txt")


#------------------------------test case 2---------------------------
os.system("rm TestCase2/output.txt")

msg = "Correct output."
total = 1
status = "success"

os.system("sed -f var_change.sed TestCase2/test2.cpp > TestCase2/output.txt")
file1 = open('TestCase2/expected_output.txt', 'r')
Lines1 = file1.readlines()
file2 = open('TestCase2/output.txt', 'r')
Lines2 = file2.readlines()

if len(Lines1) < len(Lines2) :
    total = 0
    status = "failure"
    msg = "Wrong output, your output has some extra statements"
elif len(Lines1) > len(Lines2) :
    total = 0
    status = "failure"
    msg = "Wrong output, your output has some missing statements"
else :
    for i in range(len(Lines1)) :
        if Lines1[i].strip() != Lines2[i].strip() :
            total = 0
            status = "failure"
            msg = f"Wrong output, Expected statment {i+1}: '" + Lines1[i].strip() + "' Your output : '" + Lines2[i].strip() + "'"
            break

cr = result.copy() 
cr["testid"] = "2"
cr["score"] = total
cr["message"] = msg
cr["status"] = status

data.append(cr)
os.system("rm TestCase2/output.txt")

#------------------------------test case 3---------------------------
os.system("rm TestCase3/output.txt")

msg = "Correct output."
total = 1
status = "success"

os.system("sed -f var_change.sed TestCase3/test3.cpp > TestCase3/output.txt")
file1 = open('TestCase3/expected_output.txt', 'r')
Lines1 = file1.readlines()
file2 = open('TestCase3/output.txt', 'r')
Lines2 = file2.readlines()

if len(Lines1) < len(Lines2) :
    total = 0
    status = "failure"
    msg = "Wrong output, your output has some extra statements"
elif len(Lines1) > len(Lines2) :
    total = 0
    status = "failure"
    msg = "Wrong output, your output has some missing statements"
else :
    for i in range(len(Lines1)) :
        if Lines1[i].strip() != Lines2[i].strip() :
            total = 0
            status = "failure"
            msg = f"Wrong output, Expected statment {i+1}: '" + Lines1[i].strip() + "' Your output : '" + Lines2[i].strip() + "'"
            break

cr = result.copy() 
cr["testid"] = "3"
cr["score"] = total
cr["message"] = msg
cr["status"] = status

data.append(cr)
os.system("rm TestCase3/output.txt")

## Dumping the result
overall['data'] = data
print(json.dumps(overall, indent=4))
with open('../evaluate.json', 'w') as f:
    json.dump(overall,f,indent=4)

