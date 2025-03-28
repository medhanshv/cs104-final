from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os
import time
import json

overall = {"data": []
}

data = []

def run_autograder(test_cases):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    # Create the webdriver instance
    chrome_service = Service('/usr/bin/chromedriver')
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

    try:
        # Open the index.html file in the browser
        current_directory = os.getcwd()
        file_url = 'file://' + os.path.join(current_directory, 'index.html')
        driver.get(file_url)

        # Wait for the page to load
        time.sleep(2)

        result = {
            "testid": 0,
            "status": "failed",
            "score": 0,
            "maximum marks" : 1,
            "message": ""
        }

        # Check if all required elements are present
        required_ids = ["fullName", "email", "password", "confirmPassword", "submit", "feedback"]
        missing_ids = [element_id for element_id in required_ids if not driver.find_elements(By.ID, element_id)]

        if missing_ids:
            result["message"] = result["message"] + f"Error: The following IDs are missing: {', '.join(missing_ids)}. "
            result["message"] = result["message"] + "Further checking won't proceed. Use correct ids. "
            data.append(result)
            return
        
        # Check input box types
        input_box_types = {
            "fullName": "text",
            "email": "email",
            "password": "password",
            "confirmPassword": "password",  # Assuming Confirm Password is also of type password
        }
        
        check = True
        for input_id, expected_type in input_box_types.items():
            input_element = driver.find_element(By.ID, input_id)
            actual_type = input_element.get_attribute("type")
            
            if actual_type != expected_type:
                result["message"] = result["message"] + f"Test Failed: Input box '{input_id}' has an incorrect 'type' attribute. Expected: {expected_type}, Actual: {actual_type}. "
                check = False
        if check==False:
            result["message"] = result["message"] + "Further checking won't proceed. Correct the 'type' attributes. "
            data.append(result)
            return
        
        # Check submit button type
        submit_button = driver.find_element(By.ID, "submit")
        expected_button_type = "button"
        actual_button_type = submit_button.get_attribute("type")

        if actual_button_type != expected_button_type:
            result["message"] = result["message"] + f"Test Failed: Submit button has an incorrect 'type' attribute. Expected: {expected_button_type}, Actual: {actual_button_type}. "
            result["message"] = result["message"] + "Further checking won't proceed. Correct the 'type' attributes. "
            data.append(result)
            return

        # Check the background color of the body
        body = driver.find_element(By.TAG_NAME, "body")
        body_color = body.value_of_css_property("background-color")
        if body_color != "rgba(240, 255, 255, 1)":  # Azure color
            result["message"] = result["message"] + f"Test Failed: Background color of the body is not azure. "
            result["message"] = result["message"] + "Further checking won't proceed. Correct the body background-color. "
            data.append(result)
            return
            
        result['status']="success"
        result['score']=1
        result['message']="Pre-requisites are correct."

        data.append(result)

        test_case_count = 1
        for test_case in test_cases:
            execute_test_case(driver, test_case, test_case_count)
            test_case_count += 1

    except Exception as e:
        print(f"Error: {str(e)}")
    finally:
        # Close the browser window
        driver.quit()

def execute_test_case(driver, test_case, test_case_count):
    message = ""
    total = 0
    testcase = {
        "testid": test_case_count,
        "status": "success",
        "score": 0,
        "maximum marks" : 2,
        "message": ""
    }

    full_name_input = driver.find_element(By.ID, "fullName")
    email_input = driver.find_element(By.ID, "email")
    password_input = driver.find_element(By.ID, "password")
    confirm_password_input = driver.find_element(By.ID, "confirmPassword")
    submit_button = driver.find_element(By.ID, "submit")

    # Input data into form fields
    full_name_input.clear()
    email_input.clear()
    password_input.clear()
    confirm_password_input.clear()

    full_name_input.send_keys(test_case["fullName"])
    email_input.send_keys(test_case["email"])
    password_input.send_keys(test_case["password"])
    confirm_password_input.send_keys(test_case["confirmPassword"])

    # Click the submit button
    submit_button.click()

    # Wait for feedback message
    time.sleep(2)

    # Get the feedback message and its style
    feedback_message = driver.find_element(By.ID, "feedback")
    feedback_message_text = feedback_message.text

    # Validate the feedback message content
    if feedback_message_text == test_case["expectedFeedback"]:
        message = message + f"Test Passed: {test_case['description']} - Feedback content is correct. "
        total += 2
    else:
        message = message + f"Test Failed: {test_case['description']} - Feedback content is incorrect. Expected: {test_case['expectedFeedback']}, Actual: {feedback_message_text} "
        testcase['status'] = "failed"

    testcase["message"] = message
    testcase["score"] = total

    data.append(testcase)

    test_case_count += 1


if __name__ == "__main__":
    # Define test cases

    rval = os.system('ls index.html style.css script.js > /dev/null 2> /dev/null')

    if rval != 0:
        data.append({
            "testid": "Pre-requisite check",
            "status": "failed",
            "score": 0,
            "maximum marks" : 1,
            "message": "Files not found. Further checking stopped."
        })
    else:

        test_cases = [
            {
                "description": "Valid Registration",
                "fullName": "John Doe",
                "email": "johndoe@example.com",
                "password": "password123",
                "confirmPassword": "password123",
                "expectedFeedback": "Registration successful!"
            },
            {
                "description": "Invalid Email",
                "fullName": "John Doe",
                "email": "john.doe",
                "password": "password123",
                "confirmPassword": "password123",
                "expectedFeedback": "Error: Invalid Email Address."
            },
            {
                "description": "Different Passwords",
                "fullName": "Kavya",
                "email": "kg@kg.com",
                "password": "password123",
                "confirmPassword": "password",
                "expectedFeedback": "Error: Passwords do not match."
            },
            {
                "description": "Incomplete fields",
                "fullName": "Kavya",
                "email": "",
                "password": "password123",
                "confirmPassword": "password123",
                "expectedFeedback": "Error: All fields are required."
            }
            # Add more test cases as needed
        ]

        run_autograder(test_cases)

    os.system('touch ../evaluate.json')
    os.system("clear")
    overall['data'] = data
    print(json.dumps(overall, indent=4))
    with open('../evaluate.json', 'w') as f:
        json.dump(overall,f,indent=4)
