# Autograder script for makefile lab

import os
import json 
import subprocess 


overall = {"data" : []}
data = []
main_files = ['restore.cpp', 'powerful.cpp']
src_cpp_files = ['nohehe.cpp', 'hehe.cpp', 'haha.cpp']
src_h_files = ['deck.h', 'card.h', 'player.h']
all_files = main_files + src_cpp_files + src_h_files + ['script.py', 'Makefile']

msg = ""
total = 0
result = {
    "testid": "1",
    "status": "success",
    "score": 0,
    "maximum marks" : 4,
    "message": ""
    }

def find_compiler_options(file, strings_to_match):
    strings_matched = {}
    for string in strings_to_match:
        strings_matched[string] = 0
    readelf_output = subprocess.check_output(['readelf', '-p', '.GCC.command.line', file])
    readelf_output = readelf_output.decode('utf-8')
    lines = readelf_output.split('\n')
    for line in lines:
        for string in strings_to_match:
            if string in line:
                strings_matched[string] = 1
    return strings_matched

def check_make_clean_in_dir(path, files, should_exit):
    iswrong = 0
    global msg
    for file in os.scandir(path=path):
        if(file.is_file()):
            if file.name not in files:
                iswrong = 1
                msg += f"Make restore did not regain its original state."
                print(f"{file.name} not in {files}")
                if should_exit:
                    result["score"] = total
                    result["message"] = msg
                    data.append(result)
                    overall["data"] = data

                    with open("../../evaluate.json", "w") as f:
                        json.dump(overall, f, indent=4)
                    exit(0)
        else:
            # If the file is a directory
            msg += f"Unknown directories found after make clean."
            # print(f"Unknown directories in {path}: {file.name}")
            iswrong = 1
            if should_exit:
                result["score"] = total
                result["message"] = msg
                data.append(result)
                overall["data"] = data

                with open("../../evaluate.json", "w") as f:
                    json.dump(overall, f, indent=4)
                exit(0)
        
    # Also check if all the files are present in the directory path
    for file in files:
        if not os.path.exists(os.path.join(path, file)):
            iswrong = 1
            msg += f"Make restore removed some cpp or header files."
            if should_exit:
                result["score"] = total
                result["message"] = msg
                data.append(result)
                overall["data"] = data

                with open("../../evaluate.json", "w") as f:
                    json.dump(overall, f, indent=4)
                exit(0)
    return 1-iswrong

# First -- make clean
os.system('make restore 2>/dev/null')


print("***CHECKING MAKE RESTORE***")
check_make_clean_in_dir(path='.', files=all_files, should_exit=True)

# Second -- make
print("***CHECKING MAKE***")
os.system('make 2>/dev/null')
expected_obj_files = ['hehe.o', 'nohehe.o', 'haha.o']
expected_executables = ['restore', 'powerful']

# Check if all the .o files are present
# Check if all the executables are present
# Check if the executables are working by 
# running them and comparing output with expected output
# 0.5 mark
expected_obj_files_missing = False
for file in expected_obj_files:
    if not os.path.exists(file):
        expected_obj_files_missing = True
        # msg += f"Make did not create {file}."
    else:
        total += 0.1
if(expected_obj_files_missing):
    msg += "Make did not create required three .o files."

expected_executables_missing = False
expected_executables_wrong_output = False
for file in expected_executables:
    if not os.path.exists(file):
        expected_executables_missing = True
        # msg += f"Make did not create {file}."
    else:
        command = f"./{file} > output.txt 2>/dev/null"
        os.system(command)
        command = f"diff -Bw output.txt ../EVALUATION/{file}.txt"
        val = os.system(command)
        if val == 0:
            total += 0.1
        else:
            # msg += f"{file} output is not as expected."
            expected_executables_wrong_output = True

if(expected_executables_missing): 
    msg += "Make did not create required two executables."
if(expected_executables_wrong_output):
    msg += "Created executables do not match expected output."

os.system("rm -f output.txt")
# Also check if there are no other files apart from the original files + expected executables+obj files
# if fails then -0.5 marks
for file in os.scandir(path='.'):
    if(file.is_file()):
        if file.name not in all_files + expected_executables + expected_obj_files:
            msg += f"Make created some extra files."
            total -= 0.25
            break
    else:
        # If the file is a directory
        msg += f"Unknown directories in current directory: {file.name}"
        total -= 0.25
        break

if not total == 0.5:
    result["score"] = total
    result["message"] = msg
    data.append(result)
    overall["data"] = data

    with open("../../evaluate.json", "w") as f:
        json.dump(overall, f, indent=4)
    exit(0)

# Third -- make clean again
print("***CHECKING MAKE RESTORE***")
os.system('make restore 2>/dev/null')

# Do the same checks as before -- 0.5 marks -- make restore
total += check_make_clean_in_dir(path='.', files=all_files, should_exit=False)/2

if not total == 1:
    result["score"] = total
    result["message"] = msg
    data.append(result)
    overall["data"] = data

    with open("../../evaluate.json", "w") as f:
        json.dump(overall, f, indent=4)
    exit(0)
## Make with CXX Flags -- 1 mark
print("***CHECKING CXXFLAGS***")
if(total == 1):
    os.system("make CXXFLAGS='-frecord-gcc-switches -g -O2 --std=c++14' 2>/dev/null")
    strings_to_match = ['GNU C++14', '-g ', '-O2']
    local = 0
    for file in expected_obj_files:
        strings_matched = find_compiler_options(file, strings_to_match)
        if strings_matched['GNU C++14'] and strings_matched['-g '] and strings_matched['-O2']:
            local += 1
    for file in expected_executables:
        strings_matched = find_compiler_options(file, strings_to_match)
        if strings_matched['GNU C++14'] and strings_matched['-g '] and strings_matched['-O2']:
            local += 1

    if local < 5:
        msg += "Makefile does not handle CXXFLAGS properly."
    total += local/5.0 # 1 mark

    os.system('make restore')

# Part 2

print("***CHECKING RECOMPILATION***")
if(total == 2):
    ## TC 1: Change restore.cpp
    ## Stats should only change for restore and no other files
    os.system("make")

    older_stats = {}
    for file in expected_executables:
        older_stats[file] = os.stat(file).st_mtime
    for file in expected_obj_files:
        older_stats[file] = os.stat(file).st_mtime

    os.system(f"cp restore.cpp restore.cpp.bak")
    os.system(f"cp restore.cpp.bak restore.cpp")
    os.system(f"rm restore.cpp.bak")

    os.system("sleep 2")
    os.system("make")

    local_score = 0
    newer_stats = {}
    for file in expected_executables:
        newer_stats[file] = os.stat(file).st_mtime
    for file in expected_obj_files:
        newer_stats[file] = os.stat(file).st_mtime

    for file in older_stats.keys():
        if file == 'restore':
            if older_stats[file] != newer_stats[file]:
                local_score += 1
        else:
            if older_stats[file] == newer_stats[file]:
                local_score += 1

    total += (local_score/5.0) # 1 mark

    ## TC 2: Change .h and check stats
    ## Stats should change for player.o and main

    older_stats = {}
    for file in expected_executables:
        older_stats[file] = os.stat(file).st_mtime
    for file in expected_obj_files:
        older_stats[file] = os.stat(file).st_mtime

    newer_stats = {}

    os.system(f"cp player.h player.h.bak")
    os.system(f"cp player.h.bak player.h")
    os.system(f"rm player.h.bak")

    os.system("sleep 2")
    os.system("make")

    for file in expected_executables:
        newer_stats[file] = os.stat(file).st_mtime
    for file in expected_obj_files:
        newer_stats[file] = os.stat(file).st_mtime

    local_score = 0
    for file in older_stats.keys():
        if file == 'haha.o' or file == 'restore':
            if older_stats[file] != newer_stats[file]:
                local_score += 1
        else:
            if older_stats[file] == newer_stats[file]:
                local_score += 1
        
    total += (local_score/5.0) # 1 mark

    os.system('make restore')

    if total < 4:
        msg += "Makefile does not handle dependencies properly."

if(total == 4):
    msg += "Congrats! All public tests passed"

result["score"] = total
result["message"] = msg
data.append(result)
overall["data"] = data
print(json.dumps(overall, indent=4))
with open("../../evaluate.json", "w") as f:
    json.dump(overall, f, indent=4)
os.system('rm -f *.o 2>/dev/null')
os.system('rm -f main[0-1] 2>/dev/null')
exit(0)
