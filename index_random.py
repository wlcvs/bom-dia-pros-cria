import random
import json

def index_random():
    links = ''
    with open("links.json", encoding='utf-8') as links_json:
        links = json.load(links_json)

    tamanho_links = len(links['links'])
    return random.randrange(0, tamanho_links)