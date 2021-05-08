class Node(object):
    def __init__(self, name):
        """Assumes name is a string"""
        self.name = name
    def getName(self):
        return self.name
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.__str__()

class Edge(object):
    def __init__(self, src, dest):
        """Assumes src and dest are nodes"""
        self.src = src
        self.dest = dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __str__(self):
        return self.src.getName() + '->' + self.dest.getName()
               
class Digraph(object):
    """edges is a dict mapping each node to a list of
    its children"""
    def __init__(self):
        self.edges = {}
    def addNode(self, node):
        if node in self.edges:
            raise ValueError('Duplicate node')
        else:
            self.edges[node] = []
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not (src in self.edges and dest in self.edges):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)
    def childrenOf(self, node):
        return self.edges[node]
    def hasNode(self, node):
        return node in self.edges
    def getNode(self, name):
        for n in self.edges:
            if n.getName() == name:
                return n
        raise NameError(name)
    def __str__(self):
        result = ''
        for src in self.edges:
            for dest in self.edges[src]:
                result = result + src.getName() + '->'\
                         + dest.getName() + '\n'
        return result[:-1] #omit final newline

class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, rev)
    
def buildCityGraph(graphType):
    g = graphType()
    for name in ('ABC', 'BAC', 'ACB', 'BCA', 'CAB', 'CBA'): #Create 7 nodes
        g.addNode(Node(name))
    g.addEdge(Edge(g.getNode('ABC'), g.getNode('BAC')))
    g.addEdge(Edge(g.getNode('ABC'), g.getNode('ACB')))
    g.addEdge(Edge(g.getNode('BAC'), g.getNode('BCA')))
    g.addEdge(Edge(g.getNode('ACB'), g.getNode('CAB')))
    g.addEdge(Edge(g.getNode('BCA'), g.getNode('CBA')))
    g.addEdge(Edge(g.getNode('CAB'), g.getNode('CBA')))
    return g
print(buildCityGraph(Graph))


def printPath(path):
    """Assumes path is a list of nodes"""
    result = ''
    for i in range(len(path)):
        result = result + str(path[i])
        if i != len(path) - 1:
            result = result + '->'
    return result 


def DFSpath(graph, start, end, path, shortest):
    path = path + [start]
    if start == end:
        return path
    else:
        for node in graph.childrenOf(start):
            if node not in path:
                if shortest == None or len(path) < len(shortest):
                    new = DFSpath(graph, node, end, path, shortest)
                    if new != None:
                        shortest = new
    return shortest

def shortestPath(graph, start, end):
    """Assumes graph is a Digraph; start and end are nodes
       Returns a shortest path from start to end in graph"""
    return DFSpath(graph, start, end, [], None)

def testSP(source, destination):
    g = buildCityGraph(Graph)
    sp = shortestPath(g, g.getNode(source), g.getNode(destination))
    if sp != None:
        print('Shortest path from', source, 'to',
              destination, 'is', printPath(sp))
    else:
        print('There is no path from', source, 'to', destination)

def BFS(graph, start, end, toPrint = False):
    """Assumes graph is a Digraph; start and end are nodes
       Returns a shortest path from start to end in graph"""
    initPath = [start]
    pathQueue = [initPath]
    while len(pathQueue) != 0:
        print('Current path queue:', pathQueue)
        #Get and remove oldest element in pathQueue
        tmpPath = pathQueue.pop(0)
        if toPrint:
            print('Current BFS path:', printPath(tmpPath))
        lastNode = tmpPath[-1]
        if lastNode == end:
            return tmpPath
        for nextNode in graph.childrenOf(lastNode):
            if nextNode not in tmpPath:
                newPath = tmpPath + [nextNode]
                pathQueue.append(newPath)
    return None

def shortestPath(graph, start, end, toPrint = False):
    """Assumes graph is a Digraph; start and end are nodes
       Returns a shortest path from start to end in graph"""
    return BFS(graph, start, end, toPrint)

#testSP('Chicago', 'Boston')
testSP('ABC', 'CAB')
