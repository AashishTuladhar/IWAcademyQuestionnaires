# Write a python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.

data = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]


def lastElement(n):
    return n[-1]


def sortTupleByLastElement(tupleCollection):
    return sorted(tupleCollection, key=lastElement)


print(sortTupleByLastElement(data))
