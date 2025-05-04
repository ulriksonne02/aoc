# day 2 : part 2 of aoc 2024

import io
import sys

def dampened_safety_check(input):
    def double_check(report, direction):
        skipped = 0

        direction = direction * -1

        print(report)
        for c in range(1,len(report)):

            #print((report[c] - report[c-1]))
            if ((report[c] - report[c-1]) * direction ) in range(1,4):
                print(report[c-1], ((report[c] - report[c-1]) * direction ) in range(1,4))
                continue


            elif (c+1 < len(report)):
                print("SKIP DIFF", report[c+1],report[c-1])
                if ((report[c+1] - report[c-1]) * direction) in range(1,4):
                    print("SUCCESS: A", (report[c+1] - report[c-1]))
                    return 1
            elif (c == len(report)-1):
                print("SUCCESS: LAST")
                return 1

            else:
                print("FAIL")
                return 0
        print("SUCCESS: END")
        return 1
    
    safe_reports = 0
    primary = 0

    for i, report in enumerate(input):
        report = report.split(" ")
        report = [int(k) for k in report]

        
        increasing = 0
        decreasing = 0

        for c in range(1, len(report)):
            diff = report[c-1] - report[c]
            if (diff > 0) and (diff <= 3):
                increasing += 1
            if (diff < 0) and (diff >= -3):
                decreasing += 1
        
        if (len(report) - 1) == increasing or (len(report) - 1) == decreasing:
            safe_reports += 1
            primary += 1

        elif(len(report) - 2) == increasing:
            safe_reports += double_check(report, 1)
        elif((len(report) - 2) == decreasing):
            safe_reports += double_check(report, -1)
    print(primary)
    return safe_reports

if __name__ == "__main__":
    f = open(sys.argv[1], "r", encoding="utf-8")
    print(dampened_safety_check(f))
