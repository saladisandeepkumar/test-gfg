class Solution:
    class Graph:
        def __init__(self, V):
            self.V = V
            self.adj = {i: [] for i in range(V)}

        def add_edge(self, u, v):
            self.adj[u].append(v)
            self.adj[v].append(u)

        def is_cycle_util(self, v, visited, parent):
            visited[v] = True
            for neighbor in self.adj[v]:
                if not visited[neighbor]:  
                    if self.is_cycle_util(neighbor, visited, v):
                        return True
                elif neighbor != parent:  
                    return True
            return False

        def is_cycle(self):
            visited = [False] * self.V
            for i in range(self.V):
                if not visited[i]:  
                    if self.is_cycle_util(i, visited, -1):
                        return True
            return False

    def isCycle(self, V, edges):
        graph = self.Graph(V)  
        for u, v in edges:
            graph.add_edge(u, v)  
        return graph.is_cycle()
#{ 
 # Driver Code Starts
import sys
#Position this line where user code will be pasted.


def main():
    tc = int(input())
    for _ in range(tc):
        V = int(input())
        E = int(input())
        edges = []
        for _ in range(E):
            u, v = map(int, input().split())
            edges.append((u, v))

        obj = Solution()
        ans = obj.isCycle(V, edges)
        print("true" if ans else "false")
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends