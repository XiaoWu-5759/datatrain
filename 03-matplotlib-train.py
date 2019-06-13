
import matplotlib.pyplot as plt
import numpy as np


def show_plot():
    # plt.plot([3, 1, 4, 5, 2])
    # # plot 只有一个输入列表或数组时，参数被作为Y轴，X轴以索引自动生成
    # plt.ylabel("grande")
    # # 输出为图像存储，默认PNG格式
    # # 需要先输出，再展示
    # plt.savefig('./test', dpi=600)
    # plt.show()

    plt.plot([0,2,4,6,8],[3, 1, 4, 5, 2])
    # 分别对应x，y轴
    plt.ylabel("grande")
    # x轴和y轴的尺度 ，需要四个参数，前两个限制x轴
    plt.axis([-1,10,0,6])
    plt.show()

def image_kind():
    a = np.arange(10)
    # go- 绿色 圆圈 实线连接
    plt.plot(a,a*1.5,"go-",a, a*2.5,"rx",a,a*3.5,"*",a, a*4.5, "b-.")
    plt.show()

def image_text():
    a = np.arange(0.0,5.0,0.02)
    plt.plot(a,np.cos(2*np.pi*a),'r--')
    # tex latex的 格式文本
    # 以$ 包装起来的字段

    plt.xlabel('横轴：时间',fontproperties='SimHei',fontsize=15,color='green')
    plt.ylabel('纵轴：振幅', fontproperties='SimHei', fontsize=15)
    plt.title(r'正弦波实例 $y=cos(2\pi x)$', fontproperties='SimHei', fontsize=20)
    # plt.text(2, 1, r'$\mu=100$', fontsize=15)
    plt.annotate(r'$\mu=100$', xy=(2, 1), xytext=(3, 1.5), arrowprops=dict(facecolor='black', shrink=0.1, width=2))
    plt.axis([-1, 6, -2, 2])
    plt.grid(True)  # 显示网格
    plt.show()

if __name__ == '__main__':
    # show_plot()
    # image_kind()
    image_text()