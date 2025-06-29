# Dictionaries
band = {
    "vocals": "plant",
    "guitar": "page"
}

band2 = dict(vocals="plant", guitar="page")

print(band)
print(band2)
print(len(band))
print(type(band))

print()

# Access items
print(band["vocals"])
print(band.get("guitar"))

print()

# list al keys
print(band.keys())

print()

# list all values
print(band.values())

print()

# list of items
# key/value pairs as tuples
print(band.items())

print()

# verify if key exists
print("guitar" in band)
print("triangle" in band)

print()

# Change value
band["guitar"] = "coverdale"
band.update({"bass": "JPJ"})

print(band)

print()

# Remove items
print(band.pop("bass"))
print(band)

band["drums"] = "Bonham"
print(band)

print(band.popitem()) # tuple
print(band)

print()

# Delete and clear

band["drums"] = "Bonham"
del band["drums"]
print(band)

band2.clear()
print(band2)

del band2

print()

# # Copy dict

# band2 = band #! dict is a pointer
# print('Bad copy!')
# print(band2)
# print(band)

# band2["drums"] = "Dave"
# print(band)

band2 = band.copy()
band2["drums"] = "Dave"
print('Good copy')
print(band)
print(band2)

print()

# or use dict() constructor
band3 = dict(band)
print('Good copy')
print(band3)

print()

# Nested dictionaries
member1 = {
    "name": "Elvis",
    "instrument": "piano",
}
member2 = {
    "name": "page",
    "instrument": "guitar",
}
band = {
    "member1": member1,
    "member2": member2
}

print(band)
print(band["member1"]["name"])


band = {
    "member1":  {
        "name": "Elvis",
        "instrument": "piano",
    },
    "member2":  {
        "name": "page",
        "instrument": "guitar",
    }
}
print(band)

print()

# Set

numbers = {1, 2, 3, 4}

numbers2 = set((1, 2, 3, 4))

print(numbers)
print(numbers2)

print(type(numbers))
print(len(numbers))

numbers = {1, 2, 2, 3}
print(numbers)

print()

# True is a dupe of 1... 999, False is a dupe of zero
numbers = {1, True, 2, False, 3, 4, 0}
print(numbers)

print()

# check if a value is in a set
print(2 in numbers)

# but you cannot refer to an element in the set with an index position or a key

# Add a new element to a set 
numbers.add(8)
print(numbers)

# Add elements from one set to another
morenumbers = {5, 6, 7}
numbers.update(morenumbers)
print(numbers)

# you can use update with lists, tuples and dicts too.

# Merge two set to create new set
one = {1, 2, 3}
two = {5, 6, 7}

newset = one.union(two)
print(newset)

# keep only dups
one = {1, 2, 3}
two = {2, 3, 4}

one.intersection_update(two)
print(one)

# keep not(only) dups
one = {1, 2, 3}
two = {2, 3, 4}

one.symmetric_difference_update(two)
print(one)