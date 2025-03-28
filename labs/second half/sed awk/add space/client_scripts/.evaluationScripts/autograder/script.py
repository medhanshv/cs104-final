import os
import json

num_testcases = 2

data = []



for i in range(1,num_testcases+1):
	result = {
		"status": "success",
		"testid":  1,
		"score":  0,
		"maximum marks": 1,
		"message": ""
	}
      
	code = f"testcases/{i}/test.py"
	expected = f"testcases/{i}/expected.py"
	output = f"output.py"
	script = f"add_space.sed"
	res = os.system(f"sed -Ef {script} {code} > {output}")
	if res != 0:
		result["status"] = "failed"
		result["message"] = "Failed to execute script. "
		data.append(result)
		continue
	res2 = os.system(f"diff {output} {expected}")
	if res2 == 0:
		result["score"]+=1
		result["message"]+= f"Testcase {i} passed"
	else:
		result["message"]+= f"Testcase {i} failed. Check output. "
	data.append(result)

overall = {"data" : data}

filename = "../evaluate.json"


with open(filename, 'w') as file:
    json.dump(overall, file, indent=4)

