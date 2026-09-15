class Cell:
    """Represents a single cell in the grid.

    Attributes:
        position (tuple): (row, col) coordinates of the cell.
        is_wall (bool): Whether the cell blocks movement. Defaults to False.
        weight (int): Cost to move through the cell (1-5). Defaults to 1.
    """

    def __init__(self, position: tuple, is_wall: bool = False, weight: int = 1):
        self.position = position
        self.is_wall = is_wall
        self.weight = weight

class Grid:
    """Represents a grid of cells.
    Attributes:
        width_height (tuple): (w,h) representing the width and height of the grid.
        cells (tuple): A tuple of Cell objects.
        def get_walkable_neighbors: get walkable neighbors of current cell.
    """
    def __init__(self, width_height: tuple=(25, 25)):
        self.width_height = width_height
        self.cells = self.get_cells(width_height)


    def get_cells(self, width_height):
        """Returns a tuple of Cell objects."""
        cells = []
        width, height = width_height
        for w in range(0, width):
            for h in range(0, height):
                cell = Cell((w, h))
                cells.append(cell)

        cells_as_tuple = tuple(cells)

        return cells_as_tuple