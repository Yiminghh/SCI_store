import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams

"""
zorder: 设置图层位置
"""

width = 0.1  # 柱状图的宽度，可以根据自己的需求和审美来改
gap = 0.1 # 柱子间的间隔
fontsize = 14
config = {
            "font.family": 'Arial',
            "font.size": fontsize,# 相当于小四大小
            "mathtext.fontset": 'stix',#matplotlib渲染数学字体时使用的字体，和Times New Roman差别不大
            "font.serif": ['SimSun'],#宋体
            'axes.unicode_minus': False # 处理负号，即-号
         }
rcParams.update(config)

plt.figure(figsize=(6.4,7.4*(1-0.618)))#默认640*480
# 600 x 600 像素（先宽度 后高度）
# 注意这里的宽度和高度的单位是英寸，1英寸=100像素，所以要除以100





PH = [0.159, 0.198, 0.157, 0.196, 0.183, 0.193, 0.148]
Crime = [0.031, 0.033, 0.030, 0.034, 0.034, 0.03, 0.021]
Collaboration = [0.071, 0.385, 0.068, 0.108, 0.073, 0.084, 0.065]
Grid = [0.038, 0.195, 0.037, 0.04, 0.052, 0.064, 0.025]
data = np.array([PH, Crime, Collaboration, Grid])



nets = ['PH', 'Crime', 'Collaboration', 'Grid']
methods = ['BPD', 'CNE', 'GNDR', 'CoreHD', 'MinSum', 'Betweenness', 'VE']
color_list = ['#b8f0d7','#72bdf0','#fc998e','#fdc381']
#edge_color_list=["#6bc2c8","#d9d9d9","#f1bfb4","#f0d2b1"]
x = 1.3*np.arange(len(nets))  # 标签位置
interval=[]
for i in range(7):
    interval.append(i*(width+gap))

# index = np.array(range(len(methods)),dtype=float)
# for i in range(len(methods)):
#     index[i] = (width+gap)*i
index = [(width+gap)*i for i in range(len(methods))]

for x in range(len(methods)):
    for y in range(len(nets)):
        plt.bar(index[x],
                height=data[y,x],
                bottom=np.sum(data[:y, x]),
                width=width,
                color=color_list[y],
                edgecolor='w',#edge_color_list[y],
                label=nets[y],
                zorder=2)

plt.ylim(0.0, 0.4)

ax=plt.gca()
plt.tick_params(labelsize=fontsize)     #调整坐标轴数字大小
# 为y轴、标题和x轴等添加一些文本
ax.set_ylabel('${R}$', fontsize=16)
#ax.set_xlabel('Agency', fontsize=16)
# ax.set_title('这里是标题')
# ax.set_yticks([1.0,1.05,1.1,1.15,1.2])
# ax.set_yticklabels(['1.0','','1.1','','1.2'])
ax.set_xticks(index)
ax.set_xticklabels(methods, rotation=28)


# plt.legend()
# # 下面3行设置legend字体
# leg = plt.gca().get_legend()
# ltext = leg.get_texts()
# plt.setp(ltext, fontsize=fontsize)

# 设置坐标轴粗细
# ax = plt.gca()
ax.spines['bottom'].set_linewidth(1.5)  # 设置底部坐标轴的粗细
ax.spines['left'].set_linewidth(1.5)  # 设置左边坐标轴的粗细
ax.spines['right'].set_linewidth(1.5)  # 设置右边坐标轴的粗细
ax.spines['top'].set_linewidth(1.5)  # 设置上部坐标轴的粗细

plt.grid(axis='y', c="#d9d9d9", zorder=0)#添加水平直线
plt.gcf().subplots_adjust(left=0.1, right=0.99, bottom=0.28, top=0.93)


plt.savefig('../fig/stack_robustness.pdf',
            format='pdf',
            dpi=600,
            transparent=True,#设置图片背景透明
            bbox_inches='tight')
plt.show()

