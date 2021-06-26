import requests
import re
import datetime
import pandas as pd
import os
import sys
from requests_html import HTML

BASE_DIR = os.path.dirname(__file__)


def url_to_text(url, filename="weibo.html", save=False):
    user_agent = {"User-agent": "AdsBot-Google (+http://www.google.com/adsbot.html)"}
    r = requests.get(url, headers=user_agent)
    # print(r.text)
    # p_nick = re.compile(r"CONFIG\['onick'\]='(.*?)'")
    # m_nick = re.findall(p_nick, r.text)
    # if len(m_nick) == 1:
    #     print(m_nick[0])
    # else:
    #     print("Not found!")

    if r.status_code == 200:
        # r.encoding = 'utf-8'
        html_text = r.text
        if save:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(html_text)

        return html_text
    return ""


def parse_and_extract(url, name="2020"):
    html_text = url_to_text(url)
    # print(html_text)
    # html_text = html_text.encode(encoding="utf-8")
    r_html = HTML(html=html_text)
    entry_class = "div.WB_text.W_f14"
    entry_list = r_html.find(entry_class)
    # print(entry_list[1].text)
    return_text = ""
    for entry in entry_list:
        return_text += entry.text + "\n"
        # print()
    return return_text

    # print(entry_list)


def run():
    url = "https://weibo.com/u/6046923929?refer_flag=1005050005_&is_all=1#_loginLayer_1620007819300"
    latest_post = parse_and_extract(url)
    print("Finished")
    return latest_post
