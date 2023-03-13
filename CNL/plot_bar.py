import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams

"""
zorder: 设置图层位置
"""

width = 0.2  # 柱状图的宽度，可以根据自己的需求和审美来改
gap = 0.03 # 柱子间的间隔
fontsize = 13
font2 = {'family': 'Times New Roman',#Arial
         'weight': 'normal',
         'size': 30,
         }
config = {
            "font.family": 'serif',
            "font.size": fontsize,# 相当于小四大小
            "mathtext.fontset": 'stix',#matplotlib渲染数学字体时使用的字体，和Times New Roman差别不大
            "font.serif": ['SimSun'],#宋体
            'axes.unicode_minus': False # 处理负号，即-号
         }
rcParams.update(config)

plt.figure(figsize=(6.4,3.2*0.618))#默认640*480
# 600 x 600 像素（先宽度 后高度）
# 注意这里的宽度和高度的单位是英寸，1英寸=100像素，所以要除以100


labels = ['US-states', 'US-regions', 'Spain','Twitter']
# GAT模型数据
# local_=np.array([0.805, 0.768, 0.236, 0.865])
# integrated_=np.array([0.849, 0.779, 0.275, 0.876])
# centralized_ = np.array([0.865, 0.789, 0.386, 0.959])
# SAGE模型结果
local_=np.array([0.851,0.724,0.149,0.959])
integrated_=np.array([0.852,0.765,0.401,0.961])
centralized_ = np.array([0.872,0.701,0.319,0.958])

integrated_ = integrated_/local_
centralized_ = centralized_/local_
local_ = local_/local_

x = 0.9*np.arange(len(labels))  # 标签位置


#fig, ax = plt.subplots()

plt.bar(x - width-gap, local_, width, label='Local',color='#86888c',zorder=2)
plt.bar(x ,             integrated_, width, label='Integrated',color='#ff2e17',zorder=2)
plt.bar(x + width+gap, centralized_, width, label='Centralized',color='#ffca36',zorder=2)
# rects4 = ax.bar(x + width+ 0.03, d, width, label='d')
# rects5 = ax.bar(x + width*2 + 0.04, e, width, label='e')

# for a,b in zip(x- width-gap,local_):   #柱子上的数字显示
#  plt.text(a,b,'%.3f'%b,ha='center',va='bottom',fontsize=9);
#
# for a,b in zip(x,integrated_):   #柱子上的数字显示
#  plt.text(a,b,'%.3f'%b,ha='center',va='bottom',fontsize=9);
#
# for a, b in zip(x+ width+gap, centralized_):  # 柱子上的数字显示
#  plt.text(a, b, '%.3f' % b, ha='center', va='bottom', fontsize=9);


plt.ylim(0.98, 1.2)

ax=plt.gca()
plt.tick_params(labelsize=fontsize)     #调整坐标轴数字大小
# 为y轴、标题和x轴等添加一些文本
ax.set_ylabel('${PCC/PCC_{Local}}$',font2, fontsize=16)
#ax.set_xlabel('Agency', fontsize=16)
# ax.set_title('这里是标题')
ax.set_yticks([1.0,1.05,1.1,1.15,1.2])
ax.set_yticklabels(['1.0','','1.1','','1.2'])
ax.set_xticks(x)
ax.set_xticklabels(labels)


plt.legend()
# 下面3行设置legend字体
leg = plt.gca().get_legend()
ltext = leg.get_texts()
plt.setp(ltext, fontsize=fontsize)

# 设置坐标轴粗细
# ax = plt.gca()
ax.spines['bottom'].set_linewidth(1.5)  # 设置底部坐标轴的粗细
ax.spines['left'].set_linewidth(1.5)  # 设置左边坐标轴的粗细
ax.spines['right'].set_linewidth(1.5)  # 设置右边坐标轴的粗细
ax.spines['top'].set_linewidth(1.5)  # 设置上部坐标轴的粗细

plt.grid(axis='y', c="#d9d9d9", zorder=0)#添加水平直线
plt.gcf().subplots_adjust(left=0.12, right=0.99, bottom=0.15, top=0.93)


plt.savefig('../fig/empirical_results_GAT.svg',
            format='svg',
            dpi=600,
            transparent=True,#设置图片背景透明
            bbox_inches='tight')
plt.show()

