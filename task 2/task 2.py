class Graph:
    # 0 - White, 1 - Grey, 2 - Black
    def __init__(self, n):
        self.n = n
        self.adj = [[] for _ in range(n)]
        self.colors = [0] * n
        self.count = 0

    def AddEdge(self, a, b):
        self.adj[a].append(b)
        self.adj[b].append(a)

    def GetChildren(self, a):
        return self.adj[a]

    def DFS(self, start):
        self.colors[start] = 1

        for ch in self.GetChildren(start):
            if self.colors[ch] == 0:
                self.DFS(ch)
            
        self.colors[start] = 2
    
    def Count_of_components(self):
        for i in range(self.n):
            if (self.colors[i] == 0):
                self.DFS(i)
                self.count+=1
    
    def PrintResult(self):
        self.Count_of_components()
        print(self.count - 1)

v, e = list(map(int, input('Кол-во вершин Кол-во рёбер: ').split(' ')))
g = Graph(v)

for i in range(e):
    temp = list(map(int, input(f'Введите ребро {i + 1}: ').split(' ')))
    g.AddEdge(temp[0] - 1, temp[1] - 1)

g.PrintResult()

