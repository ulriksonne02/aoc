# day 2 : part 2 of aoc 2024

import io
import sys

def dampened_safety_check(input):
    def double_check(report, direction):
        skipped = 0
        for c, elm in enumerate(1, report):
            if (report[c] - report[c-1]) / abs(report[c] - report[c-1]) == direction:
                continue
            elif (c+1 <= len(report)):
                if (skipped == 0) and #STOPPET HER
                


    safe_reports = 0

    for i, report in enumerate(input):
        report = report.split(" ")
        report = [int(k) for k in report]

        
        increasing = 0
        decreasing = 0

        for c, elm in enumerate(1, report):
            diff = report[c-1] - report[c]
            if (diff > 0) and (diff <= 3):
                increasing += 1
            if (diff < 0) and (diff >= -3):
                decreasing += 1
        
        if (len(report) - 1) == increasing or (len(report) - 1) == decreasing:
            safe_reports += 1

        elif(len(report) - 2) == increasing:
        
        
    
    return safe_reports

if __name__ == "__main__":
    f = open(sys.argv[1], "r", encoding="utf-8")
    print(dampened_safety_check(f))
