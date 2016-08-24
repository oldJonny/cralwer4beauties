from bs4 import BeautifulSoup
from selenium import webdriver
import re
import os
import urllib

#获取整个页面的html（使用PhantomJS+webdriver解析）
PDriver0 = webdriver.PhantomJS(executable_path = 'C:/Users/lyzdsb/Desktop/phantomjs-2.1.1-windows/bin/phantomjs')
PDriver0.get('https://mm.taobao.com/search_tstar_model.htm?')
soup = BeautifulSoup(PDriver0.page_source , 'lxml')
#print(soup.prettify()) 格式化输出html,check源html

#获取html后，用bs4获取相对应的url

#获取封面照片

cover_imgs = soup.find_all("img", { 'data-ks-lazyload' : True })
#for img in cover_imgs:
    #print(img.get())
'''
#坑1：得到img标签后，无法得到attribute：data-ks-lazyload
'''
#获取个人链接
def perUrl_List():
    Urls = soup.find_all("a",href = re.compile('\/\/.*userId=(\d*)'))
    PDriver1 = webdriver.PhantomJS(executable_path = 'C:/Users/lyzdsb/Desktop/phantomjs-2.1.1-windows/bin/phantomjs')
    perUrls = []
    for per in Urls:
        perUrl = PDriver1.get(per.get('href'))
        perUrls.append(perUrl)
    #print(perUrls)
    return perUrls
#获取个人页面的html源码
    Urls = soup.find_all("a", href=re.compile('\/\/.*userId=(\d*)'))
    url = Urls[""]
#获取个人文本信息
perInfos = PDriver0.find_element_by_id('J_GirlsList').text
print(perInfos)
#创建文件夹
def mkdir(path):
    isExists = os.path.exists(path)
    if not isExists:
        #创建
        print("创建目录为"+path+"的文件夹")
        os.mkdir(path)
        return  True
    if isExists:
        print(path+"已存在")
        return  False

#保存封面图片到本地
url = "https:"+str(cover_imgs)
#open,read(data),write,close,flush
html = urlopen(url)
data = html.read()
Filename = "C:/Users/lyzdsb/Desktop/img"
File =Filename+str(number)+".jpg"
f = open(File,"wb") #write in binary
try:
    f.write(data)
finally:
    f.close()
    f.flush()
#保存个人主页的艺术照
perUrrl = "https:"+str(perUrl)
html_per = urlopen(perUrrl)
data = html.read()
Filename =