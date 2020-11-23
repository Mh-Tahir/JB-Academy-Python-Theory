# iterative version of the binary search algorithm (ascending sorted list)

def binary_search(elements, target):
    left, right = 0, len(elements) - 1
 
    while left <= right:
        middle = (left + right) // 2
 
        if elements[middle] == target:
            return middle
        elif target < elements[middle]:
            right = middle - 1
        else:
            left = middle + 1
 
    return -1

# recursive implementation

def binary_search(elements, target, left, right):
    if left > right:
        return -1
 
    middle = (left + right) // 2
 
    if elements[middle] == target:
        return middle
    elif target < elements[middle]:
        return binary_search(elements, target, left, middle - 1)
    else:
        return binary_search(elements, target, middle + 1, right)

# Finding indexes of each element of one list in another one

def binary_search(elements, target):
    left, right = 0, len(elements) - 1

    while left <= right:
        middle = (left + right) // 2

        if elements[middle] == target:
            return middle
        if target < elements[middle]:
            right = middle - 1
        else:
            left = middle + 1

    return -1

x = [int(x) for x in input().split()]
y = [int(y) for y in input().split()]
for k in x:
    print(binary_search(y, k), end=' ')

# Descending sorted list

def binary_search(elements, target, left, right):
    if left > right:
        return -1
 
    middle = (left + right) // 2
 
    if elements[middle] == target:
        return middle
    if target < elements[middle]:
        return binary_search(elements, target, middle + 1, right)
    return binary_search(elements, target, left, middle - 1)

x = [int(x) for x in input().split()]
y = int(input())
print(binary_search(x, y, 0, len(x) - 1))

# Finding the left-most position of a target element in a descending-sorted list

def binary_search(elements, target, left, right):
    if left > right:
        return -1

    middle = (left + right) // 2

    if elements[middle] == target:
        if elements[middle - 1] == target:
            return binary_search(elements, target, left, middle - 1)
        return middle
    if target < elements[middle]:
        return binary_search(elements, target, middle + 1, right)
    return binary_search(elements, target, left, middle - 1)

x = [int(x) for x in input().split()]
y = int(input())
print(binary_search(x, y, 0, len(x) - 1))
