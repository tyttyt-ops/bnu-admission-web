from pyecharts.charts import Line # type: ignore
from pyecharts import options as opts # type: ignore
import webbrowser

attr = ['2022','2023','2024']
v1 = [665,658,658]
v2 = [666,662,660]
v3 = [668,664,664]
v4 = [663,657,659]
v5 = [666,657,658]
v6 = [670,660,661]
v7 = [670,657,660]
v8 = [662,657,658]
v9 = [669,669,660]
v10 = [656,659,664]
v11 = [659,659,664]

line = (Line().add_xaxis(attr).add_yaxis(series_name="地理科学",y_axis=v1).add_yaxis(series_name='化学',y_axis=v2)
.add_yaxis(series_name='理科实验班',y_axis=v3).add_yaxis(series_name='人工智能',y_axis=v4).add_yaxis(series_name='生命科学类',y_axis=v5)
.add_yaxis(series_name='数学与应用数学',y_axis=v6).add_xaxis(attr).add_yaxis(series_name='统计学',y_axis=v7)
.add_yaxis(series_name='物理学类',y_axis=v8).add_yaxis(series_name='心理学',y_axis=v9)
.add_yaxis(series_name='金融科技',y_axis=v10).add_yaxis(series_name='政治学，经济学与哲学',y_axis=v11)
        .set_global_opts(title_opts=opts.TitleOpts(title='2022-2024')
,xaxis_opts=opts.AxisOpts(name='年份',is_show=True)
,yaxis_opts=opts.AxisOpts(name='分数',min_=655,max_=670)))
grid_opts=opts.GridOpts(pos_left="20%")
line.render('zhexian.html')
webbrowser.open('zhexian.html')


