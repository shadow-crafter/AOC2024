reports = []

def process_input():
    with open("..\input.txt") as f:
            for line in f:
                reports.append([int(v) for v in line.strip().split()])

def find_safes():
    safe_count = 0
    for report in reports:
        if sorted(report) != report and sorted(report, reverse=True) != report:
            continue

        safe = True
        previous = report[0]
        for i, v in enumerate(report):
            if i == 0:
                continue
            change = abs(v - previous)
            if change > 3 or change <= 0:
                safe = False
                break
            previous = v
        
        if safe:
            safe_count += 1
        
    return safe_count

def main():
    process_input()
    print(reports)
    safe = find_safes()
    print("Safe reports: " + str(safe))

if __name__ == "__main__":
    main()