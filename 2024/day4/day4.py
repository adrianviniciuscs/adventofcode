# Read input data from file and store each line in a list
input_lines = []
with open("input.input", "r") as file:
    input_lines = [line.strip() for line in file]

# Initialize sets to store coordinates of different characters
x_coords = set()
m_coords = set()
a_coords = set()
s_coords = set()

# Populate sets with coordinates based on character type
for y, line in enumerate(input_lines):
    for x, char in enumerate(line):
        coord = (x, y)
        if char == "X":
            x_coords.add(coord)
        elif char == "M":
            m_coords.add(coord)
        elif char == "A":
            a_coords.add(coord)
        elif char == "S":
            s_coords.add(coord)

# Define possible directions for checking adjacent coordinates
directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
              (0, 1), (1, -1), (1, 0), (1, 1)]

# Calculate Part 1 answer
part1_answer = sum(
    1 for x, y in x_coords
    for dx, dy in directions
    if (x + dx, y + dy) in m_coords and (x + 2 * dx, y + 2 * dy) in a_coords and (x + 3 * dx, y + 3 * dy) in s_coords
)

# Calculate Part 2 answer
part2_answer = 0
for x, y in a_coords:
    top_left, top_right, bottom_left, bottom_right = (
        x - 1, y - 1), (x + 1, y - 1), (x - 1, y + 1), (x + 1, y + 1)
    for _ in range(4):
        if top_left in m_coords and top_right in m_coords and bottom_left in s_coords and bottom_right in s_coords:
            part2_answer += 1
            break
        top_left, top_right, bottom_right, bottom_left = top_right, bottom_right, bottom_left, top_left

# Print the results
print(f"{part1_answer=}")
print(f"{part2_answer=}")
