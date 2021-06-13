from bs4 import BeautifulSoup
import requests
import re

page_link = "https://en.wikipedia.org/wiki/Dark_(TV_series)"
page_response = requests.get(page_link,verify=False, timeout=5)
page_content = BeautifulSoup(page_response.content, "html.parser")
textContent = {}
for tag in page_content.find_all('h2')[1:]:
    texth2=tag.text.strip()
    texth2 = re.sub(r"\[.*?\]+", '', texth2)
    paragraph = []
    # textContent.append(texth2)
    for item in tag.find_next_siblings('p'):
        if texth2 in item.find_previous_siblings('h2')[0].text.strip():
            pTag = item.text.strip()
            pTag = re.sub(r"\[.*?\]+", '', pTag)
            paragraph.append(pTag)
    textContent[texth2] = paragraph

result = {}
for key, value in textContent.items():
    if len(value) != 0:
        result[key] = value

print(result)