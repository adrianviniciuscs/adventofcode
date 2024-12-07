import random
from graphviz import Digraph


def load_equations_from_file(filename):
    equations = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            target, numbers = line.split(':')
            target = int(target.strip())
            numbers = list(map(int, numbers.strip().split()))
            equations.append((target, numbers))
    return equations


def visualize_explore(nums, current_value, index, target, graph, parent_id):
    if index == len(nums):  # Base case: we've reached the end
        if current_value == target:
            graph.node(str(current_value), label=f'✔️ {
                       current_value}', shape='doublecircle', color='green')
        else:
            graph.node(str(current_value), label=f'{
                       current_value}', color='red')
        graph.edge(parent_id, str(current_value))
        return current_value == target

    current_id = f'{current_value}_{index}'
    graph.node(current_id, label=f'{current_value}')
    if parent_id:
        graph.edge(parent_id, current_id)

    next_num = nums[index]
    add_id = f'{current_value}+{next_num}'
    mult_id = f'{current_value}*{next_num}'
    concat_id = f'{current_value}||{next_num}'

    graph.node(add_id, label=f'{
               current_value} + {next_num} = {current_value + next_num}')
    graph.node(mult_id, label=f'{
               current_value} * {next_num} = {current_value * next_num}')
    graph.node(concat_id, label=f'{current_value} || {next_num} = {
               int(str(current_value) + str(next_num))}')

    graph.edge(current_id, add_id, label='+')
    graph.edge(current_id, mult_id, label='*')
    graph.edge(current_id, concat_id, label='||')

    add_path = visualize_explore(
        nums, current_value + next_num, index + 1, target, graph, add_id)
    mult_path = visualize_explore(
        nums, current_value * next_num, index + 1, target, graph, mult_id)
    concat_path = visualize_explore(nums, int(
        str(current_value) + str(next_num)), index + 1, target, graph, concat_id)

    return add_path or mult_path or concat_path


def visualize_equation(equation, filename='computation_tree'):
    target, nums = equation
    graph = Digraph(format='png')
    graph.attr(rankdir='TB')  # Top to bottom
    graph.node('start', label=f'Start ({
               nums[0]})', shape='ellipse', color='blue')

    visualize_explore(nums, nums[0], 1, target, graph, 'start')

    output_path = f'{filename}'
    graph.render(output_path, format='png', cleanup=True)
    print(f"Computation tree saved as {output_path}.png")


if __name__ == "__main__":
    filename = 'test.input'
    equations = load_equations_from_file(filename)

    equation_to_visualize = equations[random.randint(0, len(equations) - 1)]

    visualize_equation(equation_to_visualize, filename='computation_tree')
