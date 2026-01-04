tricky_tuple = (1, 2, [3, 4])
#index          0  1   2
print(len(tricky_tuple))  #3

try:
    tricky_tuple[2] += [5, 6]
except TypeError as e:
    print(f"Error: {e}")

print(f"Result: {tricky_tuple}")
""" 
It throws a TypeError (saying tuples don't support item assignment).
BUT, if you print the tuple, the list has been updated! """