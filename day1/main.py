location_list = []

def process_input():
    with open("..\input.txt") as f:
        for line in f:
            location_list.append(line.strip().split("   "))

def main():
    process_input()
    print(location_list)

if __name__ == "__main__":
    main()
