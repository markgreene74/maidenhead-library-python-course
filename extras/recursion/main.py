import curses
from random import randint
from time import sleep

N_STEPS = 15


def initialise_grid(
    height: int, width: int, starting_point: tuple[int, int]
) -> list[list[int | str]]:
    """initialise the grid with a random number in each cell and mark the starting point"""
    grid = [[randint(0, 9) for i in range(height)] for j in range(width)]
    x, y = starting_point
    grid[x][y] = "X"
    return grid


def display_grid(
    stdscr, grid: list[list[int | str]], grid_height: int, grid_width: int
) -> None:
    message = "test"
    stdscr.addstr(0, 0, message, curses.color_pair(1))

    for x in range(grid_width):
        for y in range(grid_height):
            # shift +1 when drawing the square on screen
            stdscr.addstr(y + 1, x + 1, str(grid[x][y]), curses.color_pair(2))

    stdscr.refresh()


def is_valid(coord: tuple[int, int], grid_height: int, grid_width: int) -> bool:
    x, y = coord
    if (0 <= x < grid_width) and (0 <= y < grid_height):  # noqa: SIM103
        return True
    return False


def next_move(coord: tuple[int, int], steps: int) -> tuple[int, int]:
    pass


def moves(coord: tuple[int, int], steps: int) -> list[tuple[int, int]]:
    results = []

    x, y = coord
    possible_moves = [
        (x - 1, y - 1),
        (x, y - 1),
        (x + 1, y - 1),
        (x - 1, y),
        (x, y),
        (x + 1, y),
        (x - 1, y + 1),
        (x, y + 1),
        (x + 1, y + 1),
    ]

    for new_coord in possible_moves:
        if not is_valid(new_coord):
            continue
        steps -= 1
        next = next_move(new_coord, steps)
        if next:
            results.append(new_coord)

    return results


def main(stdscr) -> None:
    height, width = stdscr.getmaxyx()
    grid_height = height - 2
    grid_width = width - 2
    starting_point = (randint(0, grid_width), randint(0, grid_height))

    # initialise the curses display
    stdscr.clear()
    curses.curs_set(False)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLUE)
    curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)  # alive
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_BLACK)  # dead
    stdscr.box()
    stdscr.refresh()

    # initialise and display the grid
    grid = initialise_grid(
        height=grid_height, width=grid_width, starting_point=starting_point
    )
    display_grid(stdscr, grid, grid_height, grid_width)

    sleep(5)


if __name__ == "__main__":
    curses.wrapper(main)
