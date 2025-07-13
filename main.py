from maze_generator import create_empty_maze, generate_maze
from maze_solver import bfs_solve
from maze_drawer import draw_maze_with_path
from custom_maze import custom_maze, start, goal

def print_maze(maze):
    for row in maze:
        print(''.join(row))

def main():
    WIDTH, HEIGHT = 21, 21  # Must be odd for maze structure

    # Option 1: Generate random maze
    maze = create_empty_maze(WIDTH, HEIGHT)
    generate_maze(maze, 1, 1)
    
    # Option 2: Use custom maze (uncomment to use)
    # maze = custom_maze

    print_maze(maze)

    path = bfs_solve(maze, start, goal)
    draw_maze_with_path(maze, path)

if __name__ == "__main__":
    main()
