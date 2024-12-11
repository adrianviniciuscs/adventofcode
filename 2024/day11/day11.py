from tqdm import tqdm


def load_input(file_name='input.input'):
    with open(file_name, 'r') as file:
        return [int(num) for num in file.read().split()]


def calculate_stones(stone, iterations, cache=None):
    if cache is None:
        cache = {}
    if (stone, iterations) in cache:
        return cache[(stone, iterations)]

    if iterations == 0:
        return 1
    if stone == 0:
        result = calculate_stones(1, iterations - 1, cache)
    else:
        stone_str = str(stone)
        length = len(stone_str)

        if length % 2 == 1:
            result = calculate_stones(stone * 2024, iterations - 1, cache)
        else:
            left_part = int(stone_str[:length // 2])
            right_part = int(stone_str[length // 2:])
            result = calculate_stones(
                left_part, iterations - 1, cache) + calculate_stones(right_part, iterations - 1, cache)

    cache[(stone, iterations)] = result
    return result


def solve_first_part(stones):
    return sum(calculate_stones(stone, 25) for stone in tqdm(stones, desc="First Part Progress"))


def solve_second_part(stones):
    return sum(calculate_stones(stone, 75) for stone in tqdm(stones, desc="Second Part Progress"))


if __name__ == "__main__":
    stones = load_input()
    print("First part result:", solve_first_part(stones))
    print("Second part result:", solve_second_part(stones))
