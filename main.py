import pygame
from grid import Grid, Cell
from algorithms import BFS_algorithm, DFS_algorithm, DFS_algorithm, A_Star_algorithm, Greedy_Best_First_Search_algorithm


pygame.init()
screen = pygame.display.set_mode((1000, 1000))
running = True
cell_width_height = 1000//25
grid = Grid()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("dark grey")

    for cell in grid.cells:
        row, col = cell.position
        pygame.draw.rect(screen, color="white", rect=[row * cell_width_height, col * cell_width_height, cell_width_height, cell_width_height], width=1)


    pygame.display.flip()

pygame.quit()