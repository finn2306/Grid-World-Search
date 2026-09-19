from grid import Grid, Cell

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
    queue = []
    came_from = {}

    queue.append(grid.start_cell)

    while queue:
        current_cell = queue.pop(0)
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
