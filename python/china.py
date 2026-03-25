from pyecharts.charts import Map
from pyecharts import options as opts
import webbrowser

value1 = [657,739,639,619, 568,608,575, 579, 462,654,
          663,653,643,608,637,633,634,632,636,618,
          630,620,642,662,633,559,541,590,598,634,
          633,565]
attr1 = ['北京市','海南省',"福建省", "山东省", "上海市", "甘肃省", "新疆维吾尔自治区", "广西壮族自治区","西藏自治区",'天津市',
         '浙江省','安徽省','重庆市','甘肃省','广东省','贵州省','河北省','河南省','黑龙江省','湖北省',
         '湖南省','江西省','江苏省','辽宁省','内蒙古自治区','宁夏回族自治区','青海省','山西省','陕西省','四川省',
         '云南省','吉林省']
map1 = Map()
datas1=list(zip(attr1,value1))
map1.add(
    series_name="",
    data_pair=datas1,
    maptype="china",
    label_opts=opts.LabelOpts(is_show=True),
    tooltip_opts=opts.TooltipOpts(formatter='{b}:{c}',trigger='item'),

)
map1.set_global_opts(title_opts=opts.TitleOpts(title='2024年北京师范大学各省最低分数线'),
    visualmap_opts=opts.VisualMapOpts(is_show=True,min_=min(value1),max_=max(value1),range_color=["pink","red"]))

init=opts.InitOpts(width='1600px', height='800px')



map1.render('china.html')
webbrowser.open('china.html')
