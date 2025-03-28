import os
import json

overall = {"data": []}

data = []

test_case_num = 3
test_file_name = 'rollno_name_change.sh'
submission_file_name = 'submission.sh'
output_dir_name = 'output'
true_output_dir_name = 'true_output'

command=f"mkdir ./{output_dir_name}"
os.system(command)

for i in range(1,test_case_num+1):
    
    msg = ""
    total = 0
    result = {
        "testid": "1",
        "status": "success",
        "score": 0,
        "maximum marks" : 3,
        "message": ""
        }
    
    command=f"cp -R ./testcases/{i} ./{output_dir_name}"

    os.system(command)
    
    command=f"cp ./{submission_file_name} ./{output_dir_name}/{i}/{submission_file_name}"
    
    os.system(command)
    
    command=f"cd ./{output_dir_name}/{i}/ && bash {submission_file_name} mapping{i}.txt && rm {submission_file_name} && cd ../../"
    
    rval = os.system(command)
  
    if rval == 0 :
        msg = msg + str("Script Executed Successfully. ")
    else :
        msg = msg + str("Error in Executing Script. ")
        result["status"]="failed"
        
    command=f"diff -bw ./{true_output_dir_name}/{i}/ ./{output_dir_name}/{i}/ > /dev/null 2>/dev/null"
    rval2 = os.system(command)
    
    directory=f"./{output_dir_name}/{i}/"
    
    if rval2 == 0 and rval==0:
        total=total+3
        msg = msg + str("Test Case Passed.")
    elif rval==0:
        msg = msg + str("Directory structure is not as Expected. For the failing test case, refer to testcases/")
        msg = msg + str(i) +"/ . "

    result["testid"] = i
    result["score"] = total
    result["message"] = msg
    data.append(result)

command=f"rm -rf ./{output_dir_name}/"

os.system(command)

overall['data'] = data
print(json.dumps(overall, indent=4))
with open('../evaluate.json', 'w') as f:
	json.dump(overall,f,indent=4)
