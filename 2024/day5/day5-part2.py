
from collections import defaultdict, deque


def parse_input(input_text):
    sections = input_text.strip().split("\n\n")
    rules = [tuple(map(int, rule.split("|")))
             for rule in sections[0].splitlines()]
    updates = [list(map(int, update.split(",")))
               for update in sections[1].splitlines()]
    return rules, updates


def is_valid_update(update, rules):
    page_indices = {page: i for i, page in enumerate(update)}
    for x, y in rules:
        if x in page_indices and y in page_indices:
            if page_indices[x] > page_indices[y]:
                return False
    return True


def topological_sort(pages, rules):
    # Build a graph and compute in-degrees
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    for x, y in rules:
        if x in pages and y in pages:
            graph[x].append(y)
            in_degree[y] += 1
            if x not in in_degree:
                in_degree[x] = 0

    # Perform topological sorting
    queue = deque([node for node in pages if in_degree[node] == 0])
    sorted_pages = []
    while queue:
        current = queue.popleft()
        sorted_pages.append(current)
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return sorted_pages


def process_part_two(input_text):
    rules, updates = parse_input(input_text)
    invalid_updates = []
    for update in updates:
        relevant_rules = [(x, y)
                          for x, y in rules if x in update and y in update]
        if not is_valid_update(update, relevant_rules):
            invalid_updates.append((update, relevant_rules))

    total = 0
    for update, relevant_rules in invalid_updates:
        corrected_update = topological_sort(update, relevant_rules)
        total += corrected_update[len(corrected_update) // 2]
    return total


with open("input.input") as f:
    input_text = f.read()
# Process Part Two and get the result
result = process_part_two(input_text)
print("Sum of middle pages after correction:", result)
