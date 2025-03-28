import os
import json

overall = {
    "data": []
}

data = []

with open('../evaluate.json', 'w') as f:
    json.dump(overall,f,indent=4)

if not os.path.exists("email.awk"):
    result = {
      "testid": "1",
      "status": "failure",
      "score": 0,
      "maximum marks" : 1,
      "message": "email.awk file not found"
    }
    data.append(result)

else:

    os.system("rm TestCase1/output.txt")
    os.system("clear")
    #------------------------------test case 1---------------------------
    msg = "Correct output."
    status = "success"
    total = 1

    result = {
        "testid": "1",
        "status": "failure",
        "score": 0,
        "maximum marks" : 1,
        "message": ""
        }

    os.system("awk -f email.awk students.csv > TestCase1/output.txt")
    file1 = open('TestCase1/expected_output.txt', 'r')
    Lines1 = file1.readlines()
    file2 = open('TestCase1/output.txt', 'r')
    Lines2 = file2.readlines()

    if len(Lines1) < len(Lines2) :
        total = 0
        status = "failure"
        msg = "Wrong output, your output has some extra statments"
    elif len(Lines1) > len(Lines2) :
        total = 0
        status = "failure"
        msg = "Wrong output, your output is missing some statments"
    else :
        for i in range(len(Lines1)) :
            if Lines1[i].strip() != Lines2[i].strip() :
                total = 0
                status = "failure"
                msg = f"Wrong output, Expected statment : {i+1}'" + Lines1[i].strip() + "' Your output : '" + Lines2[i].strip() + "'"
                break
        
    result["status"] = status
    result["score"] = total
    result["message"] = msg

    data.append(result)

if not os.path.exists("email.sed"):
    result = {
      "testid": "1",
      "status": "failure",
      "score": 0,
      "maximum marks" : 1,
      "message": "email.sed file not found"
    }
    data.append(result)

else:
    os.system("rm TestCase1/output.txt")
    os.system("clear")

    #------------------------------test case 2 (sed)---------------------------
    msg = "Correct output."
    status = "success"
    total = 1

    result = {
        "testid": "1",
        "status": "failure",
        "score": 0,
        "maximum marks" : 1,
        "message": ""
        }

    os.system("sed -Ef email.sed students.csv > TestCase1/output.txt")
    file1 = open('TestCase1/expected_output.txt', 'r')
    Lines1 = file1.readlines()
    file2 = open('TestCase1/output.txt', 'r')
    Lines2 = file2.readlines()

    if len(Lines1) < len(Lines2) :
        total = 0
        status = "failure"
        msg = "Wrong output, your output has some extra statments"
    elif len(Lines1) > len(Lines2) :
        total = 0
        status = "failure"
        msg = "Wrong output, your output is missing some statments"
    else :
        for i in range(len(Lines1)) :
            if Lines1[i].strip() != Lines2[i].strip() :
                total = 0
                status = "failure"
                msg = f"Wrong output, Expected statment : {i+1}'" + Lines1[i].strip() + "' Your output : '" + Lines2[i].strip() + "'"
                break
        
    result["status"] = status
    result["score"] = total
    result["message"] = msg

    data.append(result)


overall['data'] = data
print(json.dumps(overall, indent=4))
with open('../evaluate.json', 'w') as f:
    json.dump(overall,f,indent=4)

