from grid import Grid, Cell
from collections import deque
import heapq

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
        yield current_cell
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

def Dijkstra_algorithm(grid):
    """Finds the cheapest path from the grid's start cell to its end cell
    using Dijkstra's algorithm.

    Explores the grid using a priority queue, always processing the
    cell with the lowest known total cost so far. Unlike BFS, this
    accounts for each cell's weight, guaranteeing that the first time
    the end cell is reached, it has been reached via the cheapest
    possible path (lowest total cost), even if that path takes more
    steps than a shorter, more expensive alternative.

    Args:
        grid (Grid): The grid to search, providing the start cell, end cell,
            and walkable neighbor lookups.

    Returns:
        list: A list of Cell objects in order from the start cell to the end
            cell, representing the cheapest path found.
    """

    costs = {}
    heap = []

    came_from = {}

    costs[grid.start_cell] = grid.start_cell.weight

    heapq.heappush(heap,(costs[grid.start_cell],grid.start_cell))

    while heap:
        cost, current_cell = heapq.heappop(heap)

        if current_cell == grid.end_cell:
            break
        elif cost > costs[current_cell]:
            continue
        else:
            neighbors = grid.get_walkable_neighbors(current_cell=current_cell)
            for neighbor in neighbors:
                new_cost = costs[current_cell] + neighbor.weight
                if neighbor not in costs or new_cost < costs[neighbor]:
                    costs[neighbor] = new_cost
                    came_from[neighbor] = current_cell
                    heapq.heappush(heap, (costs[neighbor], neighbor))

    path = [grid.end_cell]
    for cell in path:
        previous_cell = came_from[cell]
        path.append(previous_cell)
        if previous_cell == grid.start_cell:
            break

    return list(reversed(path))

def A_Star_algorithm(grid):
    """Finds the cheapest path from the grid's start cell to its end cell
    using the A* algorithm.

    Like Dijkstra, explores the grid using a priority queue ordered by
    accumulated cost, but also factors in a heuristic estimate (Manhattan
    distance) of each cell's remaining distance to the goal. This biases
    exploration toward the goal, typically visiting far fewer cells than
    Dijkstra while still guaranteeing the same cheapest possible path.

    Args:
        grid (Grid): The grid to search, providing the start cell, end cell,
            and walkable neighbor lookups.

    Returns:
        list: A list of Cell objects in order from the start cell to the end
            cell, representing the cheapest path found.
    """

    costs = {}
    heap = []

    came_from = {}

    costs[grid.start_cell] = grid.start_cell.weight

    heapq.heappush(heap,(costs[grid.start_cell],grid.start_cell))
    w_end_cell, h_end_cell = grid.end_cell.position


    while heap:
        cost, current_cell = heapq.heappop(heap)
        w, h = current_cell.position
        heuristic = abs((w_end_cell - w)) + abs((h_end_cell - h))
        if current_cell == grid.end_cell:
            break
        elif (cost - heuristic) > costs[current_cell]:
            continue
        else:
            neighbors = grid.get_walkable_neighbors(current_cell=current_cell)
            for neighbor in neighbors:
                neighbor_w, neighbor_h = neighbor.position
                neighbor_heuristic = abs(w_end_cell - neighbor_w) + abs(h_end_cell - neighbor_h)
                new_cost = costs[current_cell] + neighbor.weight
                if neighbor not in costs or new_cost < costs[neighbor]:
                    costs[neighbor] = new_cost
                    came_from[neighbor] = current_cell
                    heapq.heappush(heap, (new_cost + neighbor_heuristic, neighbor))

    path = [grid.end_cell]
    for cell in path:
        previous_cell = came_from[cell]
        path.append(previous_cell)
        if previous_cell == grid.start_cell:
            break

    return list(reversed(path))

def Greedy_Best_First_Search_algorithm(grid):
    """Finds a path from the grid's start cell to its end cell using
    Greedy Best-First Search.

    Explores the grid using a priority queue ordered purely by a heuristic
    estimate (Manhattan distance) to the goal, completely ignoring the real
    accumulated cost of getting there. This tends to move quickly toward the
    goal, but unlike Dijkstra and A*, offers no guarantee of finding the
    cheapest path, since it can be lured into expensive routes that merely
    look close to the goal.

    Args:
        grid (Grid): The grid to search, providing the start cell, end cell,
            and walkable neighbor lookups.

    Returns:
        list: A list of Cell objects in order from the start cell to the end
            cell, representing the path found (not guaranteed to be cheapest).
    """

    visited = [grid.start_cell]
    heap = []

    came_from = {}

    w_end_cell, h_end_cell = grid.end_cell.position
    w_start_cell, h_start_cell = grid.start_cell.position
    start_heuristic = abs(w_end_cell - w_start_cell) + abs(h_end_cell - h_start_cell)
    heapq.heappush(heap, (start_heuristic, grid.start_cell))

    while heap:
        heuristic, current_cell = heapq.heappop(heap)

        if current_cell == grid.end_cell:
            break
        else:
            neighbors = grid.get_walkable_neighbors(current_cell=current_cell)
            for neighbor in neighbors:
                neighbor_w, neighbor_h = neighbor.position
                neighbor_heuristic = abs(w_end_cell - neighbor_w) + abs(h_end_cell - neighbor_h)
                if (neighbor not in visited) and (neighbor not in heap) :
                    came_from[neighbor] = current_cell
                    heapq.heappush(heap, (neighbor_heuristic, neighbor))
            visited.append(current_cell)

    path = [grid.end_cell]
    for cell in path:
        previous_cell = came_from[cell]
        path.append(previous_cell)
        if previous_cell == grid.start_cell:
            break

    return list(reversed(path))
