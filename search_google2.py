from bs4 import BeautifulSoup
import requests

def get_title(link):
    URL = link
    get_page = requests.get(URL)
    plain_text = get_page.text
    soup = BeautifulSoup(plain_text, 'html.parser')

    for table_tag in soup.find_all('table'):

        for each_row in table_tag.find_all('tr'):
            links = each_row.find('a', href=True)



        if links:  # check before you access
            for i in range(1):
                title =str(links.get('title'))
                title = title.replace("None","")
                return title
