import re
from typing import List, DefaultDict, Tuple, NamedTuple


CoordPair = NamedTuple('CoordPair', [
    ('x1', int),
    ('y1', int),
    ('x2', int),
    ('y2', int),
])

LINE_PATTERN = re.compile(r"^(\d+),(\d+) -> (\d+),(\d+)")


def part1(coords: List[CoordPair], allow_diagonal: bool = False) -> None:
    dd = DefaultDict[Tuple[int, int], int](int)

    for c in coords:
        # figure out if it's a vertical or horizontal row
        if c.x1 == c.x2:  # column, same x value
            x = c.x1
            y1 = min(c.y1, c.y2)
            y2 = max(c.y1, c.y2)
            for y in range(y1, y2+1):
                dd[(x, y)] += 1

        elif c.y1 == c.y2:  # row, same y value
            y = c.y1
            x1 = min(c.x1, c.x2)
            x2 = max(c.x1, c.x2)
            for x in range(x1, x2+1):
                dd[(x, y)] += 1

        elif not allow_diagonal:
            print("Skipping rectangular / non-row coordinate pair: " + str(c))

        else:
            # assume diagonal
            x1, x2 = c.x1, c.x2
            y1, y2 = c.y1, c.y2
            span = abs(x2 - x1)
            x_dir = 1 if x2 > x1 else -1
            y_dir = 1 if y2 > y1 else -1
            print(f"({x1},{y1}) -> ({x2},{y2}): span: {span}, dx {x_dir}, dy {y_dir}")
            for i in range(span + 1):
                dd[(x1 + i*x_dir, y1 + i*y_dir)] += 1

    # Find where at least 2 rows/cols intersected a coord
    counts_over_2 = [v for v in dd.values() if v >= 2]
    print(len(counts_over_2))


PART_1 = False


if __name__ == "__main__":
    with open("day5input.txt", "r") as f:
        raw_lines = f.readlines()

        # parse each line into two xy coordinates
        matched_groups = [LINE_PATTERN.match(s).groups() for s in raw_lines]
        coords = [CoordPair(int(x1), int(y1), int(x2), int(y2)) for x1, y1, x2, y2 in matched_groups]

        if PART_1:
            part1(coords)
        else:
            part1(coords, allow_diagonal=True)
