# if not sorted
def search(numbers, target):
    for i, e in enumerate(numbers):
        if e == target:
            return i
    return -1

# if sorted
def search(elements, target):
    index = -1
 
    for i, elem in enumerate(elements):
        if elem == target:
            index = i
            break
 
        if elem > target:
            break
 
    return index

# k-th occurrence
def kth(numbers, target, k):
    x = 0
    for i, n in enumerate(numbers):
        if n == target:
            x += 1
            if x == k:
                return i
    else:
        return -1


numbers = [int(i) for i in input().split()]
target = int(input())
k = int(input())
print(kth(numbers, target, k))

# Count occurrences
def count(numbers, target):
    x = 0
    for n in numbers:
        if n == target:
            x += 1
    return x


numbers = [int(i) for i in input().split()]
target = int(input())
print(count(numbers, target))

# first occurrence in sublist
def search(numbers, target, a, b):
    for i, n in enumerate(numbers[a:b]):
        if n == target:
            return i + a
    return -1


numbers = [int(i) for i in input().split()]
target = int(input())
a, b = (int(i) for i in input().split())
print(search(numbers, target, a, b))

# last occurrence
def search(numbers, target):
    last = -1
    for i, e in enumerate(numbers):
        if e == target:
            last = i
    return last

numbers = [int(i) for i in input().split()]
target = int(input())
print(search(numbers, target))
