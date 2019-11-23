import requests, re, json, os
from urllib.parse import urlencode
from urllib.request import urlretrieve
import pprint
import re

def getPid(url):
    #url为该页面的网址
    return_text = requests.get(url).text
    searchObj = re.findall(r'<!--repaste.video.code.begin-->(.+?)<!--repaste.video.code.end-->', return_text)
    return searchObj[0]

def getVideInfo(pid):
    #pid为该页面视频对应的pid
    #pid 从页面中的源代码找到，在<!--repaste.video.code.begin-->和<!--repaste.video.code.end-->之间
    url = "http://vdn.apps.cntv.cn/api/getHttpVideoInfo.do?pid=" + pid
    res = requests.get(url).text
    res = json.loads(res)
    title = res['title']
    video_url = res['video']['chapters4'][0]['url']
    return title,video_url

def saveVideo(url):
    pid = getPid(url)
    title,video_url = getVideInfo(pid)
    urlretrieve(video_url, title+".mp4")
    print("完成保存！")

if __name__ == "__main__":
    # url = "http://tv.cctv.com/2019/11/23/VIDEzEc0GomMhqbJubVXXSKy191123.shtml"
    url = input()
    saveVideo(url)
    print("==="*30,'\n')
    