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


def calculate_similarity_score(file_path):
    left_list = []
    right_list = []

    # Read the input file and parse the data
    with open(file_path, 'r') as f:
        for line in f:
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)

    # Count occurrences in the right list
    right_count = {}
    for item in right_list:
        if item in right_count:
            right_count[item] += 1
        else:
            right_count[item] = 1

    # Calculate the similarity score
    similarity_score = 0
    for item in left_list:
        if item in right_count:
            similarity_score += item * right_count[item]

    return similarity_score


file_path = 'input.input'
total_distance = calculate_total_distance(file_path)
similarity_score = calculate_similarity_score(file_path)
print(f'Total distance: {total_distance}')
print(f'Similarity score: {similarity_score}')
