from collections import defaultdict 
from pytest import set_trace
  
class Graph: 
    def __init__(self): 
        self._graph = dict()
        self.node_count = 0
        self.nodes = set()
  
    def insert(self, id_, el): 
        if id_ in self._graph:
            self._graph[id_].append(el) 
        else:
            self._graph[id_] = [el]
        self.node_count += 1
        self.nodes.add(el)
        self.nodes.add(id_)
  
    def get_graph(self):
        return self._graph
  
    def sort(self): 
        visited = defaultdict(lambda: False)
        stack =[] 
  
        def _sort(v, visited, stack): 
            visited[v] = True
      
            for node in self._graph.get(v, []):
                print('node', node)
                if visited[node] == False: 
                    _sort(node, visited, stack) 

      
            if v in self._graph.get(node, []):
                print('cycle!', node, v)
            else:
                stack.insert(0, v) 
            print('stack', stack)

        for v in sorted(self._graph.keys()): 
            print(v)
            if visited[v] == False: 
                _sort(v, visited, stack) 

        return stack
  
  
graph = Graph() 
graph.insert(0, 1)
graph.insert(1, 2)
graph.insert(2, 3)
graph.insert(3, 2)
  
sorted_list = graph.sort() 
print(sorted_list)
