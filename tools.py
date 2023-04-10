import fire
from collections import Counter
import matplotlib as mpl
from typing import *
import pandas as pd
import matplotlib.pyplot as plt

COLOR = ['black', 'magenta', 'green', 'yellow', 'cyan']

def plot(arg = '1'):
    # 将arg命令进行解码成List[int] 然后把列表中每个元素index
    # 将{index}.csv文件的数据画成图显示出来
    # csv的格式，总共有5列
    # 其中最简单的是两列 action 和 point
    # action是每回合采取的行动（打鸟牌 0，拿食物 1，下蛋 2，抽卡 3）
    # point是自己和对方一回合行动结束后自己的总分
    # 更详细一点的是加上了 food egg card列
    mpl.rcParams['axes.labelsize'] = 20
    #index = _parse(arg)
    index = int(arg)
    fig = plt.figure(constrained_layout = True, figsize = (12,6))
    ax1 = plt.subplot2grid((3, 2), (0, 0), rowspan = 3)
    ax2 = plt.subplot2grid((3, 2), (0, 1))
    ax2.set_xticks([])
    ax3 = plt.subplot2grid((3, 2), (1, 1))
    ax3.set_xticks([])
    ax4 = plt.subplot2grid((3, 2), (2, 1))
    df = pd.read_csv(f'{index}.csv')
    # 画4个图，分别是point，food，egg，card
    ax1.set_xlabel("Turn")
    ax4.set_xlabel("Turn")
    ax1.plot(range(27), df.point.values, linewidth = 3, zorder = 1, color = 'black', label = "point")
    ax1.scatter(range(27), df.point.values, zorder = 2, color = [COLOR[i + 1] for i in df.action.values])
    special_axes = fig.add_axes((0.1, 0.7, 0.2, 0.2), title = "Actions")
    c = Counter(df.action.values)
    special_axes.pie([c[0], c[1], c[2], c[3]], labels = [f'Bird:{c[0]}', f'Food:{c[1]}', f'Egg:{c[2]}', f'Card:{c[3]}'], colors = ['magenta', 'green', 'yellow', 'cyan'], autopct = '%.1f%%', shadow = True, explode = (0, 0, 0.1, 0))
    # 接下来画food，egg，card的资源
    ax2.plot(range(27), df.food.values, linewidth = 3, zorder = 1, color = 'black', label = "food")
    ax2.scatter(range(27), df.food.values, zorder = 2, color = [COLOR[i + 1] for i in df.action.values])
    ax3.plot(range(27), df.egg.values, linewidth = 3, zorder = 1, color = 'black', label = "egg")
    ax3.scatter(range(27), df.egg.values, zorder = 2, color = [COLOR[i + 1] for i in df.action.values])
    ax4.plot(range(27), df.card.values, linewidth = 3, zorder = 1, color = 'black', label = "card")
    ax4.scatter(range(27), df.card.values, zorder = 2, color = [COLOR[i + 1] for i in df.action.values])

    ax1.legend(prop = {'size' : 15})
    ax2.legend(prop = {'size' : 15})
    ax3.legend(prop = {'size' : 15})
    ax4.legend(prop = {'size' : 15})
    #def on_move(event):
    #    if event.inaxes == ax1:
    #        print(f'data coords {event.xdata} {event.ydata}')
    #plt.connect('motion_notify_event', on_move)
    plt.show()


def _parse(argument : str = '1') -> List[int]:
    # 这个是将字符串argument进行解析
    # 1 2 3 解析成1 2 3
    # 1-3 解析成 1 2
    # 1-5-2 解析成1 3
    # 1-5-2 4 解析成 1 3 4
    args = argument.split()
    numbers = set()
    for arg in args:
        if '-' in arg:
            arg = arg.split('-')
            if len(arg) == 2: arg.append('1')
            for i in range(int(arg[0]), int(arg[1]), int(arg[2])):
                numbers.add(i)
        else:
            numbers.add(int(arg))
    return list(numbers)


if __name__ == '__main__':
    fire.Fire()
