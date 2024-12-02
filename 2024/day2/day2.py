def is_increasing(arr):
    for i in range(len(arr) - 1):
        if arr[i] >= arr[i + 1] or not (1 <= abs(arr[i] - arr[i + 1]) <= 3):
            return False
    return True


def is_decreasing(arr):
    for i in range(len(arr) - 1):
        if arr[i] <= arr[i + 1] or not (1 <= abs(arr[i] - arr[i + 1]) <= 3):
            return False
    return True


with open('input') as f:
    lines = f.readlines()
    array = []

    safe = 0
    for line in lines:
        numbers = list(map(int, line.split()))
        array.append(numbers)

    for arr in array:
        print(arr)
        if is_increasing(arr) or is_decreasing(arr):
            print("Safe")
            safe += 1
        else:
            print("Unsafe")

    print(f"Safe reports: {safe}")
