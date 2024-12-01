def calculate_total_distance(file_path):
    left_list = []
    right_list = []

    # Read the input file and parse the data
    with open(file_path, 'r') as f:
        for line in f:
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)

    # Sort both lists
    left_list.sort()
    right_list.sort()

    # Calculate the total distance
    total_distance = sum(abs(l - r) for l, r in zip(left_list, right_list))

    return total_distance


# Example usage
file_path = 'input.input'
total_distance = calculate_total_distance(file_path)
print(f'Total distance: {total_distance}')
