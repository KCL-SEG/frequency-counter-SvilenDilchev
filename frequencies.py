"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""


def frequencies(items):
    newList = transformAllItemsToStrings(items)
    uniqueItems = []
    frequencies = {}
    for item in newList:
        print(f"pure item - {item}, string version - {str(item)}")
        if uniqueItems.count(item) == 0 & uniqueItems.count(str(item)) == 0:
            uniqueItems.append(item)

    for item in uniqueItems:
        frequencies[item] = newList.count(item)
    return frequencies


def transformAllItemsToStrings(items):
    newList = []
    for item in items:
        if type(item) == int:
            newList.append(f'{item}')
        else:
            newList.append(item)
    return newList

