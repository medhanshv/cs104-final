from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import os
import time
import json

overall = {"data": []}

data = []

# Testcases for HTML and CSS checks
testcases = [
    {"Input": "2", "Alert": "Thank you for your response!"},
    {"Input": "7", "Alert": "Thank you for your response!"},
    {"Input": "-1", "Alert": "Invalid Response. Try again, please!"},
    {"Input": "", "Alert": "Invalid Response. Try again, please!"},
    {"Input": "11", "Alert": "Invalid Response. Try again, please!"},
]

# -----------------------------------------------Starting Chromedriver---------------------------------------------------
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_service = Service("/usr/bin/chromedriver")
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
current_directory = os.getcwd()
file_url = "file://" + os.path.join(current_directory, "survey.html")
driver.get(file_url)
time.sleep(2)
# ----------------------------------------------------------------------------------------------------------------------


# Function to check HTML elements and CSS styles
def grade_against_testcases():
    message = ""
    try:
        # Checking Title
        if driver.title == "CSE Trip Survey":
            data.append(
                {
                    "testid": "Title",
                    "status": "success",
                    "score": 0.25,
                    "maximum marks": 0.25,
                    "message": "Page title is correct.",
                }
            )
        else:
            data.append(
                {
                    "testid": "Title",
                    "status": "failed",
                    "score": 0,
                    "maximum marks": 0.25,
                    "message": "Error: Page title is wrong or not set.",
                }
            )
    except Exception as e:
        print(e)

    # -------------------------------------------------Checking Heading-------------------------------------------------
    try:
        h1_element = driver.find_element(By.TAG_NAME, "h1")
        h1_text = h1_element.text
        if h1_text == "CSE Trip Anonymous Feedback":
            data.append(
                {
                    "testid": "Heading",
                    "status": "success",
                    "score": 0.25,
                    "maximum marks": 0.25,
                    "message": "<h1> heading is correct.",
                }
            )
        else:
            data.append(
                {
                    "testid": "Heading",
                    "status": "failed",
                    "score": 0,
                    "maximum marks": 0.25,
                    "message": "Error: <h1> heading is wrong.",
                }
            )
    except NoSuchElementException:
        data.append(
            {
                "testid": "Heading",
                "status": "failed",
                "score": 0,
                "maximum marks": 0.25,
                "message": "Error: No <h1> tag found.",
            }
        )
    # ------------------------------------------------------------------------------------------------------------------

    # ----------------------------------------------------Checking Q1---------------------------------------------------
    total = 0
    message = ""
    result = {
        "testid": "Q1 <div>",
        "status": "success",
        "score": 0,
        "maximum marks": 1,
        "message": "",
    }
    try:
        Q1 = driver.find_element(By.XPATH, '//div[@id="Q1" and @class="Box"]')
        if Q1:
            Q1_p = Q1.find_element(By.XPATH, "./p")
            if Q1_p.text == "Q1: How would you rate the trip?":
                total += 0.5
            Q1_input = Q1.find_element(
                By.XPATH, './/input[@type="text" and @class="Rating"]'
            )
            if Q1_input:
                total += 0.5
    except Exception:
        message += "Error: Q1 <div> or child elements are not correct."
        result["status"] = "failed"

    result["score"] = total
    result["message"] = message if message else "<div> correctly built for Q1."
    data.append(result)
    # ------------------------------------------------------------------------------------------------------------------

    # ----------------------------------------------------Checking Q2---------------------------------------------------
    total = 0
    message = ""
    result = {
        "testid": "Q2 <div>",
        "status": "success",
        "score": 0,
        "maximum marks": 1,
        "message": "",
    }
    try:
        Q2 = driver.find_element(By.XPATH, '//div[@id="Q2" and @class="Box"]')
        if Q2:
            Q2_p = Q2.find_element(By.XPATH, "./p")
            if Q2_p.text == "Q2: How would you rate the fun you had?":
                total += 0.5
            Q2_input = Q2.find_element(
                By.XPATH, './/input[@type="text" and @class="Rating"]'
            )
            if Q2_input:
                total += 0.5
    except Exception:
        message += "Error: Q2 <div> or child elements are not correct."
        result["status"] = "failed"

    result["score"] = total
    result["message"] = message if message else "<div> correctly built for Q2."
    data.append(result)
    # ------------------------------------------------------------------------------------------------------------------

    # ------------------------------------------------Internal CSS check------------------------------------------------
    result = {
        "testid": "Internal CSS",
        "status": "success",
        "score": 0,
        "maximum marks": 1,
        "message": "",
    }
    message = ""
    total = 0
    try:
        style_tag = driver.find_element(By.TAG_NAME, "style")
        total += 0.5
        style_content = style_tag.get_attribute("textContent")
        if "formContainer" in style_content and "background-color" in style_content:
            message = "Internal CSS done correctly."
            total += 0.5
    except Exception:
        message = "Error: Internal CSS tag not found or incorrectly defined."

    result["score"] = total
    result["message"] = message
    data.append(result)
    # ------------------------------------------------------------------------------------------------------------------

    # ------------------------------------------------External CSS check------------------------------------------------
    css_content = None
    with open("./style.css", "r") as css_file:
        css_content = css_file.read()
    if (
        css_content
        and ".Rating" in css_content
        and "width" in css_content
        and "50px" in css_content
    ):
        data.append(
            {
                "testid": "External CSS",
                "status": "success",
                "score": 1,
                "maximum marks": 1,
                "message": "External CSS done correctly.",
            }
        )
    else:
        data.append(
            {
                "testid": "External CSS",
                "status": "failed",
                "score": 0,
                "maximum marks": 1,
                "message": "External CSS is incorrect.",
            }
        )
    # ------------------------------------------------------------------------------------------------------------------


if __name__ == "__main__":

    rval = os.system("ls survey.html style.css > /dev/null 2> /dev/null")

    if rval != 0:
        data.append(
            {
                "testid": "Files",
                "status": "failed",
                "score": 0,
                "maximum marks": 10,
                "message": "Files not found. Further checking stopped.",
            }
        )
    else:
        data.append(
            {
                "testid": "Files",
                "status": "success",
                "score": 0,
                "maximum marks": 0,
                "message": "All files are present!",
            }
        )
        grade_against_testcases()

    os.system("touch ../evaluate.json")
    os.system("clear")
    overall["data"] = data
    print(json.dumps(overall, indent=4))
    with open("../evaluate.json", "w") as f:
        json.dump(overall, f, indent=4)
