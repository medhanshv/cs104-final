#!/usr/bin/python3
import json, os

os.system('clear')

# The data Structure for final results to be stored in evaluate.json
overall = {
    "data": []
}

# YOUR Evaluation Code here
dataSkel = {
            "testid": 1,
            "status": "fail",
            "score": 0,
            "maximum marks": 1,
            "message": "Autograder Failed!"
        }

os.system("cp /home/labDirectory/submission.sh /home/.evaluationScripts/autograder/submission.sh")
for i in range(1,6):
    tempDataSkel = dataSkel.copy()
    tempDataSkel["testid"] = i
    os.system("rm error.log")
    os.system(f"bash /home/.evaluationScripts/autograder/submission.sh /home/.evaluationScripts/autograder/testcases/{i}/grades.csv 2> error.log")
    if os.stat("error.log").st_size == 0:
        os.system("rm diff1.log diff2.log")
        os.system(f"diff -s ug23.csv /home/.evaluationScripts/autograder/testcases/{i}/ug23.csv >> diff1.log")
        os.system(f"diff -s ug24.csv /home/.evaluationScripts/autograder/testcases/{i}/ug24.csv >> diff2.log")
        diff1 = ""
        with open("diff1.log", "rt") as f:
            diff1 = f.read()
        diff2 = ""
        with open("diff2.log", "rt") as f:
            diff2 = f.read()
        if "are identical" in diff1 and "are identical" in diff2:
            tempDataSkel["message"] = "Testcase passed!"
            tempDataSkel["status"] = "success"
            tempDataSkel["score"] = 1
        else:
            tempDataSkel["message"] = ""
            if "are identical" not in diff1:
                tempDataSkel["message"] += "ug23.csv is not as expected! "
            if "are identical" not in diff2:
                tempDataSkel["message"] += "ug24.csv is not as expected! "
        os.system("rm diff1.log diff2.log error.log")
    else:
        tempDataSkel["message"] = "Execution of submission.sh failed! Error-log: "
        with open("error.log", "rt") as f:
            tempDataSkel["message"] += f.read()
    overall["data"].append(tempDataSkel)

# Store evaluation results
with open('/home/.evaluationScripts/evaluate.json','w',encoding='utf-8') as f:
    json.dump(overall,f,indent=4)

# Show evaluation results
with open('/home/.evaluationScripts/evaluate.json','r',encoding='utf-8') as f:
    for line in f.readlines():
        print(line)