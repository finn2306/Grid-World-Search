import pygame
from grid import Grid, Cell
from algorithms import BFS_algorithm, DFS_algorithm, Dijkstra_algorithm, A_Star_algorithm, Greedy_Best_First_Search_algorithm


pygame.init()
screen = pygame.display.set_mode((1300, 900))
running = True
cell_width_height = 900//25
grid = Grid(width_height=(25, 25), start_position=(1, 1), end_position=(23, 23))
explored_cells = []

generator = None
path = None

while running:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            generator = None
            explored_cells.clear()
            path = None
        if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
            explored_cells.clear()
            generator = BFS_algorithm(grid)
            path = None
        if event.type == pygame.KEYDOWN and event.key == pygame.K_2:
            explored_cells.clear()
            generator = DFS_algorithm(grid)
            path = None
        if event.type == pygame.KEYDOWN and event.key == pygame.K_3:
            explored_cells.clear()
            generator = Dijkstra_algorithm(grid)
            path = None
        if event.type == pygame.KEYDOWN and event.key == pygame.K_4:
            explored_cells.clear()
            generator = A_Star_algorithm(grid)
            path = None
        if event.type == pygame.KEYDOWN and event.key == pygame.K_5:
            explored_cells.clear()
            generator = Greedy_Best_First_Search_algorithm(grid)
            path = None
        if event.type == pygame.QUIT:
            running = False

    if generator is not None:
        try:
            explored_cells.append(next(generator))
        except StopIteration as e:
            path = e.value
            generator = None
            explored_cells.clear()

    screen.fill((74, 85, 104))

    for cell in grid.cells:
        row, col = cell.position
        if cell == grid.start_cell:
            pygame.draw.rect(screen, color="green",
                             rect=[row * cell_width_height, col * cell_width_height, cell_width_height,
                                   cell_width_height], width=0)
        elif cell == grid.end_cell:
            pygame.draw.rect(screen, color="red",
                             rect=[row * cell_width_height, col * cell_width_height, cell_width_height,
                                   cell_width_height], width=0)
        else:
            pygame.draw.rect(screen, color="black", rect=[row * cell_width_height, col * cell_width_height, cell_width_height, cell_width_height], width=1)

    for cell in explored_cells:
        row, col = cell.position
        if cell == grid.start_cell:
            pygame.draw.rect(screen, color="green",
                             rect=[row * cell_width_height, col * cell_width_height, cell_width_height,
                                   cell_width_height], width=0)
        elif cell == grid.end_cell:
            pygame.draw.rect(screen, color="red",
                             rect=[row * cell_width_height, col * cell_width_height, cell_width_height,
                                   cell_width_height], width=0)
        else:
            pygame.draw.rect(screen, color="yellow",
                         rect=[row * cell_width_height, col * cell_width_height, cell_width_height, cell_width_height],
                         width=0)
    if path is not None:
        for cell in path:
            row, col = cell.position
            if cell == grid.start_cell:
                pygame.draw.rect(screen, color="green",
                             rect=[row * cell_width_height, col * cell_width_height, cell_width_height,
                                   cell_width_height], width=0)
            elif cell == grid.end_cell:
                pygame.draw.rect(screen, color="red",
                             rect=[row * cell_width_height, col * cell_width_height, cell_width_height,
                                   cell_width_height], width=0)
            else:
                pygame.draw.rect(screen, color="purple",
                             rect=[row * cell_width_height, col * cell_width_height, cell_width_height,
                                   cell_width_height],
                             width=0)

    pygame.display.flip()

pygame.quit()