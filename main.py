#WikiSpeaks
from bs4 import BeautifulSoup
import requests
from gtts import gTTS

page =  requests.get("https://en.wikipedia.org/wiki/Dark_(TV_series)")  #input("Enter the Wiki URL: "))

soup = BeautifulSoup(page.content, 'html.parser')


headings = soup.find_all("h2")
# spanTag = headings.findChildren("span" , class_ = "mw-headline")
# print(headings)
# print("#############################################")
for line in headings:
    try:
        headline = line.find("span" , class_ = "mw-headline")
        print(headline.text)
        print("-----------------------------End of headline-----------------------------")
        print(line.text)
        print("-------------------------End of line---------------------------------------")
        print(line.next_sibling.text)
        print("------------------------End of sibling----------------------------------------")
    except Exception as e:
        continue


# for line in headings:
#     # head = line.find(class_ = "mw-headline")
#     # paragraph = head.find_all("p")
#     spanTag = line.findChildren("span" , class_ = "mw-headline")
#     print(spanTag[0].text)
#     print("----------------------------------------------------------------")
#     # print(paragraph.text)