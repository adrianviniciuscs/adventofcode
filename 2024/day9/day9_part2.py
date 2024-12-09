def optimize_file_placement(input_file):
    # Read and parse the input file
    with open(input_file) as f:
        disk_code = [int(i) for i in "".join(line.strip() for line in f)]

    # Track file positions and free spaces
    file_positions, free_spaces = {}, []
    counter = 0

    # Populate file positions and free spaces
    for i, block_size in enumerate(disk_code):
        start, end = counter, counter + block_size
        if i % 2 == 0:
            file_positions[i // 2] = (start, end)
        elif block_size > 0:
            free_spaces.append((start, end))
        counter += block_size

    # Optimize file placement from highest to lowest file ID
    for file_id in sorted(file_positions.keys(), reverse=True):
        file_start, file_end = file_positions[file_id]
        file_length = file_end - file_start

        for i, (gap_start, gap_end) in enumerate(free_spaces):
            if gap_start >= file_start:
                break

            gap_length = gap_end - gap_start
            if file_length <= gap_length:
                free_spaces.pop(i)
                new_file_start = gap_start
                new_file_end = new_file_start + file_length
                file_positions[file_id] = (new_file_start, new_file_end)

                # Add remaining gap back if necessary
                if new_file_end < gap_end:
                    free_spaces.insert(i, (new_file_end, gap_end))
                break

    # Calculate final checksum
    return sum(file_id * pos
               for file_id, (start, end) in file_positions.items()
               for pos in range(start, end))


# Read input and print result
print(optimize_file_placement("input.input"))
