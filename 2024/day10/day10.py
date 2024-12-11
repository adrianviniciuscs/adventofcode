from collections import deque


def read_input(filename):
    with open(filename) as file:
        return [list(map(int, line.strip())) for line in file]


def build_graph(grid):
    rows, cols = len(grid), len(grid[0])
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    graph = {}
    starts = []

    for y in range(rows):
        for x in range(cols):
            node = (y, x)
            graph[node] = []
            if grid[y][x] == 0:
                starts.append(node)
            for dy, dx in directions:
                ny, nx = y + dy, x + dx
                if 0 <= ny < rows and 0 <= nx < cols and grid[ny][nx] == grid[y][x] + 1:
                    graph[node].append((ny, nx))

    return graph, starts


def count_trails(graph, start, trail_len):
    queue = deque([(start, 1)])
    unique_ends = set()
    total_ends = 0

    while queue:
        node, length = queue.popleft()
        if length == trail_len:
            unique_ends.add(node)
            total_ends += 1
        else:
            for neighbor in graph[node]:
                queue.append((neighbor, length + 1))

    return len(unique_ends), total_ends


def main():
    grid = read_input('input.input')
    graph, starts = build_graph(grid)
    trail_len = 10
    part1, part2 = 0, 0

    for start in starts:
        unique_ends, total_ends = count_trails(graph, start, trail_len)
        part1 += unique_ends
        part2 += total_ends

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")


if __name__ == "__main__":
    main()
