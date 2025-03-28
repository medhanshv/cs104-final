import os
import json

overall = {"data": []
}

data = []

test_case_num=5

result = {
        "testid": "0",
        "status": "success",
        "score": 0,
        "maximum marks" : 1,
        "message": ""
        }


os.system("rm -rf bigdirectory")
os.system("rm -rf bigdirectory")

     
args = ["-regex \".*file_[0-9][0-9][0-9][0-9]\\.txt\" ",
"-name \"*.log\" ",
"-perm 777 ",
"-mtime 0 ",
"-mtime +7  -size +100c "]

os.system ("echo >> submission.sh")
os.system(f"echo \"tar -xf files_backup.tar.gz >/dev/null 2>/dev/null\" >> submission.sh")
for i in range(1,6):
    os.system(f"echo \"find bigdirectory -type f {args[i-1]} > {i}_corr.txt\" >> submission.sh")

res=os.system("bash submission.sh")



if res!=0:
    print("ERROR IN SCRIPT")
    result["message"]="Failed to execute script."
    result["status"]="failed"
    data.append(result)
else:
	result["message"]="Script Executed Successfully."


if res==0:
    for i in range(1,test_case_num+1):
        msg = ""
        total = 0
        result = {
            "testid": f"{i}",
            "status": "success",
            "score": 0,
            "maximum marks" : 1,
            "message": ""
            }
        
        # print(f"COMMAND : find bigdirectory -type f {args[i-1]} > {i}_corr.txt")
        
        # print(f"SED COMMAND: sed 's/\\.\\/\\(.*\\)/\\1/' {i}.txt > temp")
        os.system(f"sed 's/\\.\\/\\(.*\\)/\\1/' {i}.txt > temp")
        os.system(f"mv temp  {i}.txt")
        print(f"Diffing part {i}")
        command=f"diff -Bw {i}.txt {i}_corr.txt "# /dev/null 2>/dev/null"
        rval = os.system(command)
        
        if rval == 0:
            total=total+1
            msg = msg + str("Output correct")
        else:
            msg = msg + str("Output incorrect. Check Part ")
            result["status"] = "Failed"
            msg = msg + str(i) +". "

        result["score"] = total
        result["message"] = msg
        data.append(result)

os.system("rm -rf 1_corr.txt 2_corr.txt 3_corr.txt 4_corr.txt 5_corr.txt files.tar.gz files_backup.tar.gz 1.txt 2.txt 3.txt 4.txt 5.txt")

overall['data'] = data
print(json.dumps(overall, indent=4))
with open('../evaluate.json', 'w') as f:
	json.dump(overall,f,indent=4)
