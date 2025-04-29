# day 1 : part 2 of aoc 2024

import io
import sys

def get_diffs(input):
    similarity_score = 0
    left_list = list()
    right_list = list()
    right_occurances = dict()

    for i, line in enumerate(input):
        left, right = line.split("   ")

        left = int(left)
        right = int(right)

        left_list.append(left)
        right_list.append(right)

        if right in right_occurances:
            right_occurances[right] += 1
        else:
            right_occurances.update({right:1})

    for i, num in enumerate(left_list):
        if num in right_occurances:
            similarity_score += num * right_occurances[num]

    return similarity_score

if __name__ == "__main__":
    f = open(sys.argv[1], "r", encoding="utf-8")
    print(get_diffs(f))


