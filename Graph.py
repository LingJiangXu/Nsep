# auther: xulingjiang
# time: 2022/6/12
# coding: utf-8

# class GraphError:
#     pass


class Graph:        #基本图类，采用邻接矩阵
    def __init__(self, mat, unconn=0):
        vnum = len(mat)
        for x in mat:
            if len(x) != vnum:  #检查是否为方阵
                raise ValueError("Argument for 'Graph'.")
        self._mat = [mat[i][:] for i in range(vnum)]    #拷贝
        self._unconn = unconn
        self._vnum = vnum

    def vertex_num(self):
        return self._vnum

    def _invalid(self, v):    #检查参数合理性
        return 0 > v or v >= self._vnum

    def add_vertex(self):
        raise GraphError("Adj-Matrix dose not support 'add_vertex'.")

    def add_edge(self, vi, vj, val=1):
        if self._invalid(vi) or self._invalid(vj):
            raise GraphError(str(vi) + 'or' + str(vj) + 'is not a valid vertex.')

        self._mat[vi][vj] = val

    def get_edge(self, vi, vj):
        if self._invalid(vi) or self._invalid(vj):
            raise GraphError(str(vi) + 'or' + str(vj) + 'is not a valid vertex.')
        return self._mat[vi][vj]

    def out_edges(self, vi):
        if self._invalid(vi):
            raise GraphError(str(vi) + 'is not a valid vertex.')
        return self._out_edges(self._mat[vi], self._unconn)

    @staticmethod
    def _out_edges(row, unconn):
        edges = []
        for i in range(len(row)):
            if row[i] != unconn:
                edges.append((i, row[i]))
        return edges


