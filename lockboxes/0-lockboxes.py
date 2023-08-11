#!/usr/bin/python3
"""
Method that determines if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    n = len(boxes)
    keys_list = [0]

    for element in keys_list:
        if element < n:
            for key in boxes[element]:
                if key not in keys_list or key < n:
                    keys_list.append(key)

    if len(keys_list) == n:
        return True
    return False
