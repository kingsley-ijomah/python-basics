NODE, EDGE, ATTR = range(3)


class Node:
    def __init__(self, name, attrs):
        self.name = name
        self.attrs = attrs

    def __eq__(self, other):
        return self.name == other.name and self.attrs == other.attrs


class Edge:
    def __init__(self, src, dst, attrs):
        self.src = src
        self.dst = dst
        self.attrs = attrs

    def __eq__(self, other):
        return (self.src == other.src and
                self.dst == other.dst and
                self.attrs == other.attrs)


class Graph:
    def __init__(self, data=None):
        self.nodes = []
        self.edges = []
        self.attrs = {}
        self.data = data or []
        
        if type(self.data) != list: raise TypeError('Type Error')
        for tuple in self.data:
            if len(tuple) < 2: raise TypeError('Type Error')

        for (key, *args) in self.data:
            if key == NODE:
                if len(args) != 2: raise ValueError('Invalid Value')
                self.nodes.append(Node(*args))
            elif key == EDGE:
                if len(args) != 3: raise ValueError('Invalid Value')
                self.edges.append(Edge(*args))
            elif key == ATTR:
                if len(args) != 2: raise ValueError('Invalid Value')
                name, value = args
                self.attrs[name] = value
            else:
                raise ValueError('Invalid Value')
