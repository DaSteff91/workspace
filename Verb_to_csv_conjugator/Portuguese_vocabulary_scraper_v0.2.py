import re
from bs4 import BeautifulSoup
import requests
import pandas as pd

verbo = input("Enter a verb: ")

input_mode = input("Enter Indicativo: ")

input_time = input("Enter Presente: ")

url = "https://www.conjugacao.com.br/"+verbo

page = requests.get(url)
    
soup = BeautifulSoup(page.text, "html.parser")

indicativo = soup.find("h3", string = input_mode).parent

presente = indicativo.find("h4", string = input_time).parent

conjugacao = presente.find("p")

conjugacao_list = [str(text) for text in conjugacao if text != "\n" and text != " " and text.name != "br"]

final_list = []

for i in range(len(conjugacao_list)):

    final_list.append(re.sub("<[^>]+>", " ", str(conjugacao_list[i])).strip().replace("  ", " "))

df = pd.DataFrame({"A" : [verbo], "B" : str(final_list).replace(", ", "\n").replace("'","").replace("[","").replace("]",""), "C": ["{} {}".format(input_mode, input_time)]})

df.to_csv(r"/media/sf_Share_VM/output6.csv", mode='a', header=None, index=False)

#-> IT WORKS, BITCHES