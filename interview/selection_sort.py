def selection_sort(data: list[int]):
    n = len(data)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if data[j] < data[min_idx]:
                min_idx = j
        data[min_idx], data[i] = data[i], data[min_idx]
    return data

print(selection_sort([41, 34, 6, 16, 38, 36, 28, 19, 45, 43, 49]))
