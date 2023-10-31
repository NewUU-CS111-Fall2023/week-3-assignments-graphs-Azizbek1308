class MazeSolver:
    def __init__(self, maze):
        self.maze = maze
        self.num_rows = len(maze)
        self.num_cols = len(maze[0])
        self.start = None
        self.treasure = None

    def solve_maze(self, num_avoid_spikes):
        self.find_start_and_treasure()

        visited = [[False] * self.num_cols for _ in range(self.num_rows)]
        return self.dfs(self.start[0], self.start[1], num_avoid_spikes, visited)

    def dfs(self, row, col, num_avoid_spikes, visited):

        if (row, col) == self.treasure:
            return True

        if not self.is_valid_position(row, col) or visited[row][col]:
            return False

        visited[row][col] = True

        if self.maze[row][col] == 's':
            if num_avoid_spikes > 0:
                num_avoid_spikes -= 1
            else:
                return False

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if self.dfs(row + dr, col + dc, num_avoid_spikes, visited):
                return True

        return False

    def is_valid_position(self, row, col):
        return 0 <= row < self.num_rows and 0 <= col < self.num_cols and self.maze[row][col] != '#'

    def find_start_and_treasure(self):
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                if self.maze[i][j] == '@':
                    self.start = (i, j)
                elif self.maze[i][j] == 'x':
                    self.treasure = (i, j)

if __name__ == "__main__":
    print("hi")