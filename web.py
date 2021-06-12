# Import packages
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

# Specify url of the web page
source = urlopen("https://en.wikipedia.org/wiki/Dark_(TV_series)").read()

# Make a soup 
soup = BeautifulSoup(source,'html.parser')
soup

# Extract the plain text content from paragraphs
paras = []
for paragraph in soup.find_all('p'):
    if paragraph.parent["class"] == ["mw-parser-output"]: 
        paras.append(str(paragraph.text))

# Extract text from paragraph headers
heads = []
for head in soup.find_all('span', attrs={'mw-headline'}):
    heads.append(str(head.text))

# Interleave paragraphs & headers
text = [val for pair in zip(paras, heads) for val in pair]
text = ' '.join(text)

# Drop footnote superscripts in brackets
text = re.sub(r"\[.*?\]+", '', text)

# Replace '\n' (a new line) with '' and end the string at $1000.
text = text.replace('\n', '')[:-11]
print(text)