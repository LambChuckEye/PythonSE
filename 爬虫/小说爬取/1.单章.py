from urllib import request
from bs4 import BeautifulSoup

if __name__ == "__main__":
    download_url = 'http://www.biqukan.com/1_1094/5403177.html'
    # 模仿浏览器发送器请求
    head = {}
    head[
        'User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
    # 构建request
    download_req = request.Request(url=download_url, headers=head)
    # 发送并获取response
    download_response = request.urlopen(download_req)
    # 读取response中的内容
    download_html = download_response.read().decode('gbk', 'ignore')
    # 将内容转换为beautifulSoup类型
    soup_texts = BeautifulSoup(download_html, 'lxml')
    # 获取指定id和class的标签内容
    texts = soup_texts.find_all(id='content', class_='showtxt')
    # 将上一步的查询结果转换为beautifulSoup
    soup_text = BeautifulSoup(str(texts), 'lxml')
    # 获取div中的内容,并将\xa0无法解码的字符删除
    print(soup_text.div.text.replace('\xa0', ''))
