import json
import os

overall = {"data": []}
data = []

# Run tests
for i in range(1, 17):
    result = {
        "testid": str(i),
        "status": "success",
        "score": 0,
        "maximum marks": 1,
        "message": ""
    }

    # Run the code and capture output to out.txt
    os.system(f'timeout 3s python3 main.py {i} > out.txt')

    # Compare output using diff
    diff_status = os.system(
        f'diff -w out.txt outputs/output{i}.txt > /dev/null')

    if diff_status == 0:
        result["score"] = 1
    else:
        result["status"] = "failed"
        result["message"] = f"Output mismatch. Check your code for test case {i}."

    # Clean up
    os.system('rm out.txt')

    data.append(result)

# Record results
overall['data'] = data
print(json.dumps(overall, indent=4))

with open('../evaluate.json', 'w') as f:
    json.dump(overall, f, indent=4)
