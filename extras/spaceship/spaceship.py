import curses
from time import sleep

CENTER = 0
HEIGHT = 0
WIDTH = 0
GOING_UP = True
STEP = 2
PLANET_1 = "Earth"
PLANET_2 = "Moon"


def draw_planets(stdscr, p1, p2):
    stdscr.addstr(p1, int(CENTER - len(PLANET_1) // 2), PLANET_1, curses.color_pair(2))
    stdscr.addstr(p2, int(CENTER - len(PLANET_2) // 2), PLANET_2, curses.color_pair(3))


def erase_spaceship(stdscr, offset):
    stdscr.addstr(offset, CENTER, " ", curses.color_pair(4))


def draw_spaceship(stdscr, offset):
    spaceship = "⮝" if GOING_UP else "⮟"
    stdscr.addstr(offset, CENTER, spaceship, curses.color_pair(4))


def main(stdscr):
    stdscr.clear()
    curses.curs_set(False)
    global CENTER, HEIGHT, WIDTH, GOING_UP
    HEIGHT, WIDTH = stdscr.getmaxyx()

    CENTER = int(WIDTH // 2)

    # start colours
    curses.start_color()
    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)  # info
    curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)  # planet 1
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)  # planet 2
    curses.init_pair(4, curses.COLOR_RED, curses.COLOR_BLACK)  # rocket

    # info
    dimensions = f"Width: {WIDTH}, Height: {HEIGHT}"
    stdscr.addstr(0, 0, dimensions, curses.color_pair(1))

    # planets
    p1 = HEIGHT - 5  # planet 1, bottom
    p2 = 5  # planet 2, top

    # spaceship start/end
    sp_start = p1 - 1  # starts at the bottom of the screen
    sp_end = p2 + 1  # end at the top of the screen
    sp_current = sp_start

    draw_planets(stdscr, p1, p2)
    draw_spaceship(stdscr, sp_start)
    stdscr.refresh()

    while True:
        erase_spaceship(stdscr, sp_current)

        if GOING_UP:
            sp_current = max(sp_end, sp_current - STEP)
            # check the next step
            if sp_current - STEP < sp_end:
                GOING_UP = False
        else:
            sp_current = min(sp_start, sp_current + STEP)
            # check the next step
            if sp_current + STEP > sp_start:
                GOING_UP = True

        draw_spaceship(stdscr, sp_current)
        stdscr.addstr(1, 0, f"Spaceship {sp_current:>4}", curses.color_pair(1))

        stdscr.refresh()
        sleep(0.5)


if __name__ == "__main__":
    curses.wrapper(main)
