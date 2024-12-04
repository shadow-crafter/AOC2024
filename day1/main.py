location_list = [[], []]

def process_input():
    with open("..\input.txt") as f:
        for line in f:
            split = line.strip().split("   ")
            location_list[0].append(int(split[0]))
            location_list[1].append(int(split[1]))
        location_list[0].sort()
        location_list[1].sort()

def find_distances(locations):
    distances = []
    for i in range(len(locations[0])):
        distances.append(abs(locations[0][i] - locations[1][i]))
    return distances

def find_frequency(locations):
    frequency_vals = []
    for i in range(len(locations[0])):
        frequency_vals.append(locations[1].count(locations[0][i]) * locations[0][i])
    return frequency_vals

def main():
    process_input()
    print(location_list)

    distances = find_distances(location_list)
    total_distance = sum(distances)
    print("Total of the distances: " + str(total_distance))

    frequencies = find_frequency(location_list)
    total_similarity = sum(frequencies)
    print("Total of similarity scores: " + str(total_similarity))

if __name__ == "__main__":
    main()
