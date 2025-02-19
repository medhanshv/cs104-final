from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
import os
import json




overall = {"data": []
}

data = []
test_case_num = 10
all_test_inputs = [1, 2, 5, 10, 100, 603, 1000, 1401, 2808, 10000]
all_test_outputs = [0, 2, 5, 7, 97, 601, 997, 1399, 2803, 9973]

#------------------------------test cases---------------------------
current_directory = os.getcwd()
file_url = 'file://' + os.path.join(current_directory, 'basic.html')
# driver = webdriver.Chrome()
options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--headless')

options.add_argument('--disable-dev-shm-usage')
# os.system('ls')
chrome_service = Service('/usr/bin/chromedriver')
driver = webdriver.Chrome(service=chrome_service, options=options)
driver.get(file_url)
for i in range(0,test_case_num):
    
    # os.system("rm -f collect.txt expected_output.txt")

    msg = ""
    total = 0
    result = {
        "testid": "1",
        "status": "success",
        "score": 0,
        "maximum marks" : 1,
        "message": ""
        }
    # print("Hello Hello")
    # os.system('which chromedriver')
    # print("Hello Hello")
    # os.system('ls ..')
    # driver_path = '/home/.evaluationScripts/chromedriver'
    
    # time.sleep(2)
    input_number = all_test_inputs[i] # Replace with the desired number
    input_field = driver.find_element("id", "inputNumber")
    input_field.clear()
    input_field.send_keys(str(input_number))
    input_field.send_keys(Keys.RETURN)
    button = driver.find_element("xpath", "//button[text()='Find Largest Prime']")
    button.click()
    # time.sleep(1)

    # print("hello")
    # Retrieve the result
    result_element = driver.find_element("id", "result")
    result_output = result_element.text
    words = result_output.split()
    if words.__len__() > 0:
        last_word = words[-1]
        last_number = int(''.join(filter(str.isdigit, last_word)))
        if (last_number == all_test_outputs[i]):
            total = 1
            msg = "Correct Output!"
        else:
            msg = "Wrong Output!"
    else:
        msg = "Wrong Output!"

    

    result["testid"] = i + 1
    result["score"] = total
    result["message"] = msg
    data.append(result)
driver.quit()

overall['data'] = data
print(json.dumps(overall, indent=4))
with open('../evaluate.json', 'w') as f:
	json.dump(overall,f,indent=4)