# Write a Python program to multiply all the items in a dictionary.

from functools import reduce

data = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}


def multiplyDictionaryValues(a, b): return a * b


totalProductOfValues = reduce(multiplyDictionaryValues, data.values())
print(totalProductOfValues)
