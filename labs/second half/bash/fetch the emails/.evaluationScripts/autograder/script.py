import os
import json
import subprocess
import random
import string

overall = {"data": []
}

data = []

test_case_num = 5
submission_file_name = 'getEmails.sh'

command = 'clear'
os.system(command)
#------------------------------test cases---------------------------

for i in range(1,test_case_num+1):
	
	os.system("rm -f codeoutput.txt input.txt output.txt")

	msg = ""
	total = 0
	result = {
		"testid": "1",
		"status": "success",
		"score": 0,
		"maximum marks" : 6,
		"message": ""
		}
	
	os.system(f"cp -R ./testcases/{i}/input.txt .")
	os.system(f"cp -R ./testcases/{i}/output.txt .")
	# os.system("cp /home/labDirectory/getEmails.sh .")
	try:
		output = subprocess.check_output(f"bash {submission_file_name}", shell=True)

		# Decode the output from bytes to string (assuming UTF-8 encoding)
		output_str = output.decode('utf-8').strip()

		if output_str == "Usage: ./getEmails.sh <file>":
			msg = msg + str("None Argument -> Error message is shown correctly!! ")
			total=total+1
		else:
			msg = msg + str("None Argument -> Wrong error message shown! Check testcase ")
			msg = msg + str(i) +"/ ."
	except subprocess.CalledProcessError as error:
		output_str = error.output.decode('utf-8').strip()
		if output_str == "Usage: ./getEmails.sh <file>":
			msg = msg + str("None Argument -> Error message is shown correctly!! ")
			total=total+1
		else:
			msg = msg + str("None Argument -> Wrong error message shown! Check testcase ")
			msg = msg + str(i) +"/ ."
	try:
		output = subprocess.check_output(f"bash {submission_file_name} hello.txt hello2.txt", shell=True)

		# Decode the output from bytes to string (assuming UTF-8 encoding)
		output_str = output.decode('utf-8').strip()

		if output_str == "Usage: ./getEmails.sh <file>":
			msg = msg + str("Multi Argument -> Error message is shown correctly!! ")
			total=total+1
		else:
			msg = msg + str("Multi Argument -> Wrong error message shown! Check testcase ")
			msg = msg + str(i) +"/ ."
	except subprocess.CalledProcessError as error:
		output_str = error.output.decode('utf-8').strip()

		if output_str == "Usage: ./getEmails.sh <file>":
			msg = msg + str("Multi Argument -> Error message is shown correctly!! ")
			total=total+1
		else:
			msg = msg + str("Multi Argument -> Wrong error message shown! Check testcase ")
			msg = msg + str(i) +"/ ."
	try:
		dummy_output = "hello_" + ''.join(random.choices(string.ascii_lowercase,k=10))
		output = subprocess.check_output(f"bash {submission_file_name} {dummy_output}", shell=True)

		# Decode the output from bytes to string (assuming UTF-8 encoding)
		output_str = output.decode('utf-8').strip()

		if output_str == "Input File doesn't exist":
			msg = msg + str("Non Existent File -> Error message is shown correctly!! ")
			total=total+1
		else:
			msg = msg + str("Non Existent File -> Wrong error message shown! Check testcase ")
			msg = msg + str(i) +"/ ."
	except subprocess.CalledProcessError as error:
		output_str = error.output.decode('utf-8').strip()

		if output_str == "Input File doesn't exist":
			msg = msg + str("Non Existent File -> Error message is shown correctly!! ")
			total=total+1
		else:
			msg = msg + str("Non Existent File -> Wrong error message shown! Check testcase ")
			msg = msg + str(i) +"/ ."

	command=f"bash {submission_file_name} input.txt"
	rval = os.system(command)
	
	if rval == 0 :
		msg = msg + str("Script Executed Successfully. ")
	else :
		msg = msg + str("Error in Executing Script. ")
		result["status"]="failed"
	
	rval = os.system("cat emails.txt sortedEmails.txt cseEmails.txt | md5sum | cut -d' ' -f1 > codeoutput.txt")
	
	if rval == 0 :
		msg = msg + str("Output Files generated Successfully! ")
	else :
		msg = msg + str("Error in Output Files generation!")
		result["status"]="failed"

	command="diff -Bw codeoutput.txt output.txt > /dev/null 2>/dev/null"
	
	rval = os.system(command)
	
	if rval == 0:
		total=total+3
		msg = msg + str("All the text files are correctly generated! ")
	else:
		msg = msg + str("Wrong Text files generated! Check testcase ")
		msg = msg + str(i) +"/ ."
	

	os.system("rm -f cseEmails.txt emails.txt sortedEmails.txt codeoutput.txt input.txt output.txt")

	result["testid"] = i
	result["score"] = total
	result["message"] = msg
	data.append(result)

overall['data'] = data
print(json.dumps(overall, indent=4))
with open('../evaluate.json', 'w') as f:
	json.dump(overall,f,indent=4)

