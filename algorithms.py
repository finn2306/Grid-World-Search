from grid import Grid, Cell
from collections import deque

def BFS_algorithm(grid):
    """Finds the shortest path from the grid's start cell to its end cell using
    Breadth-First Search.

    Explores the grid outward in rings of increasing distance from the start
    cell, guaranteeing that the first time the end cell is reached, it has
    been reached via the shortest possible path (fewest steps).

    Args:
        grid (Grid): The grid to search, providing the start cell, end cell,
            and walkable neighbor lookups.

    Returns:
        list: A list of Cell objects in order from the start cell to the end
            cell, representing the shortest path found.
    """
    visited = []
    queue = deque()
    came_from = {}

    queue.append(grid.start_cell)

    while queue:
        current_cell = queue.popleft()
        if current_cell == grid.end_cell:
            break
        else:
            neighbors = grid.get_walkable_neighbors(current_cell=current_cell)
            for neighbor in neighbors:
                if (neighbor not in queue) and (neighbor not in visited):
                    queue.append(neighbor)
                    came_from[neighbor] = current_cell

            visited.append(current_cell)

    path = [grid.end_cell]
    for cell in path:
        previous_cell = came_from[cell]
        path.append(previous_cell)
        if previous_cell == grid.start_cell:
            break

    return list(reversed(path))


def DFS_algorithm(grid):
    """Finds a path from the grid's start cell to its end cell using
    Depth-First Search.

    Explores the grid by diving as deep as possible down one path before
    backtracking to try alternatives. Unlike BFS, DFS does not guarantee
    that the first path found is the shortest one.

    Args:
        grid (Grid): The grid to search, providing the start cell, end cell,
            and walkable neighbor lookups.

    Returns:
        list: A list of Cell objects in order from the start cell to the end
            cell, representing the path found (not guaranteed to be shortest).
    """
    visited = []
    stack = deque()
    came_from = {}

    stack.append(grid.start_cell)

    while stack:
        current_cell = stack.pop()
        if current_cell == grid.end_cell:
            break
        else:
            neighbors = grid.get_walkable_neighbors(current_cell=current_cell)
            for neighbor in neighbors:
                if (neighbor not in stack) and (neighbor not in visited):
                    stack.append(neighbor)
                    came_from[neighbor] = current_cell

            visited.append(current_cell)

    path = [grid.end_cell]
    for cell in path:
        previous_cell = came_from[cell]
        path.append(previous_cell)
        if previous_cell == grid.start_cell:
            break

    return list(reversed(path))