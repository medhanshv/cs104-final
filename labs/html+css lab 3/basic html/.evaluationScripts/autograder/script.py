'''Import required modules'''
import json
from bs4 import BeautifulSoup
import os

overall = {"data": []
}


# {
#     "data": [
#         {
#             "testid": 1,
#             "status": "success",
#             "score": 1,
#             "maximum marks": 1,
#             "message": "Script Executed Successfully. Test Case Passed."
#         },
#         {
#             "testid": 2,
#             "status": "success",
#             "score": 0,
#             "maximum marks": 1,
#             "message": "Script Executed Successfully. Output is not as Expected."
#         }
#     ]
# }

# overall = {
#     'marks': {},
#     'total': 12,
#     'feedback': {}
# }

marks = {
    'Total': {
        'Your Total': 0,
        'Maximum Marks': 12
    },
    'Basic-Features': {
        'HTML Tag': 0,
        'Title Tag': 0
    },
    'Text': {
        'H1': 0,
        'H2': 0,
        'Paragraphs': 0
    },
    'List': {
        'ul': 0,
    },
    'Table': {
        'Table Heading': 0,
        'Table Row': 0,
        'Table Data': 0
    },
    'Email': {
        'href': 0,
        'mailto': 0
    },
    'Footer': {
        'footer': 0
    },
}

feedback = {
    'Basic-Features': {
        'HTML Tag': '',
        'Title Tag': ''
    },
    'Text': {
        'H1': '',
        'H2': '',
        'Paragraphs': ''
    },
    'List': {
        'ul': '',
    },
    'Table': {
        'Table Heading': '',
        'Table Row': '',
        'Table Data': ''
    },
    'Email': {
        'href': '',
        'mailto': ''
    },
    'Footer': {
        'footer': ''
    },
}

page = open('/home/labDirectory/basic.html', 'r', encoding='utf-8')
soup = BeautifulSoup(page, 'html.parser')

try:
    html_tag = soup.find('html')
    if html_tag is not None:
        marks['Basic-Features']['HTML Tag'] = 1
        marks['Total']['Your Total'] += 1
        feedback['Basic-Features']['HTML Tag'] = 'html tag present'
    else:
        feedback['Basic-Features']['HTML Tag'] = 'html tag missing'
    
except AttributeError:
    feedback['Basic-Features']['HTML Tag'] = 'Error encountered (check html tag)'

try:
    html_tag = soup.find('title')
    if html_tag is not None:
        marks['Basic-Features']['Title Tag'] = 1
        marks['Total']['Your Total'] += 1
        feedback['Basic-Features']['Title Tag'] = 'title tag present'
    else:
        feedback['Basic-Features']['Title Tag'] = 'title tag missing'
    
except AttributeError:
    feedback['Basic-Features']['Title Tag'] = 'Error encountered (check title tag)'

try:
    html_tag = soup.find('h1')
    if html_tag is not None:
        marks['Text']['H1'] = 1
        marks['Total']['Your Total'] += 1
        feedback['Text']['H1'] = 'h1 tag present'
    else:
        feedback['Text']['H1'] = 'h1 tag missing'
    
except AttributeError:
    feedback['Text']['H1'] = 'Error encountered (check h1 tag)'
    
try:
    html_tag = soup.find('h2')
    if html_tag is not None:
        marks['Text']['H2'] = 1
        marks['Total']['Your Total'] += 1
        feedback['Text']['H2'] = 'h2 tag present'
    else:
        feedback['Text']['H2'] = 'h2 tag missing'
    
except AttributeError:
    feedback['Text']['H2'] = 'Error encountered (check h2 tag)'

try:
    html_tag = soup.find('p')
    if html_tag is not None:
        marks['Text']['Paragraphs'] = 1
        marks['Total']['Your Total'] += 1
        feedback['Text']['Paragraphs'] = 'p tag present'
    else:
        feedback['Text']['Paragraphs'] = 'p tag missing'
    
except AttributeError:
    feedback['Text']['Paragraphs'] = 'Error encountered (check p tag)'

try:
    html_tag = soup.find('ul')
    if html_tag is not None:
        marks['List']['ul'] = 1
        marks['Total']['Your Total'] += 1
        feedback['List']['ul'] = 'ul tag present'
    else:
        feedback['List']['ul'] = 'ul tag missing'
    
except AttributeError:
    feedback['List']['ul'] = 'Error encountered (check ul tag)'

try:
    html_tag = soup.find('th')
    if html_tag is not None:
        marks['Table']['Table Heading'] = 1
        marks['Total']['Your Total'] += 1
        feedback['Table']['Table Heading'] = 'th tag present'
    else:
        feedback['Table']['Table Heading'] = 'th tag missing'
    
except AttributeError:
    feedback['Table']['Table Heading'] = 'Error encountered (check th tag)'

try:
    html_tag = soup.find('tr')
    if html_tag is not None:
        marks['Table']['Table Row'] = 1
        marks['Total']['Your Total'] += 1
        feedback['Table']['Table Row'] = 'tr tag present'
    else:
        feedback['Table']['Table Row'] = 'tr tag missing'
    
except AttributeError:
    feedback['Table']['Table Row'] = 'Error encountered (check tr tag)'

try:
    html_tag = soup.find('td')
    if html_tag is not None:
        marks['Table']['Table Data'] = 1
        marks['Total']['Your Total'] += 1
        feedback['Table']['Table Data'] = 'td tag present'
    else:
        feedback['Table']['Table Data'] = 'td tag missing'
    
except AttributeError:
    feedback['Table']['Table Data'] = 'Error encountered (check td tag)'

try:
    html_tag = soup.find('a')
    if html_tag is not None:
        marks['Email']['href'] = 1
        marks['Total']['Your Total'] += 1
        feedback['Email']['href'] = 'href tag present'
    else:
        feedback['Email']['href'] = 'href tag missing'
    
except AttributeError:
    feedback['Email']['href'] = 'Error encountered (check href tag)'

try:
    mailto_links = soup.find_all('a', href=lambda href: href and href.startswith('mailto:'))

    if mailto_links:
        marks['Email']['mailto'] = 1
        marks['Total']['Your Total'] += 1
        feedback['Email']['mailto'] = 'mailto present'
    else:
        feedback['Email']['mailto'] = 'mailto missing'

except AttributeError:
    feedback['Email']['mailto'] = 'Error encountered (check mailto link)'

try:
    html_tag = soup.find('footer')
    if html_tag is not None:
        marks['Footer']['footer'] = 1
        marks['Total']['Your Total'] += 1
        feedback['Footer']['footer'] = 'footer tag present'
    else:
        feedback['Footer']['footer'] = 'footer tag missing'
    
except AttributeError:
    feedback['Footer']['footer'] = 'Error encountered (check footer tag)'

overall.update({'data': []})
total_marks = 0
for parent_category,val in marks.items():
    if parent_category == 'Total':
        continue
    for child_category,compo_mark in val.items():
        overall['data'].append({
            'testid': parent_category + '/' +child_category,
            'score': compo_mark,
            'status': "success",
            'maximum marks': 1,
            'message': feedback[parent_category][child_category]
        })
        total_marks += compo_mark
# overall['data'].append({
#     'testid': 'Total',
#     'score': total_marks,
#     'maximum marks': 12,
#     'message': 'Total score'
# })
 

# overall['marks'] = marks
# overall['total'] = sum(sum(compo.values()) for compo in marks.values())
# overall['feedback'] = feedback
# print('------------------------- MARKS ------------------------------')
# print(json.dumps(marks, indent=4))
# print('----------------------- FEEDBACK -----------------------------')
# print(json.dumps(feedback, indent=4))
# print('--------------------------------------------------------------')
with open('../evaluate.json', 'w') as f:
	json.dump(overall,f,indent=4)

os.system("rm -f /home/.evaluationScripts/autograder/basic.html")
