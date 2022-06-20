# auther: xulingjiang
# time: 2022/6/14
# coding: utf-8

import math
import os

from Graph import Graph
from Dijkstra import Dijkstra_shortest_path

# 导入字典，并以空格分开
dic = open("C:/Users/18282/Desktop/Python/dict(1)/cnc.txt","r",encoding='utf-8')
the_dic = dic.read().split(" ")
dic.close()

# 输入带分词的中文句子，生成字符列表，生成对应初始邻接矩阵（值全为零）
string = input("Please input the string that you want to N-seq:\n")
str_list = list(string)
mat = [[0] * (len(string) + 1) for _ in range(len(string) + 1)]

# 填充邻接矩阵（值为相应字符串在语料库中频率的负对数）
for i in range(len(string)):
    for j in range(len(string) + 1):
        if j > i and string[i:j] in the_dic:
            mat[i][j] = -math.log2(the_dic.count(string[i:j]) / len(the_dic))

# 将字符矩阵（值为相应字符串）写入mat.csv文件
with open('./mat.csv', 'w', encoding='utf-8') as f:
    str_mat = ''
    for i in range(len(mat)):
        for j in range(len(mat)):
            str_mat += ''.join(str_list[i:j]) + ',' if mat[i][j] else str(mat[i][j]) + ','
        str_mat = str_mat[:-1] + '\n'
    f.write(str_mat)

# 由邻接矩阵生成图，并求最短路径
str_graph = Graph(mat)
paths = Dijkstra_shortest_path(str_graph, 0)
v, e = paths[-1]

# 根据最短路径，以“/”划分词
while v:
    str_list.insert(v,'/')
    v, e = paths[v]
print("The string after N-seq is:\n", ''.join(str_list))

# 调用R脚本，绘制字符串生成的图结构示意
direct = ('Rscript C:/Users/18282/Desktop/Python/Nsep/show_str_graph.R')
p = os.system(direct)

