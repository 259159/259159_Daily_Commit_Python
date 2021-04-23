lst = [("x", 1), ("x", 2), ("x", 3), ("y", 1), ("y", 2), ("z", 1)]
print(" List of tuples before converting to dictionary", lst)
dict = {}
for a, b in lst:
    dict.setdefault(a, []).append(b)
print("\n")
print("List of tuples after converting to dictionary ", dict)
