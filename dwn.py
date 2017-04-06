import os

def d(url, name):
    cmd = ''
    if url.startswith("https://www.youtube.com"):
        cmd = 'youtube-dl -f m4a "{url}" -o "{name}.mp4"'
    elif url.startswith("https://soundcloud.com"):
        cmd = 'youtube-dl -f mp3 "{url}" -o "{name}.mp3"'
    elif url.startswith("http://www.nicovideo.jp"):
        cmd = 'youtube-dl -f mp4 "{url}" -o "{name}.mp4" --username "sankaku9006221@yahoo.co.jp" --password "otiaihtt" && ffmpeg -i "{name}.mp4" -ab 128 "{name}.mp3" && rm "{name}.mp4"'
    os.system(cmd.format(url=url, name=name))

ROOT = "deemo"
def download(data, directory):
    deemo = ("/home/c0115114ca/dshare/itns/" +ROOT+ "/{}{{}}".format(directory if directory.endswith("/") else directory + "/")).format
    if type(data[0]) == list:
        for data in data:
            d(data[0], deemo(data[1]))
    elif type(data[0]) == str:
        d(data[0], deemo(data[1]))

def root(directory):
    global ROOT
    ROOT = directory[:-1] if directory.endswith("/") else directory
