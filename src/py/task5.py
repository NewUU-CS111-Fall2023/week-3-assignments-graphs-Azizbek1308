class TagGame:
    def __init__(self, n, x):
        self.n = n
        self.adj_list = [[] for _ in range(n + 1)]
        self.x = x

    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def calculate_moves(self):
        visited = [False] * (self.n + 1)
        distance = [0] * (self.n + 1)

        stack = [(self.x, 0)]

        while stack:
            vertex, dist = stack.pop()

            if visited[vertex]:
                continue

            visited[vertex] = True
            distance[vertex] = dist

            for neighbor in self.adj_list[vertex]:
                stack.append((neighbor, dist + 1))

        max_distance = max(distance)
        return max_distance * 2

if __name__ == "__main__":
    n, x = map(int, input().split())
    game = TagGame(n, x)

    for _ in range(n - 1):
        a, b = map(int, input().split())
        game.add_edge(a, b)

    moves = game.calculate_moves()
    print(moves)