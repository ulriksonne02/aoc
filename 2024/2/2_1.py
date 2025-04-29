# day 2 : part 1 of aoc 2024

import io
import sys

def safety_check(input):
    safe_reports = 0

    def increasing(report):
        adder = 1

        for i in range(2,len(report)):
            if (report[i-2] >= report[i-1]) or (report[i-1] >= report[i]):
                #print("SAME/DECREASING")
                adder = 0
                break

            if ((report[i-1] - report[i-2]) > 3) or ((report[i] - report[i-1]) > 3):
                """
                print("TOO MUCH")
                print(report[i-1], "-", report[i-2], report[i-1] - report[i-2])
                print(report[i], "-", report[i-1], report[i] - report[i-1])
                """
                adder = 0
                break
        
        return adder

    def decreasing(report):
        adder = 1

        for i in range(2,len(report)):
            if (report[i-2] <= report[i-1]) or (report[i-1] <= report[i]):
                #print("SAME/INCREASING")
                adder = 0
                break

            if ((report[i-2] - report[i-1]) > 3) or ((report[i-1] - report[i]) > 3):
                """
                print("TOO MUCH")
                print(report[i-2], "-", report[i-1], report[i-2] - report[i-1])
                print(report[i-1], "-", report[i], report[i-1] - report[i])
                """
                adder = 0
                break

        return adder

    for i, report in enumerate(input):
        report = report.split(" ")
        report = [int(k) for k in report]

        adder = 1

        if report[0] < report[1]:
            adder = increasing(report)
        elif report[0] > report[1]:
            adder = decreasing(report)
        else:
            adder = 0

        safe_reports += adder
    
    return safe_reports

if __name__ == "__main__":
    f = open(sys.argv[1], "r", encoding="utf-8")
    print(safety_check(f))
