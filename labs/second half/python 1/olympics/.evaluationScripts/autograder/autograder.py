'''Import required modules'''
import json
import os
overall = {"data": []
}
data = []
marks = {}

feedback = {}

for i in range(2):
    result = {
    "testid": "1",
    "status": "success",
    "score": 0,
    "maximum marks" : 1,
    "message": ""
    }
    result["testid"] = str(i+1)
    os.system(f'python3 main.py --path data/testcase{i + 1}/ > out.txt')
    f1 = open(f'out/testcase{i + 1}.txt', 'r', encoding='utf-8').readlines()
    f2 = open('out.txt', 'r', encoding='utf-8').readlines()
    if f1 == f2:
        result["score"] = 1
    else:
        result["status"] = "failed"
        result["message"] = "Incorrect output."
    data.append(result)
    os.system('rm out.txt')

# --------------------------- Record ---------------------------
overall['data'] = data
print(json.dumps(overall, indent=4))
with open('../evaluate.json', 'w') as f:
	json.dump(overall,f,indent=4)
