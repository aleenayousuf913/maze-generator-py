import matplotlib.pyplot as plt

def draw_maze_with_path(maze, path):
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == '#':
                ax.add_patch(plt.Rectangle((x, len(maze)-y-1), 1, 1, color='black'))
            else:
                ax.add_patch(plt.Rectangle((x, len(maze)-y-1), 1, 1, color='white'))
    # draw path
    for x, y in path:
        ax.add_patch(plt.Circle((x + 0.5, len(maze) - y - 0.5), 0.2, color='red'))

    plt.axis('off')
    plt.show()
