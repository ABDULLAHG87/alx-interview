#!/usr/bin/python3
""" A method that determines if a given data set represent
a valid UTF-8 encoding"""


def validUTF8(data):
    """Method to validate UTF8 of data"""
    UTF_BIT_1 = 1 << 7  # Negative value
    UTF_BIT_2 = 1 << 6  # Positive value
    nbytes = 0

    if not data or len(data) == 0:
        return True

    # looping through each byte of the data
    for num in data:
        # creating a mask to check most significant Bit (MSB)
        bit_mask = 1 << 7
        if nbytes == 0:
            while bit_mask & num:
                nbytes += 1
                bit_mask = bit_mask >> 1

            if nbytes == 0:
                continue
            if nbytes == 1 or nbytes > 4:
                return False
        else:
            if not (num & UTF_BIT_1 and not (num & UTF_BIT_2)):
                return False
        nbytes -= 1

    if nbytes == 0:
        return True
    else:
        return False
