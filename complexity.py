from grid import Grid, Cell
from algorithms import BFS_algorithm

grid = Grid()

generator = BFS_algorithm(grid)
while True:
    try:
        cell = next(generator)
        print(cell.position)
    except StopIteration as e:
        print(f"final path: {e.value}")
        break
