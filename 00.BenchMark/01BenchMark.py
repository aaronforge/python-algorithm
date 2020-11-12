from random import randint
import time

# SORT1 - CUSTOMIZED METHOD
array =  []
for _ in range(10000):
    array.append(randint(1, 100))

start_time = time.time()

for i in range(len(array)):
    min_index = i
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i] # SWAP ELEMENTS

end_time = time.time()

print(f'SORT1 - CUSTOMIZED METHOD TIME: {end_time - start_time}')
#: SORT1

# SORT2 - BASIC LIBRARY
array = []
for _ in range(10000):
    array.append(randint(1, 100))

start_time = time.time()

array.sort()

end_time = time.time()

print(f'SORT2 - BASIC LIBRARY TIME: {end_time - start_time}')
#: SORT2
