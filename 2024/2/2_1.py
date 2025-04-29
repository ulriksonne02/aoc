# day 2 : part 1 of aoc 2024

import io
import sys

def safety_check(input):
    safe_reports = 0

    for i, report in enumerate(input):
        report = report.split(" ")
        report = [int(k) for k in report]
        print(report)
        adder = 1

        for j in range(1,len(report)-1):
    
            print(j, report[j])
            if report[j] == report[j-1]:
                adder = 0
                break
            elif report[j] > report[j-1]:
                if (report[j] - report[j-1]) > 2:
                    adder = 0
                    break
            
            elif report[j] < report[j-1]:
                if (report[j-1] - report[j]) > 2:
                    adder = 0
                    break
        print(adder)
        safe_reports += adder
    
    return safe_reports

if __name__ == "__main__":
    f = open(sys.argv[1], "r", encoding="utf-8")
    print(safety_check(f))
