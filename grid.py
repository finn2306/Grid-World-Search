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