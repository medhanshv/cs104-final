import numpy as np
import os
import json
import matplotlib.pyplot as plt


os.system("rm -rf ../evaluate.json")

overall = {"data": []
}
data = []

result = {
    "testid": 1,
    "status": "success",
    "score": 0,
    "maximum marks" : 5,
    "message": ""
    }

# Find the difference between images plot.png and ../plot.png
img1 = plt.imread('plot.png')
img2 = plt.imread('../plot.png')
if img1.shape != img2.shape:
    result["message"] = "Images are of different shapes"
    result["status"] = "failed"
else:
    # print(img1.shape, img2.shape)
    difference = np.sum(img1 - img2)
    # if difference abs is < 1% of total pixels, then images are same
    sz = img1.shape[0]*img1.shape[1]*img1.shape[2]
    # print(difference/sz)
    if abs(difference/sz) < 0.0015:
        result["message"] = "Images are same"
        result["score"] = 5
    elif abs(difference/sz) < 0.003:
        result["message"] = "Images are almost same"
        result["score"] = 3
    elif abs(difference/sz) < 0.005:
        result["message"] = "Images are somewhat different"
        result["score"] = 2
    elif abs(difference/sz) > 0.1:
        result["message"] = "Images are very different"
        result["status"] = "failed"
        result["score"] = -5
    else:
        result["message"] = "Images are different"
        result["status"] = "failed"
        
data.append(result)
overall['data'] = data
print(json.dumps(overall, indent=4))
with open('../evaluate.json', 'w') as f:
	json.dump(overall,f,indent=4)