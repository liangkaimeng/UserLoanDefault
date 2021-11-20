# coding: utf-8 -*-
# author: 梁开孟
# date：2021/11/16 0016 20:32

"""
    Version 0.1: ROC_AUC = 0.92235835
"""

import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.utils import shuffle

pd.set_option('display.width', 500)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
plt.rcParams['font.sans-serif'] = ['FangSong']
plt.rcParams['axes.unicode_minus'] = False


class NumberFeature(object):
    def __init__(self, data):
        data['income_len'] = data['income'].astype(str).apply(len)
        print(data.head())

        # category_diff_plot(data, 'income_len')




def category_diff_plot(data, field,
                       target='label',
                       length=8, wide=6,
                       x=0.05, y=50, fs=6):
    plt.figure(figsize=(length, wide), dpi=300)
    plt.title('{} VS {}'.format(field, target))
    ax = sns.countplot(field, hue=target, data=data)
    res = []
    for i in range(len(ax.patches)):
        res.append(ax.patches[i].get_height())

    n = int(len(res) / 2)
    for i, j in zip(range(len(res)), res):
        if i <= n - 1:
            ax.annotate('{} ({:.2%})'.format(j, j / (res[i] + res[i + n])),
                        (ax.patches[i].get_x() + x, ax.patches[i].get_height() + y), fontsize=fs)
        else:
            ax.annotate('{} ({:.2%})'.format(j, j / (res[i] + res[i - n])),
                        (ax.patches[i].get_x() + x, ax.patches[i].get_height() + y), fontsize=fs)
    plt.show()

if __name__ == '__main__':
    train = pd.read_csv('data/train.csv')
    train['tag'] = 'train'
    test = pd.read_csv('data/test.csv')
    test['tag'] = 'test'
    data = train.append(test)
    data = shuffle(data)
    data.index = range(len(data))
    NumberFeature(data)