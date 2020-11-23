import copy


# function with deep copy or shallow copy mode
def my_copy(obj, copy_mode):
    return copy.deepcopy(obj) if copy_mode == "deep copy" else copy.copy(obj)


my_list = [[1], [2, 1]]
list_copy = copy.deepcopy(my_list)

# different id
print(id(my_list[0]), id(list_copy[0]))

# different id
print(id(my_list), id(list_copy))

# same id
print(id(my_list[0][0]), id(list_copy[1][1]))

# same id
print(id(my_list[1][0]), id(list_copy[1][0]))


lissst = [1, 2, 3]

# ids of lists differ, ids of its elements are same
my_copy = copy.copy(lissst)

# ids of lists are same, ids of its elements are same
my_copy = lissst

# ids of lists differ, ids of its elements are same
my_copy = lissst.copy()

# ids of lists differ, ids of its elements differ
my_copy = copy.deepcopy(lissst)

# ids of lists differ, ids of its elements are same
my_copy = [lissst[0], lissst[1], lissst[2]]


# put a list inside itself
empty_l = []
empty_l.append(empty_l)
print(empty_l)  # [[...]]
print(empty_l.copy())  # [[[...]]]
