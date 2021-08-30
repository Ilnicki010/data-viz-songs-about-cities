from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import re

def format_city_name(name):
    return name.replace('[edit]', '').strip()

def get_city_and_state(name):
    return [format_city_name(name.split(',')[i]) for i in (0, 1)]

def get_song_name(name):
    name_replaced = name.replace('“','"').replace('”','"')
    results = re.findall(r'(?<=\")(.*?)(?=\")', name_replaced)
    if results: return results[0]

def load_page(URL):
    uClient = uReq(URL)
    page_html = uClient.read()
    uClient.close()
    return soup(page_html, 'html.parser')
    
def normalized_city_name(name):
    return name.lower().replace(' ','_').strip()