def load_equations_from_file(filename):
    equations = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue  # Ignorar linhas em branco
            target, numbers = line.split(':')
            target = int(target.strip())
            numbers = list(map(int, numbers.strip().split()))
            equations.append((target, numbers))
    return equations


def explore(nums, current_value, index, target, memo):
    if index == len(nums):  # Caso base
        return current_value == target

    state = (current_value, index)
    if state in memo:  # Verificação de memoization
        return memo[state]

    next_num = nums[index]
    add_path = explore(nums, current_value + next_num, index + 1, target, memo)
    mult_path = explore(nums, current_value * next_num,
                        index + 1, target, memo)
    concat_path = explore(
        nums, int(str(current_value) + str(next_num)), index + 1, target, memo)

    result = add_path or mult_path or concat_path
    memo[state] = result
    return result


def calibrate_equations(equations):
    total = 0
    for target, nums in equations:
        memo = {}
        if explore(nums, nums[0], 1, target, memo):  # Começa com o primeiro número
            total += target  # Se a equação for válida, soma o target
    return total


if __name__ == "__main__":
    filename = 'input.input'

    equations = load_equations_from_file(filename)

    result = calibrate_equations(equations)

    print(f"Total da calibração: {result}")
