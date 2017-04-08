from bottle import *
import json
import requests
import urllib

@get("/")
def index():
    video_id = request.query.get("video_id")
    key_url = "http://embed.nicovideo.jp/play/sm{}?parent=&serviceUserId=ZjnIxfUXmT_1491466820678".format(video_id)
    response = requests.get(key_url)
    key = json.loads(response.text)
    cookie_url = "http://ext.nicovideo.jp/thumb_watch/sm{}?k={}&device=html5_watch".format(video_id, key["thumbWatchPlayKey"])
    response = requests.get(cookie_url, cookies=response.cookies)
    url = urllib.request.unquote(re.search(r"http.*$", response.text).group()).replace("premium=0", "premium=1")
    return "{}\n{}".format(cookie_url, url)

if __name__ == "__main__":
    run(host="localhost", port=3030, debug=True, reloader=True)
