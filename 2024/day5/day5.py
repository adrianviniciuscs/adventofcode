
def parse_input(input_text):
    sections = input_text.strip().split("\n\n")
    rules = [tuple(map(int, rule.split("|")))
             for rule in sections[0].splitlines()]
    updates = [list(map(int, update.split(",")))
               for update in sections[1].splitlines()]
    return rules, updates


def is_valid_update(update, rules):
    # Create a mapping of page indices for validation
    page_indices = {page: i for i, page in enumerate(update)}
    for x, y in rules:
        if x in page_indices and y in page_indices:
            if page_indices[x] > page_indices[y]:
                return False
    return True


def find_middle_page(update):
    return update[len(update) // 2]


def process_updates(input_text):
    rules, updates = parse_input(input_text)
    total = 0
    for update in updates:
        # Filter rules to include only those relevant for this update
        relevant_rules = [(x, y)
                          for x, y in rules if x in update and y in update]
        if is_valid_update(update, relevant_rules):
            total += find_middle_page(update)
    return total


with open("input.input", "r") as file:
    input_text = file.read()
# Process the input and get the result
result = process_updates(input_text)
print("Sum of middle pages:", result)
