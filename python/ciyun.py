from pyecharts.charts import WordCloud
import webbrowser

with open('北京师范大学各院系.txt','r',encoding='utf-8') as f:
    list1=[i for i in f]


value = [1 for i in range(33)]
data_pair=list(zip(list1,value))
wordcloud = WordCloud()
wordcloud.add("院系词云图", data_pair=data_pair, word_size_range=[12, 30],
              shape='cardioid',pos_top='center',pos_left='center')
wordcloud.render('ciyun.html')
webbrowser.open('ciyun.html')