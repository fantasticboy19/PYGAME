from pyecharts.charts import Bar
from pyecharts import options as opts
from pyecharts.charts import Pie
import random
from pyecharts.faker import Faker
from pyecharts.charts import Line

from pyecharts.charts import HeatMap
from pyecharts.charts import Map, Geo, Map3D

from visualization import vaccine

# 渲染成图片
from pyecharts.render import make_snapshot
from snapshot_selenium import snapshot


# bar = Bar()
# bar.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
# bar.add_yaxis("商家A",[5, 20, 36, 10, 75, 90])
# bar.render("mychart.html")

bar2 = (
    Bar()
    .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
    .add_yaxis("商家B", [56,23,12,44,55,66])
    .set_global_opts(title_opts=opts.TitleOpts(title="主标题", subtitle="副标题"))
)

#bar2.render("商家B的图表.html")


# 生成热力图

def heatmap_base() -> HeatMap:
    value = [[i, j, random.randint(0, 50)] for i in range(24) for j in range(7)]
    c = (
        HeatMap()
        .add_xaxis(Faker.clock)
        .add_yaxis("series0", Faker.week, value)
        .set_global_opts(
            title_opts=opts.TitleOpts(title="HeatMap-基本示例"),
            visualmap_opts=opts.VisualMapOpts(),
        )
    )
    return c.render("6.html")
# heatmap_base()


# 生成饼状图
def pie_base() -> Pie:
    c = (
        Pie()
        .add("", [list(z) for z in zip(Faker.choose(), Faker.values())])
        .set_global_opts(title_opts=opts.TitleOpts(title="Pie-基本示例"))
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    )
    return c.render("13.html")

# 生成世界地图2d
# data
data_json = {'武汉市':100,'黄冈市':50,'孝感市':30,'荆门市':20}
def map_world() -> Map:
    # value = [95.1, 23.2, 43.3, 66.4, 88.5]
    # attr = ["China", "Canada", "Brazil", "Russia", "United States"]
    # value = [val for val in data_json.values()]
    # attr = [key for key in data_json.keys()]
    value, attr = vaccine.val_attr()
    attr.pop(-1)
    value.pop(-1)
    print(attr)
    attr[-3] = '恩施土家族苗族自治州'
    attr[-1] = '神农架林区'
    print(attr)
    c = (
        Map()
        .add("疫情示意图", [list(z) for z in zip(attr, value)], maptype='湖北')
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Map-湖北省疫情示意图"),
            visualmap_opts=opts.VisualMapOpts(min_=0, max_=50000),

        )
    )
    return c.render("湖北省疫情分析图.html")



class every:
    class_name = '6ban'
    def __init__(self, name):
        super(every, self).__init__()
        self.name = name

    def say_myname(self):
        print(self.name)

    @classmethod
    def loc_myclass(cls):
        print(cls.class_name)
# show me the reason

def line_graph():
    line = Line()
    line.add_xaxis(Faker.choose())
    line.add_yaxis(series_name='A', y_axis=Faker.values())
    line.add_yaxis('B', Faker.values())
    line.set_global_opts(title_opts=opts.TitleOpts(title='折线图'))
    line.render(
        'line.html'
    )

def geo_base():
    geo = (
        Geo()
        .add_schema(maptype="china")
        .add("geo", [list(z) for z in zip(Faker.provinces, Faker.values())])
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(),
            title_opts=opts.TitleOpts(title="Geo-基本示例"),
        )
    )
    geo.render('geo.html')

if __name__ == '__main__':
    # pie_base()
    # html = map_world()
    # make_snapshot(snapshot, html, 'world_map.png')
    # geo_base()
    map_world()