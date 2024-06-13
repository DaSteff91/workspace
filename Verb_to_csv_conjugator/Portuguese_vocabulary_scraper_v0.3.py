# Making the code easier readable

import re
from bs4 import BeautifulSoup
import requests
import pandas as pd

verbo = input("Enter a verb: ")

input_mode = input("Enter a mode: ")

input_time = input("Enter a time: ")

url = "https://www.conjugacao.com.br/"+verbo

page = requests.get(url)
    
soup = BeautifulSoup(page.text, "html.parser")

mode = soup.find("h3", string = input_mode).parent

time = mode.find("h4", string = input_time).parent

conjugacao_with_html = time.find("p")

conjugacao_wo_html = [str(verb) for verb in conjugacao_with_html if verb != "\n" and verb != " " and verb.name != "br"]

final_list = []

for i in range(len(conjugacao_wo_html)):

    final_list.append(re.sub("<[^>]+>", " ", str(conjugacao_wo_html[i])).strip().replace("  ", " "))

df_conjugacao = str(final_list).replace(", ", "\n").replace("'","").replace("[","").replace("]","")

df_tags = ["{} {}".format(input_mode, input_time)]

df = pd.DataFrame({"A" : [verbo], "B" : df_conjugacao, "C": df_tags})

csv_name = "{}_{}_{}".format(verbo,input_mode,input_time).lower()

df.to_csv(rf"/media/sf_Share_VM/{csv_name}.csv", mode='a', header=None, index=False)
