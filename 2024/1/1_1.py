# day 1 : part 1 of aoc 2024

import io
import sys

def get_diffs(input):
    total_diffs = 0
    left_list = list()
    right_list = list()

    for i, line in enumerate(input):
        left, right = line.split("   ")
        left = int(left)
        right = int(right)

        left_list.append(left)
        right_list.append(right)

    left_list.sort()
    right_list.sort()

    for idx, j in enumerate(left_list):
        if (left_list[idx] >= right_list[idx]):
            total_diffs += left_list[idx] - right_list[idx]
        
        else:
            total_diffs += right_list[idx] - left_list[idx]

    return total_diffs

if __name__ == "__main__":
    f = open(sys.argv[1], "r", encoding="utf-8")
    print(get_diffs(f))


