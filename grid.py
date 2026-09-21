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

    def __lt__(self, other):
        return self.position < other.position

class Grid:
    """Represents a grid of cells.
    Attributes:
        width_height (tuple): (w,h) representing the width and height of the grid.
        cells (tuple): A tuple of Cell objects.
        def get_walkable_neighbors: get walkable neighbors of current cell.
    """
    def __init__(self, width_height: tuple=(25, 25), start_position: tuple=(1, 1), end_position: tuple=(24, 24)):
        self.width_height = width_height
        self.cells = self.get_cells(width_height)
        self.start_position = start_position
        self.end_position = end_position
        self.start_cell = self.get_cell_at_position(start_position)
        self.end_cell = self.get_cell_at_position(end_position)


    def get_cells(self, width_height):
        """Returns a tuple of Cell objects."""
        cells = []
        width, height = width_height
        for w in range(0, width):
            for h in range(0, height):
                cell = Cell((w, h))
                cells.append(cell)

        return cells

    def get_walkable_neighbors(self, current_cell):
        """Returns a tuple of walkable neighbors of current cell."""
        w, h = current_cell.position
        positions = [(w+1, h), (w-1, h), (w, h-1), (w, h+1)]
        neighbor_cells = []
        for cell in self.cells:
            if cell.position in positions:
                neighbor_cells.append(cell)

        walkable_neighbors = [neighbor_cell for neighbor_cell in neighbor_cells if not neighbor_cell.is_wall]

        return walkable_neighbors


    def get_cell_at_position(self, position: tuple):
        """Returns a cell."""
        for cell in self.cells:
            if cell.position == position:
                break
        else:
            return None

        return cell





