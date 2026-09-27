import pytest

import main


@pytest.mark.parametrize(
    "height,width,starting_point",
    [
        (2, 2, (0, 0)),
        (5, 5, (1, 1)),
        (10, 5, (1, 4)),
    ],
)
def test_initialise_grid(height, width, starting_point):
    sp_x, sp_y = starting_point
    grid = main.initialise_grid(height, width, starting_point)
    assert len(grid) == width
    assert len(grid[0]) == height
    assert grid[sp_x][sp_y] == "X"
    assert isinstance(grid[sp_x][sp_y + 1], int)
    assert isinstance(grid[sp_x + 1][sp_y], int)


@pytest.mark.parametrize(
    "coord,grid_height,grid_width,expected",
    [
        ((0, 0), 5, 5, True),
        ((4, 4), 5, 5, True),
        ((5, 5), 5, 5, False),
        ((10, 10), 5, 5, False),
        ((10, 1), 5, 5, False),
        ((1, 10), 5, 5, False),
    ],
)
def test_is_valid(coord, grid_height, grid_width, expected):
    assert main.is_valid(coord, grid_height, grid_width) == expected
