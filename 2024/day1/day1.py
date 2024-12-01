# open the file
with open('input.input', 'r') as f:

    def distance(a, b):
        return b - a

    def take_min(array):
        return min(map(int, array))

    def make_pairs(left, right) -> list:
        pairs = []
        while left and right:
            min_left = take_min(left)
            min_right = take_min(right)
            pairs.append([min_left, min_right])
            left.remove(str(min_left))
            right.remove(str(min_right))
        return pairs

    left = []
    right = []

    for line in f:
        numbers = line.split()
        left.append(numbers[0])
        right.append(numbers[1])

    pairs = make_pairs(left, right)
    print(pairs)

    total_distance = sum(
        distance(abs(pair[0]), abs(pair[1])) for pair in pairs)
    print(total_distance)
