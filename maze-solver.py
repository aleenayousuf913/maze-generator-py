from collections import deque

def is_valid(x, y, maze):
    return 0 <= x < len(maze[0]) and 0 <= y < len(maze)

def bfs_solve(maze, start, goal):
    queue = deque([start])
    visited = {start: None}

    while queue:
        x, y = queue.popleft()
        if (x, y) == goal:
            break
        for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny, maze) and maze[ny][nx] == ' ' and (nx, ny) not in visited:
                queue.append((nx, ny))
                visited[(nx, ny)] = (x, y)

    # reconstruct path
    path = []
    curr = goal
    while curr and curr in visited:
        path.append(curr)
        curr = visited[curr]
    path.reverse()
    return path
