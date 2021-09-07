from bs4 import BeautifulSoup
import re

html = """
<html>
<head>
<title>Jack_Cui</title>
</head>
<body>
<p class="title" name="blog"><b>My Blog</b></p>
<li><!--注释--></li>
<a href="http://blog.csdn.net/c406495762/article/details/58716886" class="sister" id="link1">Python3网络爬虫(一)：利用urllib进行简单的网页抓取</a><br/>
<a href="http://blog.csdn.net/c406495762/article/details/59095864" class="sister" id="link2">Python3网络爬虫(二)：利用urllib.urlopen发送数据</a><br/>
<a href="http://blog.csdn.net/c406495762/article/details/59488464" class="sister" id="link3">Python3网络爬虫(三)：urllib.error异常</a><br/>
</body>
</html>
"""

# 创建Beautiful Soup对象
# 读取字符串中的html
soup = BeautifulSoup(html, 'lxml')

# 读取文件中的html
# soup = BeautifulSoup(open('testhtml.html'), 'lxml')

# 格式化输出
print(soup.prettify())

# ==========================================
# 1. 获取标签:
# 标签,获取指定标签内的数据,只获取第一个匹配的标签
print(soup.title)
print(soup.head)
print(soup.a)
print(soup.p)

# 2. 标签的属性:
# soup的name为 [document]
print(soup.name)
# 标签的name为标签值
print(soup.title.name)

# 3. 将标签中的所有属性转化为字典:
print(soup.a.attrs)

# 4. 直接获取标签中的属性,两种方法
print(soup.a['class'])
print(soup.a.get('class'))

# 5. 获取标签中的字符串内容
print(soup.title.string)

# ==================================================================
# 遍历网页
# 将tag以列表形式返回
print(soup.body.contents)
print(soup.body.contents[1])

# 该标签下的获取子节点
for child in soup.body.children:
    print(child)

# ==================================================================
# 搜索
# find_all(name, attrs, recursive, text, limit, **kwargs)：
# find_all() 方法搜索当前tag的所有tag子节点,并判断是否符合过滤器的条件。

# 1. name 参数可以查找所有名字为 name 的tag,字符串对象会被自动忽略掉。
# 直接传入标签名称
print(soup.find_all('a'))

# 传入正则表达式
for tag in soup.find_all(re.compile("^b")):
    print(tag.name)

# 传入参数列表
print(soup.find_all(['title', 'b']))

# 传True返回所有
for tag in soup.find_all(True):
    print(tag)

# 2. attrs参数: 传入attrs搜索特定参数
print(soup.find_all(attrs={"class": "title"}))

# 3. recursive参数: 调用tag的 find_all() 方法时,Beautiful Soup会检索当前tag的所有子孙节点,如果只想搜索tag的直接子节点,可以使用参数 recursive=False。

# 4. text参数: 直接搜索字符串内容
print(soup.find_all(text="Python3网络爬虫(三)：urllib.error异常"))

# 5. limit参数: 限制返回数量
print(soup.find_all("a", limit=2))

# 6. kwargs参数: 如果传入 class 参数,Beautiful Soup 会搜索每个 class 属性为 title 的 tag 。kwargs 接收字符串，正则表达式
print(soup.find_all(class_="title"))
