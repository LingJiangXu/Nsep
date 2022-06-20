# auther: xulingjiang
# time: 2022/6/14
# coding: utf-8

# 使用数组定义优先队列
class PrioQueueError(ValueError):
    pass

class PrioQue:
    def __init__(self, elist=[]):
        self._elems = list(elist)       # 将输入elist转化为list，默认为空数组
        self._elems.sort(reverse=True)      # 将数组降序排序（越后优先级越高）

    def enqueue(self, e):       # 在数组中添加元素e
        i = len(self._elems) - 1        # 初始i为末尾元素下标
        while i >= 0:           # 用e从数组尾部逐项对比，直至比e小的第一个元素下表i或者遍历完后的i=-1为止。
            if self._elems[i] <= e:
                i -= 1
            else:
                break
        self._elems.insert(i+1,e)      # 在对比后的i位置后插入e

    def is_empty(self):     # 判断数组是否为空
        return not self._elems

    def peek(self):     # 显示数组最优先（最后）的元素，但不弹出
        if self.is_empty():
            raise PrioQueueError("in top")
        return self._elems[-1]

    def dequeue(self):      # 弹出最优先元素
        if self.is_empty():
            raise PrioQueueError("in pop")
        return self._elems.pop()


# 根据以上优先队列定义dijkstra求最短路径函数
def Dijkstra_shortest_path(graph, v0):     # 从vo开始的到其余各点的最短路径，返回值为元组列表，元组由后驱节点的前一节点及其最短路径长。
    vnum = graph.vertex_num()       # 获取图的节点数
    assert 0 <= v0 < vnum

    paths = [None] * vnum       # 生成长度为节点数的，值为空的最短路径列表（用于存储最终路径结果）
    count = 0               # 循环计数器
    cands = PrioQue([(0, v0, v0)])      # 优先队列，将下一候选节点加入优先队列

    while count < vnum and not cands.is_empty():
        plen, u, vmin = cands.dequeue()     # plen、u、vmin分别为最优队列最短路径的路径长、后驱节点的前一节点、后驱节点。
        if paths[vmin]:             # 如果后驱节点已在最短路径列表里，跳过，否则将（后驱节点前一节点，最短路径长）加入最短路径列表。
            continue
        paths[vmin] = (u, plen)

        for v, w in graph.out_edges(vmin):      # 将以刚刚加入最短路径列表的后驱节点作为前驱节点，返回所有的后驱节点及其最短路径，加入优先队列。
            if not paths[v]:
                cands.enqueue((plen + w, vmin, v))
        count += 1          # 计数器加1，防止已经寻得所有节点最短路径，仍继续循环，导致优先队列中的非最短路径覆盖最短路径列表里的值。
    return paths           # 返回最短路径列表


