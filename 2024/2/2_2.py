# day 2 : part 2 of aoc 2024

import io
import sys

def dampened_safety_check(input):
    def increasing(report, adder):
        if(adder <= 0):
            return 0
        print(report)
        for i in range(2,len(report)):
            if (report[i-2] == report[i-1]): #check if i-2 and i-1 are the same
                print("I2==1")
                report.pop(i-2)
                return increasing(report, adder-1)
            
            if (report[i-1] == report[i]): #check if i-1 and i are the same
                print("I1==0")
                report.pop(i-1)
                return increasing(report, adder-1)
            
            if ((report[i-2] < report[i-1]) is False):
                print("IA")
                report.pop(i-2)
                return increasing(report, adder-1)
            
            if ((report[i-1] < report[i]) is False):
                print("IB")
                report.pop(i-1)
                return increasing(report, adder-1)

            if ((report[i-1] - report[i-2]) > 3):
                print("IC")
                report.pop(i-1)
                return increasing(report, adder-1)
            
            if ((report[i] - report[i-1]) > 3):
                print("ID")
                report.pop(i)
                return increasing(report, adder-1)

        return 1

    def decreasing(report, adder):
        if(adder <= 0):
            return 0
        print(report)
        for i in range(2,len(report)):
            if (report[i-2] == report[i-1]): #check if i-2 and i-1 are the same
                print("D2==1")
                report.pop(i-2)
                return decreasing(report, adder-1)
            
            if (report[i-1] == report[i]): #check if i-1 and i are the same
                print("D1==0")
                report.pop(i-1)
                return decreasing(report, adder-1)
                        
            if ((report[i-2] > report[i-1]) is False):
                print("DA")
                report.pop(i-1)
                return decreasing(report, adder-1)
            
            if ((report[i-1] > report[i]) is False):
                print("DB")
                report.pop(i)
                return decreasing(report, adder-1)

            if ((report[i-2] - report[i-1]) > 3):
                print("DC")
                report.pop(i-1)
                return decreasing(report, adder-1)

            if ((report[i-1] - report[i]) > 3):
                print("DD")
                report.pop(i)
                return decreasing(report, adder-1)

        return 1
    
    safe_reports = 0

    for i, report in enumerate(input):
        report = report.split(" ")
        report = [int(k) for k in report]

        adder = 0


        #adder += increasing(report, 2)
        #adder += decreasing(report, 2)
        
        if report[0] <= report[-1]:
            adder = increasing(report, 2)
            #print(adder)
        elif report[0] >= report[-1]:
            adder = decreasing(report, 2)
            #print(adder)
        else:
            print("edge case")
            adder = 0
        

        #print(report)
        #adder = decreasing(report, 2) + increasing(report, 2)
        #print("out", decreasing(report, 2), increasing(report, 2))


        safe_reports += adder
    
    return safe_reports

if __name__ == "__main__":
    f = open(sys.argv[1], "r", encoding="utf-8")
    print(dampened_safety_check(f))
