class Graph:
    def __init__(self):
        self.nodes = []
        self.matrix = []
    

    def add_node(self, val):
        if val in self.nodes:
            return

        self.nodes.append(val)
        if len(self.matrix) == 0:
            self.matrix.append([0])
            return

        # Add column for matrix
        for row in self.matrix:
            row.append(0)
        # Add row for matrix
        self.matrix.append([0] * len(self.nodes))


    def add_edge(self, n1, n2, val):
        if n1 not in self.nodes or n2 not in self.nodes:
            return
        i1, i2 = self.nodes.index(n1), self.nodes.index(n2)
        self.matrix[i1][i2] = val
    
    def shortest_path(self, start, end, path=[]):
        path = path.append(start)
        if start == end:
            return path, None
        shortest = None
        res = 0
        for node in self.nodes:
            if node not in path:
                weight = self.matrix[start][self.nodes.index(node)]
                newpath = self.shortest_path(node, end, path)

        return shortest, res

    def __str__(self):
        res = f'\t{" ".join(str(x) for x in self.nodes)}\n'
        for i, row in enumerate(self.matrix):
            res += str(self.nodes[i]) + "\t"
            res += " ".join(str(x) for x in row)
            res += "\n"
        return res


def main():
    graph = Graph()
    graph.add_node(2)
    graph.add_node(4)
    graph.add_node(5)
    graph.add_edge(2, 4, 6)
    print(graph)

if __name__ == "__main__":
    main()