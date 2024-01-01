# * Author:
# * Date:
from task1 import CityGraph
from task2 import MazeSolver
from task3 import transformation
from task4 import Genome
from task5 import TagGame
print("Task1")
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
print("Task2")
n, m, j = map(int, input(
    "Enter the number of rows, width of each row, and the number of times Jarmtin can avoid spikes: ").split())
maze = []
print("Enter the maze:")
for _ in range(n):
    row = input()
    maze.append(row)

maze_solver = MazeSolver(maze)

if maze_solver.solve_maze(j):
    print("SUCCESS")
else:
    print("IMPOSSIBLE")
print("Task3")
number = transformation()
x, y = map(int, input("Please enter the two numbers! For example: 2 162 \n").split(' '))
res1 = []
step1 = 0
number.transformation(x, y, res1, step1)
print("Task4")
obj=Genome()
obj.Genome(int(input("Please enter the number of genome fragments \n")),str(input("Please enter 1 descriptions of a fragment\n")))
print("Task4")
n, x = map(int, input().split())
game = TagGame(n, x)

for _ in range(n - 1):
    a, b = map(int, input().split())
    game.add_edge(a, b)

moves = game.calculate_moves()
print(moves)
