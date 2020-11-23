# checks if a variable some_object is hashable

from collections.abc import Hashable

if isinstance(some_object, Hashable):
    print("Hashable")
else:
    print("Not hashable")


# calculates how many objects in the list object_list have the same hash value as some other element in the list

from collections.abc import Hashable

hashes = [hash(i) for i in object_list if isinstance(i, Hashable)]
print(len([i for i in hashes if hashes.count(i) > 1]))


# creates a dictionary of objects as keys and their hash values as values

from collections.abc import Hashable

objects = [1, 2, 3, 3, [3], (1, 2)]

objects_dict = {i: hash(i) for i in objects if isinstance(i, Hashable)}
