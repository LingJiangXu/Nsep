# auther: xulingjiang
# time: 2022/6/14
# coding: utf-8

class PrioQueueError(ValueError):
    pass

class PrioQue:
    def __init__(self, elist=[]):
        self._elems = list(elist)
        self._elems.sort(reverse=True)

    def enqueue(self, e):
        i = len(self._elems) - 1
        while i >= 0:
            if self._elems[i] <= e:
                i -= 1
            else:
                break
        self._elems.insert(i+1,e)

    def is_empty(self):
        return not self._elems

    def peek(self):
        if self.is_empty():
            raise PrioQueueError("in top")
        return self._elems[-1]

    def dequeue(self):
        if self.is_empty():
            raise PrioQueueError("in pop")
        return self._elems.pop()


def Dijkstra_shortest_path(graph, v0):
    vnum = graph.vertex_num()
    assert 0 <= v0 < vnum

    paths = [None] * vnum
    count = 0
    cands = PrioQue([(0, v0, v0)])

    while count < vnum and not cands.is_empty():
        plen, u, vmin = cands.dequeue()
        if paths[vmin]:
            continue
        paths[vmin] = (u, plen)

        for v, w in graph.out_edges(vmin):
            if not paths[v]:
                cands.enqueue((plen + w, vmin, v))
        count += 1
    return paths


