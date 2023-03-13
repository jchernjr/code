from typing import List, Dict


def get_all_ith_chars(strings: List[str], i: int) -> List[str]:
    """Get the ith char of all input strings, and return them as a list"""
    return [s[i] for s in strings]


def count_chars(chars: List[str]) -> Dict[str, int]:
    counts = {}
    for c in chars:
        if c not in counts:
            counts[c] = 0
        counts[c] += 1
    return counts


def get_most_common_char(chars: List[str]) -> str:
    counts = count_chars(chars)
    max_tuple = max(counts.items(), key=lambda item: item[1])  # 2nd part of tuple is the count
    return max_tuple[0]


def bit_chars_to_int(bits: List[str]) -> int:
    return int("".join(bits), 2)


if __name__ == "__main__":
    with open("day3input.txt", "r") as f:
        raw_lines = f.readlines()
        # each line is a string of 0's and 1's followed by \n (except for the last line), so we have to strip the \n
        lines = [s.strip() for s in raw_lines]

        N_BITS = len(lines[0])
        print(N_BITS)

        # figure out most common bit (0 or 1) in the 1st, 2nd, ..., Nth bit position
        most_common_bits = [get_most_common_char(get_all_ith_chars(lines, i)) for i in range(N_BITS)]
        least_common_bits = ['0' if c == '1' else '1' for c in most_common_bits]

        print(most_common_bits)
        print(least_common_bits)

        gamma_val = bit_chars_to_int(most_common_bits)
        eps_val = bit_chars_to_int(least_common_bits)

        print(f"gamma: {gamma_val}")
        print(f"eps: {eps_val}")
        print(gamma_val * eps_val)
