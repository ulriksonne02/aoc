# day 2 : part 2 of aoc 2024

import io
import sys

def dampened_safety_check(input):
    def single_check(report):
        increasing = 0
        decreasing = 0

        for c in range(1, len(report)):
            diff = report[c-1] - report[c]
            if (diff > 0) and (diff <= 3):
                increasing += 1
            if (diff < 0) and (diff >= -3):
                decreasing += 1
        
        if (len(report) - 1) == increasing or (len(report) - 1) == decreasing:
            return 1
        return 0
    def double_check(report):

        reports_to_check = list()
        
        success = 0

        for c in range(len(report)):
            reports_to_insert = report[:]
            reports_to_insert.pop(c)
            reports_to_check.append(reports_to_insert)
        print("reports to check: ", len(reports_to_check))
        for check in reports_to_check:
            success += single_check(check)
        print("succeses: ", success)
        if success > 0:
            return 1
        else:
            return 0

    
    safe_reports = 0
    primary = 0
    secondary = 0

    for i, report in enumerate(input):
        report = report.split(" ")
        report = [int(k) for k in report]

        
        increasing = 0
        decreasing = 0
        ret = 0

        
        if (single_check(report) == 1):
            safe_reports += 1
            primary += 1

        else:
            ret += double_check(report)
            print("double check", ret, report)
            print(" ")
            safe_reports += ret
            secondary += 1
    print("primary: ", primary)
    print("secondary: ", secondary)
    return safe_reports

if __name__ == "__main__":
    f = open(sys.argv[1], "r", encoding="utf-8")
    print(dampened_safety_check(f))
