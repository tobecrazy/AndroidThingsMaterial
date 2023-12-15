import requests
from bs4 import BeautifulSoup
import os
import urllib

# 目标网页的URL
url = "https://unsplash.com/search/photos/cat"

# 发送请求获取网页内容
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# 创建一个用于保存图片的目录
if not os.path.exists('images'):
    os.makedirs('images')

# 获取网页中所有图片的URL
image_tags = soup.findAll('img')
image_urls = [img['src'] for img in image_tags]

# 下载所有图片
for i, url in enumerate(image_urls):
    try:
        # 获取图片文件名
        filename = os.path.join('images', 'image{}.jpg'.format(i))
        # 下载图片
        urllib.request.urlretrieve(url, filename)
        print('Downloaded', filename)
    except Exception as e:
        print('Failed to download', url)
        print(e)
