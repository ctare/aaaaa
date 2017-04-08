#!/usr/bin/python3
from xml.etree import ElementTree
import requests
from bs4 import BeautifulSoup
import re
import json
import urllib

def get_video_data(video_id):
    response = requests.get("http://ext.nicovideo.jp/api/getthumbinfo/sm{}".format(video_id))
    if response.status_code is 200:
        root = ElementTree.fromstring(response.text)
        data = {element.tag: element.text for element in root.find("thumb")}
        response = requests.get("http://www.nicovideo.jp/watch/sm{}".format(video_id))
        soup = BeautifulSoup(response.text, "html.parser")
        data["description"] = add_link(soup.find("p", {"itemprop": "description"}).renderContents().decode("utf-8"))
        return data
    return None


def get_mylist_data(mylist):
    response = requests.get("http://www.nicovideo.jp/mylist/{}".format(mylist))
    if response.status_code is 200:
        span = re.search(r"preload\(.*\]", response.text).span()
        data = response.text[span[0]:span[1]]
        span = re.search(r"\[.*\]", data).span()
        data = data[span[0]:span[1]]
        data = json.loads(data)
        return data
    return None


def add_link(message):
    message = re.sub(r"mylist/(\d+)", r"<a href='javascript:void(0)' mylist='\1'>mylist/\1</a>", message)
    return re.sub(r"sm(\d+)", r"<a href='javascript:void(0)' video='\1'>sm\1</a>", message)


def get_mp4(video_id):
    response = requests.get("http://localhost:3030?video_id={}".format(video_id))
    cookie_url, url = response.text.split("\n")
    return {"cookie_url": cookie_url, "url": url}


IS_NUMBER = re.compile(r"\d+")
def search(query, sort="v", url=None):
    pager_data = {"next": None, "prev": None, "number": {}, "now": 0}
    if not query and not url: return {"pager": pager_data, "videos": []}
    if not url:
        url = "http://www.nicovideo.jp/search/{}?sort={}".format(query, sort)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    result = []
    for li in soup.select(".video.uad.videoList01 li.item"):
        result.append({"title": li.select("a[title]")[0]["title"], "watch_id": li["data-id"]})

    pager = soup.select(".pager")
    if pager:
        pager = pager[0]
        pager_data["now"] = pager.select(".pagerBtn.active")[0].text
        for p in pager.select(".pagerBtn"):
            t = p.text
            if IS_NUMBER.match(t):
                pager_data["number"][t] = p["href"]
            elif t == "次へ":
                pager_data["next"] = p["href"]
            elif t == "前へ":
                pager_data["prev"] = p["href"]
    return {"pager": pager_data, "videos": result}


if __name__ == "__main__":
    # print(search(url="http://www.nicovideo.jp/search/%E3%82%8C%E3%82%92%E3%82%8B?page=2&amp;sort=v&amp;order=d"))
    data = get_mp4(24399677)
    # print(data["description"])
    # print(data.keys())
    # add_link(data["description"])
    # get_mylist_data(19099704)
