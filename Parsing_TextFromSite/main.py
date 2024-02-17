import requests

link = "https://deti-online.com/stihi/stihi-1-sentyabrya/"
response = requests.get(link).text

with open('text.html','w',encoding="utf-8") as file:
    file.writelines(response)