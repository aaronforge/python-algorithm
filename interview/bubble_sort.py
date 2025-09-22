def bubble_sort(data: list[int]):
    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            if data[j + 1] < data[j]:
                data[j + 1], data[j] = data[j], data[j + 1]
    return data


print(bubble_sort([41, 34, 6, 16, 38, 36, 28, 19, 45, 43, 49]))
