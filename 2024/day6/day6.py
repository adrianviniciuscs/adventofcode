from typing import List, Tuple, Dict
from copy import deepcopy
from tqdm import tqdm


def parse_input() -> Tuple[List[List[str]], Tuple[int, int]]:
    with open("input.input") as file:
        lines = [list(line.rstrip()) for line in file]
        for y, row in enumerate(lines):
            if "^" in row:
                x = row.index("^")
                return lines, (x, y)
    return lines, (None, None)  # Should not reach here in a valid input


def get_next_position(x: int, y: int, orientation: str) -> Tuple[int, int]:
    movements = {
        "NORTH": (x, y - 1),
        "SOUTH": (x, y + 1),
        "EAST": (x + 1, y),
        "WEST": (x - 1, y)
    }
    return movements[orientation]


def is_obstacle(x: int, y: int, matrix: List[List[str]]) -> bool:
    return matrix[y][x] in ("#", "O")


def is_out_of_bounds(x: int, y: int, matrix: List[List[str]]) -> bool:
    return not (0 <= x < len(matrix[0]) and 0 <= y < len(matrix))


def is_visited(x: int, y: int, matrix: List[List[str]]) -> bool:
    return matrix[y][x] == "X"


def visit(x: int, y: int, matrix: List[List[str]]) -> None:
    matrix[y][x] = "X"


def get_new_orientation(current_orientation: str) -> str:
    orientations = ["NORTH", "EAST", "SOUTH", "WEST"]
    return orientations[(orientations.index(current_orientation) + 1) % 4]


def count_visited(matrix: List[List[str]], coords: Tuple[int, int], orientation: str) -> int:
    visit(coords[0], coords[1], matrix)
    visited = 1

    x, y = get_next_position(coords[0], coords[1], orientation)

    while not is_out_of_bounds(x, y, matrix):
        possible_x, possible_y = get_next_position(x, y, orientation)
        if is_out_of_bounds(possible_x, possible_y, matrix):
            if not is_visited(x, y, matrix):
                visit(x, y, matrix)
                visited += 1
            break
        if is_obstacle(possible_x, possible_y, matrix):
            if not is_visited(x, y, matrix):
                visit(x, y, matrix)
                visited += 1
            while is_obstacle(possible_x, possible_y, matrix):
                orientation = get_new_orientation(orientation)
                x, y = get_next_position(x, y, orientation)
                possible_x, possible_y = x, y
        else:
            if not is_visited(x, y, matrix):
                visit(x, y, matrix)
                visited += 1
            x, y = get_next_position(x, y, orientation)
    return visited


def get_all_current_obstacles(matrix: List[List[str]]) -> List[Tuple[int, int]]:
    return [(i, j) for i, row in enumerate(matrix) for j, cell in enumerate(row) if cell == "#"]


def construct_obstacle_visited_cache(matrix: List[List[str]]) -> Dict[Tuple[int, int], Dict[str, int]]:
    return {pos: {"NORTH": 0, "SOUTH": 0, "EAST": 0, "WEST": 0} for pos in get_all_current_obstacles(matrix)}


def is_loop(matrix: List[List[str]], start_coords: Tuple[int, int], visited_obstacle_cache: Dict[Tuple[int, int], Dict[str, int]], orientation: str) -> bool:
    visit(start_coords[0], start_coords[1], matrix)
    x, y = get_next_position(start_coords[0], start_coords[1], orientation)

    while not is_out_of_bounds(x, y, matrix):
        possible_x, possible_y = get_next_position(x, y, orientation)
        if is_out_of_bounds(possible_x, possible_y, matrix):
            if not is_visited(x, y, matrix):
                visit(x, y, matrix)
            return False
        if is_obstacle(possible_x, possible_y, matrix):
            if not is_visited(x, y, matrix):
                visit(x, y, matrix)
            temp_x, temp_y = possible_x, possible_y
            orig_x, orig_y = x, y
            while is_obstacle(temp_x, temp_y, matrix):
                visited_obstacle_cache[(temp_y, temp_x)][orientation] += 1
                if any(count > 1 for count in visited_obstacle_cache[(temp_y, temp_x)].values()):
                    return True
                orientation = get_new_orientation(orientation)
                x, y = get_next_position(orig_x, orig_y, orientation)
                temp_x, temp_y = x, y
        else:
            if not is_visited(x, y, matrix):
                visit(x, y, matrix)
            x, y = get_next_position(x, y, orientation)
    return True


def is_valid_obstacle_position(x: int, y: int, matrix: List[List[str]]) -> bool:
    return matrix[y][x] not in ("#", "^")


def find_possible_loops(matrix: List[List[str]], coords: Tuple[int, int]) -> List[Tuple[int, int]]:
    visited_obstacle_cache = construct_obstacle_visited_cache(matrix)
    new_obstacle_positions = []
    for row in tqdm(range(len(matrix))):
        for column in range(len(matrix[row])):
            if is_valid_obstacle_position(column, row, matrix):
                current_matrix = deepcopy(matrix)
                current_obstacle_visited_cache = deepcopy(
                    visited_obstacle_cache)
                current_matrix[row][column] = "O"
                current_obstacle_visited_cache[(row, column)] = {
                    "NORTH": 0, "SOUTH": 0, "EAST": 0, "WEST": 0}
                if is_loop(current_matrix, coords, current_obstacle_visited_cache, "NORTH"):
                    new_obstacle_positions.append((row, column))
    return new_obstacle_positions


def print_matrix(matrix: List[List[str]]) -> None:
    for row in matrix:
        print("".join(row))


if __name__ == "__main__":
    matrix, start_coords = parse_input()
    matrix_for_part2 = deepcopy(matrix)

    result_part1 = count_visited(matrix, start_coords, "NORTH")
    print(f"Solution for part 1: {result_part1}")

    loops = find_possible_loops(matrix_for_part2, start_coords)
    print(f"Solution for part 2: {len(loops)}")
