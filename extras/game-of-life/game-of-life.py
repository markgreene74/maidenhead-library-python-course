import curses
from time import sleep
from random import randint
from copy import deepcopy

HEIGHT = 0
WIDTH = 0
HEIGHT_GRID = 0
WIDTH_GRID = 0
GRID = []
ALIVE = 0
GENERATIONS = 25


def count_alive():
    """count the number of cells alive and update the global variable"""
    global ALIVE

    total = sum([sum(i) for i in GRID])
    ALIVE = total


def initialise_grid():
    """initialise the grid with a random number of alive cells (n>=1)"""
    global GRID

    # start with at least one cell alive
    h = randint(0, HEIGHT_GRID - 1)
    w = randint(0, WIDTH_GRID - 1)
    random_alive = [(h, w)]

    n_random_alive = randint(0, 500)
    for i in range(n_random_alive):
        while (h, w) in random_alive:
            h = randint(0, HEIGHT_GRID - 1)
            w = randint(0, WIDTH_GRID - 1)
        random_alive.append((h, w))

    for cell in random_alive:
        GRID[cell[0]][cell[1]] = 1

    count_alive()


def update_grid():
    """calculate the new state of the grid and update the global variable"""
    global GRID

    # make a copy of the current state
    new_state = deepcopy(GRID)

    # apply changes to the copy
    for w in range(WIDTH_GRID):
        for h in range(HEIGHT_GRID):
            cell = GRID[h][w]

            # find how many neighbours are alive
            # (-1,-1) (-1, 0) (-1, 1)
            # ( 0,-1)    x    ( 0, 1)
            # ( 1,-1) ( 1, 0) ( 1, 1)
            neighbours = [
                (-1, -1),
                (-1, 0),
                (-1, 1),
                (0, -1),
                (0, 1),
                (1, -1),
                (1, 0),
                (1, 1),
            ]
            alive_neighbours = 0
            for neighbour in neighbours:
                # check if we are in range
                neighbour_h = neighbour[0] + h
                neighbour_w = neighbour[1] + w
                if (0 < neighbour_h < HEIGHT_GRID) and (0 < neighbour_w < WIDTH_GRID):
                    alive_neighbours += GRID[neighbour_h][neighbour_w]

            # https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
            # alive and fewer than 2 live neighbours -> dies
            if cell and alive_neighbours < 2:
                new_state[h][w] = 0
            # alive and 2 or 3 live neighbours -> lives
            elif cell and alive_neighbours in [2, 3]:
                new_state[h][w] = 1
            # alive and more than 3 live neighbours -> dies
            elif cell and alive_neighbours < 2:
                new_state[h][w] = 0
            # dead with 3 alive neighbours -> becomes alive
            elif not cell and alive_neighbours == 3:
                new_state[h][w] = 1

    # and finally update the grid and update the counter
    GRID = new_state
    count_alive()


def update_output(stdscr, delay: float = 0, generation: int = 0):
    alive_str = f"Alive: {ALIVE:>5} ({WIDTH_GRID:>3}/{HEIGHT_GRID:>3}) - Generation: {generation:>3}"
    stdscr.addstr(0, 0, alive_str, curses.color_pair(1))

    for w in range(WIDTH_GRID):
        for h in range(HEIGHT_GRID):
            cell = "." if GRID[h][w] else " "
            # shift +1 when drawing the cell on screen
            stdscr.addstr(h + 1, w + 1, cell, curses.color_pair(2))

    stdscr.refresh()
    sleep(delay)


def main(stdscr):
    global HEIGHT, WIDTH, HEIGHT_GRID, WIDTH_GRID, GRID
    HEIGHT, WIDTH = stdscr.getmaxyx()
    HEIGHT_GRID = HEIGHT - 2
    WIDTH_GRID = WIDTH - 2
    GRID = [[0 for i in range(WIDTH_GRID)] for j in range(HEIGHT_GRID)]

    stdscr.clear()
    curses.curs_set(False)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLUE)
    curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)  # alive
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_BLACK)  # dead
    stdscr.box()
    stdscr.refresh()

    # initialise the grid
    initialise_grid()
    update_output(stdscr, delay=2.5)

    # start the update cycle
    for i in range(1, GENERATIONS + 1):
        update_grid()
        update_output(stdscr, delay=0.5, generation=i)


if __name__ == "__main__":
    curses.wrapper(main)
