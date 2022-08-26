import urllib.request
import os
import json

def get_image(indice):
    if not os.path.exists('./images') == True:
        os.makedirs('images')

    links = ''
    with open("links.json", encoding='utf-8') as links_json:
        links = json.load(links_json)

    imagem_index = links['links'][indice]
    urllib.request.urlretrieve(imagem_index, "images/first_img_bao_dia.jpg")