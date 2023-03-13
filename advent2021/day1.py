if __name__ == "__main__":
    with open("day1input.txt", "r") as f:
        lines = f.readlines()
        values = [int(s) for s in lines]

        count = 0
        prev = values[0]
        for val in values[1:]:
            if val > prev:
                count += 1
            prev = val

        print(count)
