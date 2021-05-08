import requests
import datetime
import pandas as pd
import os
import sys
from requests_html import HTML

BASE_DIR = os.path.dirname(__file__)


def url_to_text(url, filename="world.html", save=False):
    r = requests.get(url)
    if r.status_code == 200:
        html_text = r.text
        if save:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(html_text)
        return html_text
    return ""


def parse_and_extract(url, name='2020'):

    html_text = url_to_text(url)
    r_html = HTML(html=html_text)  # HTML object
    table_class = ".imdb-scroll-table"
    r_table = r_html.find(table_class)  # a list

    if len(r_table) == 1:

        parsed_table = r_table[0]
        rows = parsed_table.find('tr')
        header_row = rows[0]
        header_cols = header_row.find('th')
        header_names = [x.text for x in header_cols]
        table_data = []
        for row in rows[1:]:

            cols = row.find("td")
            row_data = []
            for i, col in enumerate(cols):
                # print(i, col.text, "\n\n")
                row_data.append(col.text)
            table_data.append(row_data)

        df = pd.DataFrame(table_data, columns=header_names)
        path = os.path.join(BASE_DIR, 'data')
        os.makedirs(path, exist_ok=True)
        filepath = os.path.join('data', '{}.csv'.format(name))
        df.to_csv(filepath, index=False)


def run(start_year=None, years_ago=1):

    if start_year is None:
        now = datetime.datetime.now()
        start_year = now.year
    assert isinstance(start_year, int)
    assert isinstance(years_ago, int)
    assert len(str(start_year)) == 4

    for i in range(0, years_ago + 1):
        print(start_year)
        url = "https://www.boxofficemojo.com/year/world/{}".format(start_year - i)
        parse_and_extract(url, name=str(start_year - i))
        print("Finished: {}".format(start_year - i))
