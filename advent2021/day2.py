if __name__ == "__main__":
    with open("day2input.txt", "r") as f:
        lines = f.readlines()
        commands = [s.split(" ") for s in lines]  # should be ('forward'|'up'|'down', number) list

        x_pos = 0  # horizontal (forward) distance
        depth = 0  # depth

        for direction, dist_str in commands:
            dist = int(dist_str)
            if direction == 'forward':
                x_pos += dist
            elif direction == 'up':
                depth -= dist
            elif direction == 'down':
                depth += dist
            else:
                print("unknown direction: " + str(direction))

        print(f"Horz: {x_pos}, Depth: {depth}")
        print(x_pos * depth)
