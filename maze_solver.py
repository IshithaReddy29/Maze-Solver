from collections import deque

# BFS algorithm
def bfs(maze, start, goal):
    rows, cols = len(maze), len(maze[0])
    queue = deque([start])
    visited = {start}
    parent = {}

    while queue:
        r, c = queue.popleft()

        if (r, c) == goal:
            # Reconstruct path
            path = []
            while (r, c) != start:
                path.append((r, c))
                r, c = parent[(r, c)]
            path.append(start)
            return path[::-1]  # reverse

        # possible moves: up, down, left, right
        for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == 0:
                if (nr, nc) not in visited:
                    visited.add((nr, nc))
                    parent[(nr, nc)] = (r, c)
                    queue.append((nr, nc))
    return None

# ---------------- MAIN ----------------
rows = int(input("Enter number of rows in maze: "))
cols = int(input("Enter number of columns in maze: "))

print("Enter the maze row by row (0 for free, 1 for wall):")
maze = []
for i in range(rows):
    row = list(map(int, input().split()))
    maze.append(row)

start = tuple(map(int, input("Enter start position (row col): ").split()))
goal = tuple(map(int, input("Enter goal position (row col): ").split()))

path = bfs(maze, start, goal)

if path:
    print("Path found:", path)
else:
    print("No path exists!")
