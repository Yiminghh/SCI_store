from pyecharts.charts import Map  # 注意这里与老版本pyecharts调用的区别
from pyecharts import options as opts
import random

import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.datasets import register_url
from pyecharts.globals import ChartType, SymbolType

import json
import os
import pandas as pd
import torch
import numpy as np
import copy



def gen_new_map(graph):

    path = os.path.join('.', 'data', '{}_mapData.csv'.format(graph))
    with open(os.path.join('.', 'data', 'USA.json'), 'r', encoding='utf-8') as fp:
        print(type(fp))  # 输出结果是 <class '_io.TextIOWrapper'> 一个文件类对象
        # load()函数将fp(一个支持.read()的文件类对象，包含一个JSON文档)反序列化为一个Python对象
        map_data = json.load(fp)

    # null, Northeast, Midwest, South, West
    dx = [0, 2, 0, 0, -2]
    dy = [0, 0.5, 1, -1, 0.3]

    cnl_data = pd.read_csv(path)
    cnl_dict = dict(zip(cnl_data['states'], cnl_data['index']))

    states_dict = pd.read_csv(os.path.join('.', 'data', 'states_map'), header=None, sep=', ', engine='python').values
    states_dict = dict(zip(states_dict[:, 1], states_dict[:, 0]))

    features = []
    for metaData in map_data["features"]:
        full_name = metaData["properties"]["name"]
        if full_name not in states_dict: continue
        short_name = states_dict[full_name]
        if short_name not in cnl_dict: continue
        # 将州的全称变为简写
        metaData["properties"]["name"] = short_name
        # 该州所在的机构编号
        ins_idx = int(cnl_data['institution_idx'][cnl_dict[short_name]])
        coor = metaData["geometry"]["coordinates"]

        for i in range(len(coor)):
            for j in range(len(coor[i])):
                if isinstance(coor[i][j][0], list):
                    for z in range(len(coor[i][j])):
                        coor[i][j][z][0] += dx[ins_idx]
                        coor[i][j][z][1] += dy[ins_idx]
                else:
                    coor[i][j][0] += dx[ins_idx]
                    coor[i][j][1] += dy[ins_idx]
        metaData["geometry"]["coordinates"] = coor
        features.append(metaData)

    # 写文件
    out_dict = {"type": "FeatureCollection", "features": features}
    with open("./data/USA_{}.json".format(graph), "w", encoding='utf-8') as f:  ## 设置'utf-8'编码
        f.write(json.dumps(out_dict, ensure_ascii=False))

def gen_map_data(graph):
    path = os.path.join('.', 'data', '{}_mapData.csv'.format(graph))
    cnl_data = pd.read_csv(path)

    for mode in ['local', 'Integrated', 'Centralized']:
        values = []
        for state, pcc in zip(cnl_data['states'], cnl_data['{}_pcc'.format(mode)]):
            values.append({"name": state, "value": pcc})

        # 写文件
        out_dict = {"values": values}
        with open("./data/{}_{}.json".format(graph, mode), "w", encoding='utf-8') as f:  ## 设置'utf-8'编码
            f.write(json.dumps(out_dict, ensure_ascii=False))

if __name__ == '__main__':
    graph = 'state360'
    gen_new_map(graph)
    gen_map_data(graph)



