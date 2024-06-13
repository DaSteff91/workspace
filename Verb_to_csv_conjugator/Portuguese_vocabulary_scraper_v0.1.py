import re
from bs4 import BeautifulSoup
import requests

url = "https://www.conjugacao.com.br/verbo-ir/"

page = requests.get(url)
    
soup = BeautifulSoup(page.text, "html.parser")

Indicativo = soup.find("h3", string = "Indicativo").parent

Presente = Indicativo.find("h4", string = "Presente").parent

Conjugacao = Presente.find("p")

test = [str(text) for text in Conjugacao if text != "\n" and text != " " and text.name != "br"]

final_list = []

for i in range(len(test)):

    final_list.append(re.sub("<[^>]+>", " ", str(test[i])).strip().replace("  ", " "))

print(final_list)
