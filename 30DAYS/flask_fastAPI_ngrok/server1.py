from flask import Flask
from weibo_scrape import run as scrape_runner

app = Flask(__name__)


# the root index file of the website /

# http://localhost:8000/
@app.route("/", methods=["GET"])
def hello_world():
    return "欢迎来到何思怡的weibo_first_post_scraper"


# http://localhost:8000/abc
@app.route("/abc", methods=["GET"])
def abc_view():
    return "Hello, world. this is abc"


@app.route("/janet_latest_post", methods=["GET"])
def box_office_scraper_view():
    # return scrape_runner()
    return "不用了不用了行吧"
