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

    # prefer '1' as the most common char if there's a tie
    max_count = max_tuple[1]
    max_tuples = [item for item in counts.items() if item[1] == max_count]
    max_chars = [t[0] for t in max_tuples]
    if '1' in max_chars:
        return '1'
    # otherwise return arbitrary char
    return max_tuple[0]


def filter_by_bit_criteria(bit_strings: List[str], n_bits: int, keep_most_common: bool) -> str:
    for i in range(n_bits):
        most_common_bit = get_most_common_char(get_all_ith_chars(bit_strings, i))
        if keep_most_common:
            target_bit = most_common_bit
        else:
            target_bit = '1' if most_common_bit == '0' else '0'

        # filter bit strings: must have target_bit in position [i]
        bit_strings = [s for s in bit_strings if s[i] == target_bit]

        if len(bit_strings) == 1:
            return bit_strings[0]

        if len(bit_strings) == 0:
            return 'NO MORE STRINGS AFTER POSITION ' + str(i)


def bit_chars_to_int(bits: List[str]) -> int:
    return int("".join(bits), 2)


if __name__ == "__main__":
    with open("day3input.txt", "r") as f:
        raw_lines = f.readlines()
        # each line is a string of 0's and 1's followed by \n (except for the last line), so we have to strip the \n
        lines = [s.strip() for s in raw_lines]

        N_BITS = len(lines[0])

        # do the weird bit filtering rules they gave us
        o2_bits = filter_by_bit_criteria(lines, N_BITS, True)
        co2_bits = filter_by_bit_criteria(lines, N_BITS, False)

        print(o2_bits)
        print(co2_bits)

        o2_val = int(o2_bits, 2)
        co2_val = int(co2_bits, 2)
        print(f"o2:  {o2_val}")
        print(f"co2: {co2_val}")
        print(o2_val * co2_val)
