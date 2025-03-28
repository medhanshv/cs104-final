from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
import os
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup




overall = {"data": []
}
maximum_totals = [3, 5, 5]
data = []
test_case_num = 3

#------------------------------test cases---------------------------

for i in range(0,test_case_num):
    
    # os.system("rm -f collect.txt expected_output.txt")

    msg = ""
    total = 0
    result = {
        "testid": "1",
        "status": "success",
        "score": 0,
        "maximum marks" : maximum_totals[i],
        "message": ""
    }
    # time.sleep(2)
    os.system('rm -f sample.html')
    # os.system()
    command = f'cp testcases/{i+1}/sample.html .'

    
    os.system(command)
    
    current_directory = os.getcwd()
    file_url = 'file://' + os.path.join(current_directory, 'sample.html')
    # driver = webdriver.Chrome()
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--headless')
    options.add_argument('--disable-dev-shm-usage')
    chrome_service = Service('/usr/bin/chromedriver')
    driver = webdriver.Chrome(service=chrome_service, options=options)
    
    driver.get(file_url)
    button = driver.find_element("xpath", "//button[text()='Change']")
    
    button.click()
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    images = soup.find_all('img')
    if images:
        print(f"hello {i}")
        total += 1 
    for image in images:
        if image['src'] != 'timepass.png':
             total -= 1
             msg += "Image Source Not Correct; "
             break
    
    
    # 2. Check if all <h1> heading tags are deleted
    h1_tags = soup.find_all('h1')
    if (len(h1_tags) > 0):
         total -= 1
         msg += "H1 Tags Not Removed; "
    total += 1

    # 3. Check if paragraphs have the correct content
    paragraphs = soup.find_all('p')
    if paragraphs:
         total += 1
    for paragraph in paragraphs:
        # print(paragraph.get_text)
        if not "Enough" in paragraph.get_text():
             total -= 1
             msg += "Paragraph Text Not Changed; "
             break
    # total += 1
    # 4. Check if <h2> content is uppercase
    h2_tags = soup.find_all('h2')
    if h2_tags:
        total += 1
    for h2_tag in h2_tags:
        if h2_tag.get_text() != h2_tag.get_text().upper():
             total -= 1
             msg += "H2 Text Not In Upper Case; "
             break
    
    
    # 5. Check if <div> containers with id = "div1" have an empty <h3> heading
    div_container = soup.find("div", {"id": "div1"})
    
    # print(div_container)
    if div_container:
         total += 1
         h3_tag = div_container.find("h3")
        #  print(h3_tag)
         if not h3_tag:
              total -= 1
              msg += "div1 container does not contain h3 tag; "
             
    
    
    driver.quit()

    # print("check")
    # print(msg)
    result["testid"] = i + 1
    result["score"] = total
    result["message"] = msg
    data.append(result)


overall['data'] = data
print(json.dumps(overall, indent=4))
with open('../evaluate.json', 'w') as f:
	json.dump(overall,f,indent=4)