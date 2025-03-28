import os
import json

overall = {"data": []
}

data = []

test_case_num = 3
submission_file_name = 'submission.sh'
# solution_file_name = 'solution.sh'

# command = 'clear'
# os.system(command)
#------------------------------test cases---------------------------

for i in range(1,test_case_num+1):
    
    os.system("rm -f collect.txt expected_valid.txt expected_sorted.txt")

    msg = ""
    total = 0
    result = {
        "testid": "1",
        "status": "success",
        "score": 0,
        "maximum marks" : 2,
        "message": ""
        }
    # os.system(f"cp ../../labDirectory/submission.sh .")
    os.system(f"cp ./testcases/{i}/collect.txt ./testcases/{i}/expected_sorted.txt ./testcases/{i}/expected_valid.txt  .")
    os.system("ls")
    
    print("Executing Submission")
    command=f"bash {submission_file_name}"
    rval = os.system(command)
  
    if rval == 0 :
        msg = msg + str("Script Executed Successfully. ")
    else :
        msg = msg + str("Error in Executing Script. ")
        result["status"]="failed"
    
    # print("Hello World!")
    # command=f"bash {solution_file_name} > correct_output.txt"
    # os.system("grep -E '^[a-z]+[0-9]{2} [1-4] 22b[0-9]{4}@iitb\.ac\.in submission.sh$' collect.txt > correct_output.txt")
        
    command="diff -Bw valid.txt expected_valid.txt > /dev/null 2>/dev/null"
    rval = os.system(command)
    
    if rval == 0:
        total=total+1
        msg = msg + str("valid.txt correct. ")
    else:
        msg = msg + str("valid.txt is not as Expected. Check testcase ")
        msg = msg + str(i) +". "
    
    command="diff -Bw sorted.txt expected_sorted.txt > /dev/null 2>/dev/null"
    rval = os.system(command)
    
    if rval == 0:
        total=total+1
        msg = msg + str("sorted.txt correct. ")
    else:
        msg = msg + str("sorted.txt is not as Expected. Check testcase ")
        msg = msg + str(i) +". "

    result["testid"] = i
    result["score"] = total
    result["message"] = msg
    data.append(result)

os.system("rm -rf valid.txt sorted.txt expected_valid.txt expected_sorted.txt")

overall['data'] = data
print(json.dumps(overall, indent=4))
with open('../evaluate.json', 'w') as f:
	json.dump(overall,f,indent=4)
