from bs4 import BeautifulSoup
import re


def get_all_li_list():
    f = open('data/shows_list_html.htm')
    html_doc = f.read()
    soup = BeautifulSoup(html_doc, 'html.parser')

    li_list = soup.find_all('li')
    return li_list


if __name__ == '__main__':
    print(get_all_li_list())
