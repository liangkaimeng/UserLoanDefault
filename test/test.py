# coding: utf-8 -*-
# author: 梁开孟
# date：2021/10/16 0016 22:33

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.width', 180)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', 100)
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# Proportion of category features in positive samples
def _category(data, field, target,
              sample=8, ind=8, col=6,
              save=False, dpi=400,
              inche="tight"):
    print("{}各个枚举值对正例样本的占比：".format(field))
    unique_count = len(data[field].unique())
    if unique_count <= sample:
        plt.figure(figsize=(ind, col))
        title = "{} VS {}".format(field, target)
        plt.title(title)
        sns.countplot(field, hue=target, data=data)
        if save:
            plt.savefig(title + ".jpg", dpi=dpi, bbox_inches=inche)
        plt.show()

    postive_rate_set = {}
    for item in data[field].unique().tolist():
        rate = round(data[data[field] == item].groupby([target])[field].count()[1] / len(data) * 100, 2)
        postive_rate_set[item] = "{}%".format(rate)
    return postive_rate_set




if __name__ == "__main__":
    file = "../data/train.csv"
    data = pd.read_csv(file)
    a = _category(data, "car_ownership", "label", save=False)
    print(a)