import random

DIRECTIONS = [(0, -2), (2, 0), (0, 2), (-2, 0)]  # N, E, S, W

def create_empty_maze(width, height):
    maze = [['#'] * width for _ in range(height)]
    return maze

def is_valid(x, y, maze):
    return 0 < x < len(maze[0])-1 and 0 < y < len(maze)-1

def generate_maze(maze, x, y):
    maze[y][x] = ' '
    dirs = DIRECTIONS[:]
    random.shuffle(dirs)

    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if is_valid(nx, ny, maze) and maze[ny][nx] == '#':
            maze[y + dy // 2][x + dx // 2] = ' '  # remove wall
            generate_maze(maze, nx, ny)

