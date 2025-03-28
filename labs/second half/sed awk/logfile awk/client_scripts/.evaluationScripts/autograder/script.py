import os
import json

data = []

numTests = 7

for i in range(1,numTests+1):
	result = {
		"testid": f"{i}",
		"status": "success",
		"score": 0,
		"maximum marks": 1,
		"message": "",
	}

	logFile = f"Tests/{i}/log.txt"
	output = f"output.txt"
	expected = f"Tests/{i}/Exoutput.txt"
	script = "check.awk"
	params = f"Tests/{i}/params.txt"
	cmd = f"awk -f {script} "
	file = open(params, "r")
	for line in file:
		line = line.strip()
		cmd += f" -v {line}"
	cmd += f" {logFile} > {output}"

	# print(cmd)
	#RUN COMMAND
	res = os.system(cmd)
	if res != 0:
		result["status"] = "failed"
		result["message"] = "Error in running script. "
		data.append(result)
		continue
	
	#READ CORRECT OUTPUT
	# print("Reading Expected Output")
	arrs = []
	file = open(expected, "r")
	final_result = -1
	for line in file:
		line = line.strip()
		line = line.split(" ")
		if(line[0] == "YES"):
			final_result = 1
			continue
		if(line[0] == "NO"):
			final_result = 0
			continue
		l = []
		for s in line:
			if(s != ''):
				l.append(int(s))
		arrs.append(sorted(line))
	
	# print("Reading Output")
	#READ OUTPUT
	arrs_out= []
	file = open(output, "r")
	final_result_out = -1
	for line in file:
		line = line.strip()
		line = line.split(" ")
		if(line[0] == "YES"):
			final_result_out = 1
			continue
		if(line[0] == "NO"):
			final_result_out = 0
			continue
		l = []
		for s in line:
			if(s != ''):
				l.append(int(s))
		arrs_out.append(sorted(line))

	# print("Matching Output ")
	#MATCH OUTPUT
	if(final_result == final_result_out):
		result["score"] += 0.5
		result["message"]+= "Final Result correct. "
	else:
		result["message"]+= "Final Result incorrect. "
	if(final_result == 1 and final_result_out == 1):
		if(len(arrs) == len(arrs_out)):
			all_correct = True
			for i in range(len(arrs)):
				if(arrs[i] != arrs_out[i]):
					all_correct = False
			if not all_correct:
				result["message"] += "Buffer contents incorrect. "
			else:
				result["score"]+=0.5
				result["message"] += "Buffer contents correct. "

		else:
			result["message"] += "Buffer contents incorrect. "
	elif (final_result == 0 and final_result_out ==0):
		result["score"] += 0.5

	data.append(result)

overall = {"data" : data}

print(json.dumps(overall, indent=4))
with open('../evaluate.json', 'w') as f:
    json.dump(overall,f,indent=4)
		
	
