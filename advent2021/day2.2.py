if __name__ == "__main__":
    with open("day2input.txt", "r") as f:
        lines = f.readlines()
        commands = [s.split(" ") for s in lines]  # should be ('forward'|'up'|'down', number) list

        x_pos = 0  # horizontal (forward) distance
        depth = 0  # depth
        slope = 0  # number of depth units to gain/lose per horizontal distance traveled

        for direction, dist_str in commands:
            amt = int(dist_str)
            if direction == 'forward':
                x_pos += amt
                depth += slope * amt
            elif direction == 'up':  # tail up (nose down)
                slope -= amt
            elif direction == 'down':  # tail down (nose up)
                slope += amt
            else:
                print("unknown direction: " + str(direction))

        print(f"Horz: {x_pos}, Depth: {depth}")
        print(x_pos * depth)
