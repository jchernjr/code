import itertools
import math
import re
from typing import List, Dict


SPLITTER_RE = re.compile(" +")


class BingoBoard:
    def __init__(self, rows: List[List[int]]):
        """Rows is assumed to be a 5-length list of 5-length lists of unique ints.
        We store it internally as a flat array for easier searching.
        Index 0-4 is row 1, 5-9 is row 2, 10-14 is row 3, etc."""
        self.numbers = list(itertools.chain(*rows))  # type: List[int]
        self.chosen = [False] * 25
        self.is_won = False

    def mark_chosen(self, number: int) -> None:
        """If board has this number, then mark it chosen."""
        if number in self.numbers:
            index = self.numbers.index(number)
            self.chosen[index] = True

            # Check the row and col that this number was part of, to see if we just won
            # (this is to avoid checking all 5 rows and all 5 cols every time)
            row = math.floor(index / 5)  # [0,4]
            col = index % 5  # [0,4]

            column_chosen = [self.chosen[r*5 + col] for r in range(5)]  # check along the column
            row_chosen = [self.chosen[row*5 + c] for c in range(5)]  # check along the row
            if all(column_chosen) or all(row_chosen):
                self.is_won = True

    @property
    def unmarked_numbers(self) -> List[int]:
        return [self.numbers[i] for i in range(len(self.numbers)) if not self.chosen[i]]

    @classmethod
    def from_string_lines(cls, lines: List[str]) -> 'BingoBoard':
        string_lists = [SPLITTER_RE.split(line.strip()) for line in lines]
        int_lists = [[int(s) for s in str_list] for str_list in string_lists]
        return BingoBoard(int_lists)


def part1(drawn_numbers: List[int], boards: List[BingoBoard]) -> None:
    for i, number in enumerate(drawn_numbers):
        for b in boards:
            b.mark_chosen(number)
            if b.is_won:
                unmarked = b.unmarked_numbers
                print(f"Round {i + 1}")
                print(f"Unmarked: {unmarked} (sum {sum(unmarked)})")
                print(f"Just called number {number}")
                print(sum(unmarked) * number)
                return


def part2(drawn_numbers: List[int], boards: List[BingoBoard]) -> None:
    winning_boards_in_order = []

    last_drawn_number = 0
    is_done = False
    for r, number in enumerate(drawn_numbers):
        for i, b in enumerate(boards):
            b.mark_chosen(number)
            if b.is_won and i not in winning_boards_in_order:
                print(f"Round {r + 1}, just called {number}, board {i} won.")
                winning_boards_in_order.append(i)

                print(f"Unmarked numbers in board 21: {boards[21].unmarked_numbers}")
                if len(winning_boards_in_order) == len(boards):
                    # Finished playing, stop drawing more numbers
                    is_done = True
                    break

        if is_done:
            last_drawn_number = number
            break

    last_won_index = winning_boards_in_order[-1]
    unmarked = boards[last_won_index].unmarked_numbers

    print(unmarked)
    print(last_drawn_number)
    print(last_drawn_number * sum(unmarked))


PART_1 = False


if __name__ == "__main__":
    with open("day4input.txt", "r") as f:
        raw_lines = f.readlines()

        # first line is list of numbers drawn for bingo
        drawn_numbers = [int(s) for s in raw_lines[0].strip().split(',')]

        # then starting from line 3, we have boards of 5-lines followed by a blank line
        # (line 3 is index 2)
        boards = [BingoBoard.from_string_lines(raw_lines[i:i+5]) for i in range(2, len(raw_lines), 6)]

        if PART_1:
            part1(drawn_numbers, boards)
        else:
            part2(drawn_numbers, boards)
