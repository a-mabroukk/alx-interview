#!/usr/bin/python3
"""Lockboxes"""

from collections import deque


def canUnlockAll(boxes):
    """method that determines if all the boxes can be opened"""
    n = len(boxes)
    visited = set()
    queue = deque([0])

    while queue:
        current_box = queue.popleft()  # Get the next box to process
        if current_box in visited:
            continue  # Skip if this box is already visited

        visited.add(current_box)

        # Add all boxes that can be unlocked with the keys in the current box
        for key in boxes[current_box]:
            if key < n and key not in visited:  # Check if the key is valid
                queue.append(key)

    # Check if all boxes have been visited
    return len(visited) == n
