import os
import json

overall = {"data": []
}

data = []

test_case_num = 3
submission_file_name = 'submission.sh'

# command = 'clear'
# os.system(command)
# os.system('if [ -e input ]; then mv input your_input; fi')
# os.system('if [ -e output ]; then mv output your_output; fi')

#------------------------------test cases---------------------------

for i in range(1,test_case_num+1):
    
    msg = ""
    total = 0
    result = {
        "testid": "1",
        "status": "success",
        "score": 0,
        "maximum marks" : 1,
        "message": ""
        }
    files=["result.csv","correct_output.csv"]
    
    for f in files:
        os.system(f"cp ./testcases/{i}/{f} .")
    # os.system("mkdir -p output")

    command=f"bash {submission_file_name} | sort > file.csv"
    rval1 = os.system(command)
  
    if rval1 == 0 :
        msg = msg + str("Script Executed Successfully. ")
    else :
        msg = msg + str("Error in Executing Script. ")
        result["status"]="failed"

    # os.system("touch output.txt; if [ -e output ]; then ls --color=none -ap output/ | sort > output.txt; fi")

    # os.system("if [ -e input ]; then rm -rf input; fi")
    # os.system("if [ -e output ]; then rm -rf output; fi")

    command=f"diff -Bw file.csv correct_output.csv > /dev/null 2>/dev/null"
    rval2 = os.system(command)
    
    if rval2 == 0 and rval1 == 0:
        total=total+1
        msg = msg + str("Test Case Passed.")
    else:
        msg = msg + str("Output is not as Expected. Check Testcase ")
        msg = msg + str(i) +"."

    result["testid"] = i
    result["score"] = total
    result["message"] = msg
    data.append(result)

os.system("rm -rf file.txt correct_output.csv 2> /dev/null")
# os.system('if [ -e your_input ]; then mv your_input input; fi')
# os.system('if [ -e your_output ]; then mv your_output output; fi')

overall['data'] = data
print(json.dumps(overall, indent=4))
with open('../evaluate.json', 'w') as f:
	json.dump(overall,f,indent=4)
