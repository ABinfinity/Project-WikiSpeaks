#WikiSpeaks
from bs4 import BeautifulSoup
import requests

page =  requests.get(input("Enter the Wiki URL: "))

soup = BeautifulSoup(page.content, 'html.parser')
# print(soup.prettify())

result = soup.find_all("p")
for text in result:
    print(text.text)
