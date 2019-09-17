#coding=utf-8
from icrawler.builtin import BaiduImageCrawler 
from icrawler.builtin import BingImageCrawler 
from icrawler.builtin import GoogleImageCrawler 
import os

#必应图片爬虫
def download_img(key,num):
    
    if not os.path.exists("./bing/" + key):
	os.makedirs("./bing/" + key)
    if not os.path.exists("./baidu/" + key):
        os.makedirs("./baidu/" + key)
    
    bing_storage = {'root_dir': './bing/' + key}
    bing_crawler = BingImageCrawler(parser_threads=2,
                                downloader_threads=4, 
                                storage=bing_storage)
    bing_crawler.crawl(keyword=key,
                   max_num=num)

    #谷歌图片爬虫
    baidu_storage = {'root_dir': './baidu/' + key}
    baidu_crawler = BaiduImageCrawler(parser_threads=2,
                                  downloader_threads=4,
                                  storage=baidu_storage)
    baidu_crawler.crawl(keyword=key, 
                     max_num=num)
with open("name.list","r") as f:
    for line in f:
	download_img(line.strip(),10000)
f.close()
