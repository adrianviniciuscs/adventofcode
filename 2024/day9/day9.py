def parse_disk(disk_map):
    disk, file_id = [], 0
    for i in range(0, len(disk_map) - 1, 2):
        file_size, free_space_size = map(int, disk_map[i:i+2])
        if file_size > 0:
            disk.extend([file_id] * file_size)
            file_id += 1
        if free_space_size > 0:
            disk.extend([None] * free_space_size)

    # Handle last digit if odd-length input
    if len(disk_map) % 2 != 0:
        last_file_size = int(disk_map[-1])
        if last_file_size > 0:
            disk.extend([file_id] * last_file_size)

    return disk


def compact_disk(disk):
    disk_list = disk[:]
    free_positions = [i for i, x in enumerate(disk_list) if x is None]

    for i in range(len(disk_list) - 1, -1, -1):
        if disk_list[i] is not None and free_positions and free_positions[0] < i:
            free_index = free_positions.pop(0)
            disk_list[free_index] = disk_list[i]
            disk_list[i] = None
            free_positions.append(i)
            free_positions.sort()

    return disk_list


def calculate_checksum(disk):
    return sum(position * file_id
               for position, file_id in enumerate(disk)
               if file_id is not None)


def main():
    with open('input.input') as f:
        disk_map = f.readline().strip()

    disk = parse_disk(disk_map)
    compacted_disk = compact_disk(disk)
    print(calculate_checksum(compacted_disk))


if __name__ == "__main__":
    main()
