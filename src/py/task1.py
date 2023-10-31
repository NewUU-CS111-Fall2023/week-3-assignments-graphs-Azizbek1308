import heapq


class CityGraph:
    def __init__(self, num_cities, num_roads, num_forbidden_triplets):
        self.num_cities = num_cities
        self.adj_list = [[] for _ in range(num_cities + 1)]
        self.num_roads = num_roads
        self.num_forbidden_triplets = num_forbidden_triplets

    def add_road(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def find_shortest_path(self, forbidden_triplets):
        distances = [float('inf')] * (self.num_cities + 1)
        distances[1] = 0

        prev_city = [None] * (self.num_cities + 1)
        visited = [False] * (self.num_cities + 1)

        heap = [(0, 1)]

        while heap:
            dist, city = heapq.heappop(heap)

            if visited[city]:
                continue

            visited[city] = True

            for neighbor in self.adj_list[city]:
                if visited[neighbor]:
                    continue

                new_dist = dist + 1

                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    prev_city[neighbor] = city
                    heapq.heappush(heap, (new_dist, neighbor))

        if distances[self.num_cities] == float('inf'):
            return -1, []

        for triplet in forbidden_triplets:
            a, b, c = triplet
            if distances[a] + 1 == distances[b] and distances[b] + 1 == distances[c]:
                return -1, []

        path = [self.num_cities]
        curr_city = self.num_cities
        while curr_city != 1:
            prev = prev_city[curr_city]
            path.append(prev)
            curr_city = prev

        path.reverse()

        return distances[self.num_cities], path


n, m, k = map(int, input("Enter the number of cities, number of roads, and number of forbidden triplets: ").split())
graph = CityGraph(n, m, k)

print("Enter the road descriptions:")
for _ in range(m):
    xi, yi = map(int, input().split())
    graph.add_road(xi, yi)

forbidden_triplets = []
print("Enter the forbidden triplets:")
for _ in range(k):
    ai, bi, ci = map(int, input().split())
    forbidden_triplets.append((ai, bi, ci))

shortest_path_length, shortest_path = graph.find_shortest_path(forbidden_triplets)

if shortest_path_length == -1:
    print(-1)
else:
    print("Shortest path length:", shortest_path_length)
    print("Shortest path:", " ".join(str(city) for city in shortest_path))