import os
import json

overall = {"data": []
}

test_cases = [3, 4, 5]

data = []
os.system('clear')

for j in range(len(test_cases)):
    for k in range(test_cases[j]):
        testid = f"q{j+1}_{k+1}"
        result = {
            "testid": testid,
            "status": "failure",
            "score": 0,
            "maximum marks" : 0.5,
            "message": ""
        }
        data.append(result)

overall['data'] = data
os.system('clear')
with open('../evaluate.json', 'w') as f:
    json.dump(overall,f,indent=4)
os.system('rm -f output.txt 2>/dev/null')

data = []
os.system('clear')

if not os.path.exists("language.py"):
    exit()
    
for j in range(len(test_cases)):
    for k in range(test_cases[j]):
        testid = f"q{j+1}_{k+1}"
        msg = ""
        result = {
            "testid": testid,
            "status": "failure",
            "score": 0,
            "maximum marks" : 0.5,
            "message": ""
        }
        
        command=f"timeout 5s testcases/{testid}.sh > output.txt 2>/dev/null"
        val1 = os.system(command)

        command=f"diff -Bw output.txt testcases/out_{testid}.txt 2>/dev/null"
        val2 = os.system(command)

        if(val1==0 and val2==0):
            result['status'] = "success"
            result['score'] = 0.5
        else:
            result["message"] = f"Output not as expected on case {testid}. "

        data.append(result)
        
overall['data'] = data
os.system('clear')
print(json.dumps(overall, indent=4))
with open('../evaluate.json', 'w') as f:
	json.dump(overall,f,indent=4)
os.system('rm -f output.txt 2>/dev/null')