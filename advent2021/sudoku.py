import math
from typing import List, Optional, Tuple
import pprint

def tryGrid(grid: List[List[int]]) -> bool:
  """
  From the given (current) grid, find the next empty space and try numbers in it, recursively.
  An "empty" space in the grid has an integer 0.  Otherwise, the space is not considered empty.

  :return: False if there was no solution from the given grid, or True if the grid is correctly filled.
    Otherwise, it will keep recursing deeper until the board is filled correctly.
    This function will only change the cells that it filled on its own, not any cells that were already given.
  """

  # loop over all open cells
  for x in range(9):
    for y in range(9):
      if grid[x][y] == 0:
        nums = getPossibleNumbers(grid, x, y)
        #print(f"For grid {x},{y}, valid {nums}")
        for i in nums:
          grid[x][y] = i
          #print(f"Trying [{x},{y}] = {i}")
          success = tryGrid(grid)
          if success:
            return success

        # if no number works in here, we're at a dead end grid state, return False
        grid[x][y] = 0

        return False
  return True


def getPossibleNumbers(grid: List[List[int]], x: int, y: int) -> List[int]:
  """
  :return: the possible numbers that could go into this cell, based on the current grid
  """
  allowed = [True] * 9  # these will be turned False as we find existing numbers in the grid

  # check along x-direction (row)
  for xi in range(9):
    val = grid[xi][y]
    if val != 0:
      allowed[val - 1] = False
      #print(f"saw {val} at x={xi}")

  # check along y-direction (col)
  for yi in range(9):
    val = grid[x][yi]
    if val != 0:
      allowed[val - 1] = False
      #print(f"saw {val} at y={yi}")

  # check in the current square (find top-left corner of the square first)
  square_x = int(math.floor(x / 3)) * 3
  square_y = int(math.floor(y / 3)) * 3
  #print(f"box top-left is {square_x} {square_y}")
  for xd in range(3):
    for yd in range(3):
      xi, yi = square_x + xd, square_y + yd
      val = grid[xi][yi]
      if val != 0:
        allowed[val - 1] = False
        #print(f"saw {val} at [{xi},{yi}]")

  return [i+1 for (i, tf) in enumerate(allowed) if tf]


if __name__ == "__main__":
#   grid = (
#   [
#     [0,0,0, 0,0,0, 0,0,0],
#     [0,0,7, 0,0,0, 0,0,0],
#     [0,4,0, 0,7,0, 8,6,0],
#
#     [0,0,0, 0,0,0, 0,0,0],
#     [0,0,0, 7,0,9, 0,3,0],
#     [0,3,4, 0,1,0, 5,0,0],
#
#     [0,8,0, 0,2,0, 0,5,0],
#     [0,7,0, 6,0,4, 3,9,0],
#     [0,0,0, 0,0,0, 0,0,0]
#   ])
#   grid = (
#   [
#     [0,0,7, 4,9,1, 6,0,5],
#     [2,0,0, 0,6,0, 3,0,9],
#     [0,0,0, 0,0,7, 0,1,0],
#
#     [0,5,8, 6,0,0, 0,0,4],
#     [0,0,3, 0,0,0, 0,9,0],
#     [0,0,6, 2,0,0, 1,8,7],
#
#     [9,0,4, 0,7,0, 0,0,2],
#     [6,7,0, 8,3,0, 0,0,0],
#     [8,1,0, 0,4,5, 0,0,0]
#   ])
  grid = (
  [
    [6,0,0, 0,0,9, 0,0,0],
    [0,0,0, 0,0,0, 0,0,4],
    [0,0,7, 6,4,8, 0,0,2],

    [0,0,2, 0,5,0, 8,0,0],
    [0,0,1, 8,0,0, 0,2,3],
    [7,0,4, 0,0,0, 0,0,0],

    [0,0,0, 3,0,0, 0,4,0],
    [0,0,0, 0,6,0, 5,0,0],
    [0,2,3, 0,1,0, 0,0,0]
  ])
  pprint.pprint(grid)

#   pprint.pprint(getPossibleNumbers(grid, 1, 1))
  success = tryGrid(grid)
  print(success)
  pprint.pprint(grid)



