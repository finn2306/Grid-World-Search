from grid import Grid, Cell
from algorithms import BFS_algorithm, DFS_algorithm, Dijkstra_algorithm, A_Star_algorithm, Greedy_Best_First_Search_algorithm

def test_cell_defaults():
    cell = Cell((0, 0))
    assert cell.position == (0, 0)
    assert cell.is_wall == False
    assert cell.weight == 1

def is_valid_path(grid, path):
    """..."""
    if path[0] != grid.start_cell or path[-1] != grid.end_cell:
        return False

    for i in range(len(path) - 1):
        current = path[i]
        next_cell = path[i + 1]
        if next_cell in (grid.get_walkable_neighbors(current)):
            continue
        else:
            return False

    return True

def test_bfs_finds_valid_path():
    grid = Grid((5, 5), start_position=(0, 0), end_position=(4, 4))
    path = BFS_algorithm(grid)
    assert is_valid_path(grid, path)

def test_dfs_finds_valid_path():
    grid = Grid((5, 5), start_position=(0, 0), end_position=(4, 4))
    path = DFS_algorithm(grid)
    assert is_valid_path(grid, path)

def test_dijkstra_finds_valid_path():
    grid = Grid((5, 5), start_position=(0, 0), end_position=(4, 4))
    path = Dijkstra_algorithm(grid)
    assert is_valid_path(grid, path)

def test_a_star_finds_valid_path():
    grid = Grid((5, 5), start_position=(0, 0), end_position=(4, 4))
    path = A_Star_algorithm(grid)
    assert is_valid_path(grid, path)

def test_greedy_bfs_finds_valid_path():
    grid = Grid((5, 5), start_position=(0, 0), end_position=(4, 4))
    path = Greedy_Best_First_Search_algorithm(grid)
    assert is_valid_path(grid, path)
