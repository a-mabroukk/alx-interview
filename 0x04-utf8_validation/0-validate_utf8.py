#!/usr/bin/python3
"""python"""


def validUTF8(data):
    """method that determines if a given data set represents a
    valid UTF-8 encoding"""
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    # Masks to check the most significant bits
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for byte in data:
        # Only look at the least significant 8 bits of each integer
        byte = byte & 0xFF

        if num_bytes == 0:
            # Check how many leading 1s are in the byte
            mask = 1 << 7
            while mask & byte:
                num_bytes += 1
                mask = mask >> 1

            # If no leading 1s, it's a 1-byte character
            if num_bytes == 0:
                continue

            # If the number of leading 1s is more than 4 or 1, it's invalid
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # All other bytes in a multi-byte character must start with '10'
            if not (byte & mask1 and not (byte & mask2)):
                return False

        # Decrease the number of bytes remaining in the current character
        num_bytes -= 1

    return num_bytes == 0
