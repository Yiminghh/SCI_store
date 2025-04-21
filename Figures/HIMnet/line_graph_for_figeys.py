import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import MultipleLocator
import matplotlib.ticker as mtick

font2 = {'family': 'Arial',
         'weight': 'normal',
         'size': 30,
         }

# x_tag = ['KS', 'DC', 'HI', 'ND', 'RCNN', 'MRCNN', 'HIMnet']
# color_list = ['#5ea862', '#42E292', '#26bccf', '#2ECBCB', '#c7afd6', '#fdc07c', '#f04b3c']
# figey

our_0=[0.784176443,0.777184076,0.781397123,0.77077564,0.762599226,0.76457239,0.757026034,0.772069797,0.770381724,0.746109967,0.761160656]
our_1=[0.767869568,0.765285467,0.800819297,0.761007007,0.785849821,0.767256054,0.757439399,0.751996825,0.777327609,0.768931804,0.773245484]
our_3=[0.768789319,0.760568137,0.761861545,0.765260442,0.770624695,0.759784597,0.755865913,0.753662211,0.755776252,0.754448072,0.766714698]

test = [0.78225841, 0.776456612, 0.787744897, 0.785502821, 0.762500458, 0.774349415, 0.779312918, 0.771435634,
        0.779331174, 0.765027559, 0.758452845]
our = [0.773628037, 0.770865494, 0.768435457, 0.769976335, 0.753760724, 0.746494255, 0.74584428, 0.761063947,
       0.756460328, 0.748594877, 0.748063024]
dc = [0.507522223, 0.503786137, 0.503673117, 0.50061444, 0.500119957, 0.495703337, 0.495466054, 0.49247667, 0.492782579,
      0.492778855, 0.492838179]
ks = [0.516716395, 0.51317114, 0.513996631, 0.512461613, 0.509949661, 0.506240034, 0.506149326, 0.502409874,
      0.503364118, 0.503199717, 0.503595307]
nd = [0.480845628, 0.477817818, 0.477284064, 0.474884928, 0.473614043, 0.469361639, 0.470016863, 0.467078868,
      0.467775283, 0.466986667, 0.466996053]
hi = [0.487064207, 0.483974896, 0.483795647, 0.481059523, 0.480460314, 0.475932328, 0.476483553, 0.47312495,
      0.474359801, 0.473865152, 0.473592652]

# plt.plot(list(range(11)), test, label='test_acc', marker='o', markersize=5)
x_List = [1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4, 2.6, 2.8, 3.0]
plt.plot(x_List, ks, label='KS', markersize=4, marker='s', markerfacecolor='#ffffff', markeredgewidth=2,
         color='#5ea862')
plt.plot(x_List, dc, label='DC', markersize=4, marker='v', markerfacecolor='#ffffff', markeredgewidth=2,
         color='#bcde80')
plt.plot(x_List, hi, label='HI', markersize=4, marker='o', markeredgewidth=2, markerfacecolor='#ffffff',
         color='#26bccf')
plt.plot(x_List, nd, label='ND', markersize=4, marker='D', markerfacecolor='#ffffff', markeredgewidth=2,
         color='#a0d9e4')
plt.plot(x_List, our_3, label='HiSCN', markersize=8, marker='^',markerfacecolor='#fb9b9a', markeredgewidth=2, color='#f04b3c')
#plt.plot(x_List, our_1, label='HiSCN(q=0)', markersize=8, marker='o',markerfacecolor='#fb9b9a', markeredgewidth=2, color='#f04b3c')
#plt.plot(x_List, our_1, label='HiSCN(q=1)', markersize=8, marker='v',markerfacecolor='#fb9b9a', markeredgewidth=2, color='#f04b3c')

plt.xticks(np.linspace(1.0, 3.0, 6, dtype=float), rotation=0)  # np.linspace(0,10,4)x轴的刻度
bwith = 2  # 边框宽度设置为2
ax = plt.gca()  # 获取边框
# 设置边框
ax.spines['bottom'].set_linewidth(bwith)  # 图框下边
ax.spines['left'].set_linewidth(bwith)  # 图框左边
ax.spines['top'].set_linewidth(bwith)  # 图框上边
ax.spines['right'].set_linewidth(bwith)  # 图框右边
#plt.title('2-IM on Figeys', font2)
plt.ylabel(r'$\tau$', font2)
plt.xlabel(r'$\beta/ \beta_c$', font2)  # 纵坐标轴标题
plt.tick_params(labelsize=25)
plt.legend(prop={'size': 18})
plt.rcParams.update({'font.size': 18})

bwith = 2  # 边框宽度设置为2
ax = plt.gca()  # 获取边框
# 设置边框
ax.spines['bottom'].set_linewidth(bwith)  # 图框下边
ax.spines['left'].set_linewidth(bwith)  # 图框左边
ax.spines['top'].set_linewidth(bwith)  # 图框上边
ax.spines['right'].set_linewidth(bwith)  # 图框右边


plt.ylabel(r'$\tau$', font2)
plt.xlabel(r'$\beta/ \beta_c$', font2)  # 纵坐标轴标题
plt.tick_params(labelsize=25)
# plt.legend(prop={'size': 18})
plt.rcParams.update({'font.size': 18})
plt.gcf().subplots_adjust(left=0.16, right=0.96, bottom=0.21, top=0.96)

plt.savefig('../fig/himnet_figeys.svg',
            format='svg',
            dpi=600,
            transparent=True,#设置图片背景透明
            bbox_inches='tight')
plt.show()
