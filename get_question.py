from bs4 import BeautifulSoup
import requests
import sys

# URL = sys.argv[1]
URL = "https://codeforces.com/contest/570/problem/C"

inputs = []
outputs = []
parsed_items = []

page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

def get_io():
   for _ in soup.find_all("br" ):
      _.replace_with("\n")
   
   for _ in soup.find_all("pre"):
       parsed_items.append("".join(_.contents))
   
   for _ in enumerate(parsed_items, start=1):
       if _[0] % 2 == 0:
           outputs.append(_[1])
       else:
           inputs.append(_[1])
   return inputs, outputs
def get_meta():
    return_obj = dict()
    question_name = soup.find("div", class_="title")
    # TODO: Make this robust
    return question_name.contents[0].split('.',1)[1][1:].lower()
