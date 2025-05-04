# day 3 : part 2 of aoc 2024

import io
import sys
import re


def sum_of_uncorrupted_part2(input):
    results = list()

    for line in input:
        #"[don't\(\).*do\(\)]"
        line =re.sub("don't[(][)].+do[(][)]","", line)
        print(line)
        temp_mul = re.findall("mul[(]\d+,\d+[)]", line)
        temp_split = [re.findall("\d+,\d+",i) for i in temp_mul]
        temp_split = [re.split("[,]",i[0]) for i in temp_split]
        [results.append([int(j) for j in i]) for i in temp_split]
        
    sum_of_products = 0
    for i in results:
        sum_of_products += i[0] * i[1]
    print(sum_of_products)

if __name__ == "__main__":
    f = open(sys.argv[1], "r", encoding="utf-8")
    print(sum_of_uncorrupted_part2(f))
