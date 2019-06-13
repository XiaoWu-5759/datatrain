# matplotlib 数据可视化

### matplotlib库的使用

matplotlib库是由各种可视化类构成的，内部结构负载

为了方便使用

`matplotlib.pyplot`是绘制各类可视化图形的命令子库，相当于快捷方式



`import matplotlib.pyplot as plt`



### 绘图区域

![sp190613_135723](.\images\sp190613_135723.png)

nrows 行

ncols 列



### pyplot的plot()函数

![sp190613_141543](.\images\sp190613_141543.png)

其中最重要的就是format_string 用来控制曲线的格式字符串，可选

由颜色字符、风格字符和标记字符组成

##### 颜色字符

![sp190613_141818](.\images\sp190613_141818.png)

如果用户不选择颜色，系统会自动选择不同的颜色，用来绘制图片

##### 风格字符

![sp190613_141937](.\images\sp190613_141937.png)

如果打印出来的是黑白图片，颜色就不能满足

##### 标记字符

![sp190613_142022](.\images\sp190613_142022.png)

![sp190613_142224](.\images\sp190613_142224.png)



### pyplot的中文显示

1. 第一种方法

pyplot并不默认支持中文显示，需要rcParams修改字体实现

改变全局字体的参数

`matplatlib.rcParams['font.family']='SimHei'`

‘SimHei’是黑体

##### rcParams的属性

`这种方式会改变所有的文本字体属性，包括x轴和y轴的坐标`

![sp190613_143128](.\images\sp190613_143128.png)

![sp190613_143155](.\images\sp190613_143155.png)

##### 第二种方法

推荐：

在有中文输入的地方，增加一个属性：fontproperties

`plt.xlabel('横轴：时间',fontproperties='SimHei',fontsize=20,color='green')`



### pyplot的文本显示

![sp190613_144402](.\images\sp190613_144402.png)

这样绘制的图形会显得比较专业，有注释，很清楚的了解曲线的意义。

![sp190613_145036](.\images\sp190613_145036.png)

箭头的属性 {} 用字典格式，来进行说明