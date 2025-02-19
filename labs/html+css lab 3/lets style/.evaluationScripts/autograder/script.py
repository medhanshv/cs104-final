'''Import required modules'''
import json
from bs4 import BeautifulSoup
import os

overall = {"data": []
}

marks = {
    'Total': {
        'Your Total': 0,
        'Maximum Marks': 14
    },
    'Basic-Features': {
        'HTML Tag': 0,          # d
        'Title Tag': 0,         # d
        'Link': 0               # d
    },
    'Navigation-Bar': {
        'Nav Tag': 0,
        'Background-Colour': 0
    },
    'Header': {
        'header': 0,
        'Text-Alignment': 0,
    },
    'Footer': {
        'footer': 0,
        'id': 0,
        'Text-Colour': 0
    },
    'Form': {
        'form': 0,
        'label': 0,
        'input': 0,
        'button': 0
    },

}

feedback = {
    'Basic-Features': {
        'HTML Tag': '',
        'Title Tag': '',
        'Link': ''
    },
    'Navigation-Bar': {
        'Nav Tag': '',
        'Background-Colour': ''
    },
    'Header': {
        'header': '',
        'Text-Alignment': '',
    },
    'Footer': {
        'footer': '',
        'id': '',
        'Text-Colour': ''
    },
    'Form': {
        'form': '',
        'label': '',
        'input': '',
        'button': ''
    },

}


page = open('/home/labDirectory/advanced.html', 'r', encoding='utf-8')
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
    html_tag = soup.find('link')
    if html_tag is not None:
        marks['Basic-Features']['Link'] = 1
        marks['Total']['Your Total'] += 1
        feedback['Basic-Features']['Link'] = 'link tag present'
    else:
        feedback['Basic-Features']['Link'] = 'link tag missing'
    
except AttributeError:
    feedback['Basic-Features']['Link'] = 'Error encountered (check link tag)'

try:
    html_tag = soup.find('form')
    if html_tag is not None:
        marks['Form']['form'] = 1
        marks['Total']['Your Total'] += 1
        feedback['Form']['form'] = 'form tag present'
    else:
        feedback['Form']['form'] = 'form tag missing'
    
except AttributeError:
    feedback['Form']['form'] = 'Error encountered (check form tag)'

try:
    html_tag = soup.find('label')
    if html_tag is not None:
        marks['Form']['label'] = 1
        marks['Total']['Your Total'] += 1
        feedback['Form']['label'] = 'label tag present'
    else:
        feedback['Form']['label'] = 'label tag missing'
    
except AttributeError:
    feedback['Form']['label'] = 'Error encountered (check label tag)'

try:
    html_tag = soup.find('input')
    if html_tag is not None:
        marks['Form']['input'] = 1
        marks['Total']['Your Total'] += 1
        feedback['Form']['input'] = 'input tag present'
    else:
        feedback['Form']['input'] = 'input tag missing'
    
except AttributeError:
    feedback['Form']['input'] = 'Error encountered (check input tag)'

try:
    html_tag = soup.find('button')
    if html_tag is not None:
        marks['Form']['button'] = 1
        marks['Total']['Your Total'] += 1
        feedback['Form']['button'] = 'button tag present'
    else:
        feedback['Form']['button'] = 'button tag missing'
    
except AttributeError:
    feedback['Form']['button'] = 'Error encountered (check button tag)'

try:
    html_tag = soup.find('header')
    if html_tag is not None:
        marks['Header']['header'] = 1
        marks['Total']['Your Total'] += 1
        feedback['Header']['header'] = 'header tag present'
    else:
        feedback['Header']['header'] = 'header tag missing'
    
except AttributeError:
    feedback['Header']['header'] = 'Error encountered (check header tag)'

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

try:
    html_tag = soup.find('footer')
    if 'id' in html_tag.attrs:
        marks['Footer']['id'] = 1
        marks['Total']['Your Total'] += 1
        feedback['Footer']['id'] = 'footer id present'
    else:
        feedback['Footer']['id'] = 'footer id missing'
    
except AttributeError:
    feedback['Footer']['id'] = 'Error encountered (check footer id)'

try:
    html_tag = soup.find('nav')
    if html_tag is not None:
        marks['Navigation-Bar']['Nav Tag'] = 1
        marks['Total']['Your Total'] += 1
        feedback['Navigation-Bar']['Nav Tag'] = 'nav tag present'
    else:
        feedback['Navigation-Bar']['Nav Tag'] = 'nav tag missing'
    
except AttributeError:
    feedback['Navigation-Bar']['Nav Tag'] = 'Error encountered (check nav tag)'

with open('/home/labDirectory/styles.css', 'r') as file:
    content = file.read()
    if "background-color" in content:
        marks['Navigation-Bar']['Background-Colour'] = 1
        marks['Total']['Your Total'] += 1
        feedback['Navigation-Bar']['Background-Colour'] = 'nav background-colour present'
    else:
        feedback['Navigation-Bar']['Background-Colour'] = 'nav background-colour missing'
    if "text-align" in content:
        marks['Header']['Text-Alignment'] = 1
        marks['Total']['Your Total'] += 1
        feedback['Header']['Text-Alignment'] = 'header text-alignment present'
    else:
        feedback['Header']['Text-Alignment'] = 'header text-alignment missing'
    if "color" in content:
        marks['Footer']['Text-Colour'] = 1
        marks['Total']['Your Total'] += 1
        feedback['Footer']['Text-Colour'] = 'footer text-colour present'
    else:
        feedback['Footer']['Text-Colour'] = 'footer text-colour missing'

overall.update({'data': []})
total_marks = 0
for parent_category,val in marks.items():
    if parent_category == 'Total':
        continue
    for child_category,compo_mark in val.items():
        overall['data'].append({
            'testid': parent_category + '/' +child_category,
            'score': compo_mark,
            'maximum marks': 1,
            'status': 'success',
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

