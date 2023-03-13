"""
Player 1 starting position: 7
Player 2 starting position: 10
"""


class Dice:
    def __init__(self):
        self.next_val = 1
        self.max_val = 100

        self.num_rolls = 0

    def roll_3(self) -> int:
        vals = []
        for i in range(3):
            vals.append(self.next_val)
            self.next_val += 1
            if self.next_val > self.max_val:
                self.next_val = 1
        self.num_rolls += 3
        return sum(vals)


class Player:
    def __init__(self, player_name: str, initial_space: int):
        self.name = player_name
        self.position = initial_space
        self.max_position = 10

        self.score = 0

    def move(self, num_spaces: int) -> None:
        tentative_pos = self.position + num_spaces
        # wrap around to [1, 10 (max_pos)]
        if tentative_pos <= self.max_position:
            new_pos = tentative_pos
        else:
            # landing on 20, 30, 40, etc should wrap down to spot "10".
            # landing on non-zero last digit should wrap down to that digit.
            remainder = tentative_pos % self.max_position
            new_pos = self.max_position if remainder == 0 else remainder

        print(f"Player {self.name} from space {self.position} moving {num_spaces} to {new_pos}.")

        self.position = new_pos
        self.score += new_pos


if __name__ == "__main__":
    d = Dice()

    p1 = Player("1", 7)
    p2 = Player("2", 10)

    while True:
        p1.move(d.roll_3())
        if p1.score >= 1000:
            print(f"Player 1 won")
            break

        p2.move(d.roll_3())
        if p2.score >= 1000:
            print(f"Player 2 won.")
            break

    print(f"Player 1 {p1.score} pts.  Player 2 {p2.score} pts.")
    print(f"Dice rolled {d.num_rolls} times.")
