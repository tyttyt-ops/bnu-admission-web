import requests
import re
header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                     ' (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0'}
url='https://www.bnu.edu.cn/xbyx/index.htm'

from bs4 import BeautifulSoup
html=requests.get(url,headers=header)
html.encoding='utf-8'
college=re.findall('bnu.edu.cn/" target="_blank" data-flg="1">(.*?)</a>',html.text)
print(college)
with open('北京师范大学各院系.txt','w',encoding='utf-8') as f:
    f.write('\n'.join(college))#将列表生成txt文件

