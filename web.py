#!/usr/bin/python3

from bottle import *
from web_util import *
@get("/")
def index():
    return template("index.tpl", {
        "message" : get_video_data(24399677)["description"]
        })


@get("/mylist")
def mylist():
    mylist_id = request.query.get("mylist")
    mylist = [m["item_data"] for m in get_mylist_data(mylist_id)]
    return template("mylist.tpl", {
        "mylist" : mylist
        })


@get("/search", method="POST")
def searchform():
    url = request.forms.get("url")
    if url:
        return template("search.tpl", search(request.forms.q, url=url))
    return template("search.tpl", search(request.forms.q))


@get("/video")
def video():
    video_id = request.query.get("video_id")
    video_data = get_mp4(video_id)
    return template("video.tpl", video_data)


@get("/description")
def description():
    video_id = request.query.get("video_id")
    video_data = get_video_data(video_id)
    return template("description.tpl", video_data)

if __name__ == "__main__":
    run(host="0.0.0.0", port=8000, debug=True, reloader=True)
