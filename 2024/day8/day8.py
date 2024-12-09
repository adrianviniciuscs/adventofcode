from collections import defaultdict


def find_antennas(grid):
    antenna_positions = defaultdict(list)
    for row_index, row in enumerate(grid):
        for col_index, cell in enumerate(row):
            if cell != ".":
                antenna_positions[cell].append((row_index, col_index))
    return antenna_positions


def is_within_bounds(position, total_rows, total_cols):
    return 0 <= position[0] < total_rows and 0 <= position[1] < total_cols


def main():
    with open("input.input", "rt") as file:
        grid = [line.strip() for line in file]
        total_rows, total_cols = len(grid), len(grid[0])

    antennas = find_antennas(grid)
    part1_antinodes = set()
    part2_antinodes = set()

    for positions in antennas.values():
        if len(positions) == 1:
            continue

        for i in range(len(positions) - 1):
            pos1 = positions[i]
            for j in range(i + 1, len(positions)):
                pos2 = positions[j]
                row_diff, col_diff = pos2[0] - pos1[0], pos2[1] - pos1[1]

                part2_antinodes.add(pos1)
                part2_antinodes.add(pos2)

                antinode = (pos1[0] - row_diff, pos1[1] - col_diff)
                if is_within_bounds(antinode, total_rows, total_cols):
                    part1_antinodes.add(antinode)
                    while is_within_bounds(
                        antinode := (antinode[0] - row_diff, antinode[1] - col_diff),
                        total_rows,
                        total_cols,
                    ):
                        part2_antinodes.add(antinode)

                antinode = (pos2[0] + row_diff, pos2[1] + col_diff)
                if is_within_bounds(antinode, total_rows, total_cols):
                    part1_antinodes.add(antinode)
                    while is_within_bounds(
                        antinode := (antinode[0] + row_diff, antinode[1] + col_diff),
                        total_rows,
                        total_cols,
                    ):
                        part2_antinodes.add(antinode)

    print(f"Part 1: {len(part1_antinodes)}")
    print(f"Part 2: {len(part1_antinodes | part2_antinodes)}")


if __name__ == "__main__":
    main()
