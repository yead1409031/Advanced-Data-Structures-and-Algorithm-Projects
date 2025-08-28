class Graph:
    def __init__(self):
        self.vertList={}
        self.numVertices=0

    class __Vertex:
        #created the new object 
        def __init__(self,key): #self=newVertex, key=0 #self will be what assigned
            self.id=key#newVertex.id=0
            self.connectedTo={} #newVertex.connectedTo={}
        
        def getId(self):
            return self.id
        def getConnections(self):
            return self.connectedTo.keys()
        def getWeight(self,nbr):
            return self.connectedTo[nbr]
         #v1.addNeighbor(v1,5) #graph.vertList[0].addNeighbor(graph.vertList[1],5)
        def addNeighbor(self,nbr,weight=0): #self=graph.vertList[0],nbr=graph.vertList[1],w=5
            self.connectedTo[nbr]=weight #vgraph.vertList[0].connectedTo[graph.vertList[1]]=5 #v0.connectedTo[1]=5
        def __str__(self):
            return f"conneted to {str([x.id for x in self.connectedTo])}"
        




    def addVertex(self,key): #self=graph, key=0
        self.numVertices +=1#graph.numVertices=1
        newVertex=Graph.__Vertex(key)#Graph.__Vertex(0)
        self.vertList[key]= newVertex #self.vertList[0]= newVertex #here self is graph class
        return newVertex
    def getVertex(self,key):
        if key in self.vertList:
            return self.vertList[key]
        else:
            return None
    #vertex graph
    def __contain__(self,key):
        return (key in self.vertList)
    #graph.addEdge(0,1,5)
    def addEdge(self,source,destination,weight=0): #self=graph, source=0 dest=1,weight=5
        if source not in self.vertList: #if 0m nit in graph.vertList
            newVertex=self.addVertex(source)
        if destination not in self.vertList: #if 1 not in graph.vertList
            newVertex=self.addVertex(destination)
        
        self.vertList[source].addNeighbor(self.vertList[destination],weight)
        #v0.addNeighbor(v1,5) #graph.vertList[0].addNeighbor(graph.vertList[1],5)
        
    
    def getVertices(self):
        return self.vertList.keys()
    def __iter__(self):
        return iter(self.vertList.values())
    
def dfsRecursive(visited, graph, node):
    if node not in visited:
        visited.add(node)
        for nbr in graph[node]:
            if nbr not in visited:
                dfsRecursive(visited, graph, node)


def main():
    graph=Graph()
    print(graph.vertList)
    print()
    
    for i in range(6):
        graph.addVertex(i)#graph.addVertex(1)
    
    print(graph.vertList)
    print()
    graph.addEdge(0,1,5) # (self=graph,source=0,destination=1, weight =5)
    graph.addEdge(0,5,2)
    graph.addEdge(1,2,4)
    graph.addEdge(2,3,9)
    graph.addEdge(3,4,7)
    graph.addEdge(4,4,3)
    graph.addEdge(4,0,1)
    graph.addEdge(5,4,8)

    for vertex in graph:
        for adjacent in vertex.getConnections():
            print(f"({vertex.getId()}, {adjacent.getId()})")
        
    print()
    for k,v in graph.vertList.items():
        print(k,v)


main()

#used idea: https://favtutor.com/blogs/depth-first-search-python#:~:text=The%20recursive%20method%20of%20the,of%20the%20graph%20avoiding%20cycles.