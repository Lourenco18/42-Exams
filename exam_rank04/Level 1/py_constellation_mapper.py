"""
For this exercise, you must implement the `constellation_mapper` function. The function must:
- Take as a parameter a list of tuples, each consisting of an int(row) and an int(col).
- Return a list[str] representing a grid of size `size` * `size`, composed of "." and "*" characters based on the coordinates provided in the `stars` variable.
- Ignore coordinates that fall outside the grid boundaries.
- Ignore duplicate coordinates.
FUNCTION SIGNATURE
def constellation_mapper(stars: list[tuple[int, int]], size: int) -> list[str]:
EXAMPLES
constellation_mapper([(0, 0), (1, 1), (2, 2)], 3)->["*..", ".*.", "..*"]
constellation_mapper([(0, 0), (0, 1), (0, 2), (1, 1), (2, 2)], 3)->["***", ".*.", "..*"]
constellation_mapper([(0, 0), (5, 5), (2, 2)], 3)->["*..", "...", "..*"]
constellation_mapper([(0, 0), (5, 5)], 2)->["*.", ".."]
"""
def constellation_mapper(stars: list[tuple[int, int]], size: int) -> list[str]:
    grid = []
    i = 0
    """criar linha"""
    while i < size:
        grid.append(["."] * size)
        i += 1
    for row, col in stars:
        if 0 <= row < size and 0 <= col < size:
            grid[row][col] = "*"
    result = []
    for row in grid:
        result.append("".join(row))

    return result

print(constellation_mapper([(0, 0), (1, 1), (2, 2)], 3))
print(constellation_mapper([(0, 0), (0, 1), (0, 2), (1, 1), (2, 2)], 3))
print(constellation_mapper([(0, 0), (5, 5), (2, 2)], 3))
print(constellation_mapper([(0, 0), (5, 5)], 2))
print(constellation_mapper([(0, 0), (0, 0), (0, 0)], 2))