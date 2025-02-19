# Autograder script for makefile lab

import os
import json 
import subprocess 

overall = {"data" : []}
data = []
main_files = [f'main{i}.cpp' for i in range(1, 10)]
src1_files = ['comp.cpp', 'comp.h', 'find.cpp', 'find.h', 'ops.cpp', 'ops.h']
src2_files = ['add.cpp', 'add.h', 'rem.cpp', 'rem.h']

msg = ""
total = 0
result = {
    "testid": "1",
    "status": "success",
    "score": 0,
    "maximum marks" : 30,
    "message": ""
    }

def check_make_clean_in_dir(path, files, should_exit):
    iswrong = 0
    global msg
    for file in os.scandir(path=path):
        if(file.is_file()):
            if file.name not in files:
                iswrong = 1
                msg += f"Make clean did not remove all files in {path}."
                # print(f"Make clean did not remove file in {path}: {file.name}")
                if should_exit:
                    result["score"] = total
                    result["message"] = msg
                    data.append(result)
                    overall["data"] = data

                    with open("../evaluate.json", "w") as f:
                        json.dump(overall, f, indent=4)
                    exit(0)
        else:
            # If the file is a directory
            msg += f"Unknown directories in {path}."
            # print(f"Unknown directories in {path}: {file.name}")
            iswrong = 1
            if should_exit:
                result["score"] = total
                result["message"] = msg
                data.append(result)
                overall["data"] = data

                with open("../evaluate.json", "w") as f:
                    json.dump(overall, f, indent=4)
                exit(0)
        
    # Also check if all the files are present in the directory path
    for file in files:
        if not os.path.exists(os.path.join(path, file)):
            iswrong = 1
            msg += f"Make clean removed some cpp or header files in {path}."
            if should_exit:
                result["score"] = total
                result["message"] = msg
                data.append(result)
                overall["data"] = data

                with open("../evaluate.json", "w") as f:
                    json.dump(overall, f, indent=4)
                exit(0)
    return 1-iswrong
# First -- make clean
os.system('make clean 2>/dev/null')

check_make_clean_in_dir(path='./src/src1', files=src1_files, should_exit=True)
check_make_clean_in_dir(path='./src/src2', files=src2_files, should_exit=True)
check_make_clean_in_dir(path='./main', files=main_files, should_exit=True)

# Second -- make
os.system('make 2>/dev/null')
expected_obj_files = ['comp.o', 'find.o', 'ops.o', 'add.o', 'rem.o']
expected_executables = [f'main{i}' for i in range(1,10)]

# Check if all the .o files are present
# Check if all the executables are present
# Check if the executables are working by 
# running them and comparing output with expected output
# 7 marks
for file in expected_obj_files:
    if not os.path.exists(file):
        msg += f"Make did not create {file}."
    else:
        total += 0.5

for file in expected_executables:
    if not os.path.exists(file):
        msg += f"Make did not create {file}."
    else:
        command = f"./{file} > output.txt 2>/dev/null"
        os.system(command)
        command = f"diff -Bw output.txt EVALUATION/{file}.txt" # RECHECK LATER
        val = os.system(command)
        if val == 0:
            total += 0.5
        else:
            msg += f"{file} output is not as expected."

os.system("rm output.txt")

# Third -- make clean again
os.system('make clean 2>/dev/null')


# Do the same checks as before -- 3 marks
total += check_make_clean_in_dir(path='./src/src1', files=src1_files, should_exit=False)
total += check_make_clean_in_dir(path='./src/src2', files=src2_files, should_exit=False)
total += check_make_clean_in_dir(path='./main', files=main_files, should_exit=False)

# Part 2 -- Check if the very purpose of makefile is fulfilled
# 10 marks

if(total == 10):
    # TC 1: Change main1.cpp, main2.cpp and main4.cpp and check stats of all
    # generated executables and object files. It should only change main1, main2 and main4
    os.system("make")

    older_stats = {}
    for file in expected_executables:
        older_stats[file] = os.stat(file).st_mtime
    for file in expected_obj_files:
        older_stats[file] = os.stat(file).st_mtime

    for file in [f'main/main{i}.cpp' for i in [1,2,4]]:
        os.system(f"cp {file} {file}.bak")
        os.system(f"cp {file}.bak {file}")
        os.system(f"rm {file}.bak")

    os.system("sleep 2")
    os.system("make")
    local_score = 0
    newer_stats = {}
    for file in expected_executables:
        newer_stats[file] = os.stat(file).st_mtime
    for file in expected_obj_files:
        newer_stats[file] = os.stat(file).st_mtime

    for file in older_stats.keys():
        if file not in [f'main{i}' for i in [1,2,4]]:
            if older_stats[file] == newer_stats[file]:
                local_score += 1
        else:
            if older_stats[file] != newer_stats[file]:
                local_score += 1
    total += (local_score/14)*5.0 # 5 marks

    ## TC 2: Change src1/comp.cpp and src2/add.cpp and check stats of all
    # generated executables and object files. It should only change comp.o and add.o
    # And all main files should be recompiled

    older_stats = {}
    for file in expected_executables:
        older_stats[file] = os.stat(file).st_mtime
    for file in expected_obj_files:
        older_stats[file] = os.stat(file).st_mtime

    for file in [f'src/src1/comp.cpp', f'src/src2/add.cpp']:
        os.system(f"cp {file} {file}.bak")
        os.system(f"cp {file}.bak {file}")
        os.system(f"rm {file}.bak")

    os.system("sleep 2")
    os.system("make")

    newer_stats = {}
    for file in expected_executables:
        newer_stats[file] = os.stat(file).st_mtime
    for file in expected_obj_files:
        newer_stats[file] = os.stat(file).st_mtime

    local_score = 0
    
    for file in older_stats.keys():
        if file in [f'main{i}' for i in range(1,10)]:
            if older_stats[file] != newer_stats[file]:
                local_score += 1
        elif file in ['comp.o', 'add.o']:
            if older_stats[file] != newer_stats[file]:
                local_score += 1
        else:
            if older_stats[file] == newer_stats[file]:
                local_score += 1

    total += (local_score/14)*5.0 # 5 marks

    os.system('make clean')



#If all working fine, then checking if patterns implemented
if total == 20:
    os.system("cp main/main1.cpp main/main10.cpp")
    os.system("cp main/main2.cpp main/main20.cpp")

    os.system('make main10 2>/dev/null')
    os.system('make main20 2>/dev/null')

    os.system("cp src/src1/comp.cpp src/src1/comp2.cpp")
    os.system("cp src/src1/comp.h src/src1/comp2.h")
    os.system("cp src/src2/add.cpp src/src2/add2.cpp")
    os.system("cp src/src2/add.h src/src2/add2.h")

    os.system('make comp2.o 2>/dev/null')
    os.system('make add2.o 2>/dev/null')

    expected_files = ["main10", "main20", "comp2.o", "add2.o"]
    local_score = 0
    for file in expected_files:
        if os.path.exists(file):
            local_score += 2.5
    if local_score != 10:
        msg += "Patterns not/incorrectly implemented."
    
    total += local_score

    os.system("rm -f main/main10.cpp main/main20.cpp")
    os.system("rm -f src/src1/comp2.cpp src/src1/comp2.h src/src2/add2.cpp src/src2/add2.h")


    os.system('make clean 2>/dev/null')
    for file in expected_files:
        if os.path.exists(file):
            total -= 2
            msg += "Make clean doesn't restore the original files."
            break

result["score"] = total
result["message"] = msg
data.append(result)
overall["data"] = data
print(json.dumps(overall, indent=4))
with open("../evaluate.json", "w") as f:
    json.dump(overall, f, indent=4)
os.system('rm *.o 2>/dev/null')
os.system('rm main[0-9] 2>/dev/null')
exit(0)
