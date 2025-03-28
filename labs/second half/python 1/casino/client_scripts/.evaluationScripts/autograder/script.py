'''Import required modules'''
import json
import os
overall = {"data": []
}
data = []
marks = {}


feedback = {}
testcase = [1, 2, 3, 10, 40, 50, 1000, 654321, 999998, 1000000]
expected_outputs = [1, 2, 4, 492, 567401756, 660641036, 937196411, 615247550, 39372206, 874273980]
for i in range(10):
    result = {
        "testid": str(i+1),
        "status": "success",
        "score": 0,
        "maximum marks" : 1,
        "message": ""
    }
    num = testcase[i]
    os.system(f'timeout 3s python3 main.py {num} > out.txt')
    result_num = 0
    try:
        f1 = open(f'out.txt','r',encoding='utf-8')
        result_num = int(f1.read())
    except ValueError:
        result["status"] = "failed"
        result["message"] = "Invalid output. Please make sure that the result is a single number. It is also possible that your code has timed out"
    if result_num == expected_outputs[i]:
         result["score"] = 1
    else:
        result["status"] = "failed"
        result["message"] = "Please check your script for line number " + str(i+1) + ".  Either the output is wrong, or your code has timed out."
    os.system('rm out.txt')
    i += 1
    data.append(result)

# --------------------------- Record ---------------------------
overall['data'] = data
print(json.dumps(overall, indent=4))
with open('../evaluate.json', 'w') as f:
	json.dump(overall,f,indent=4)
