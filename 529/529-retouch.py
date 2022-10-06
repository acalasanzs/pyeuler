""" 
A 10-substring of a number is a substring of its digits that sum to 10. For example, the 10-substrings of the number 3523014 are:

352 3014
3 523 014
3 5230 14
35 23014
A number is called 10-substring-friendly if every one of its digits belongs to a 10-substring. For example, 3523014 is 10-substring-friendly, but 28546 is not.

Let T(n) be the number of 10-substring-friendly numbers from 1 to 10n (inclusive).
For example T(2) = 9 and T(5) = 3492.

Find T(1018) mod 1 000 000 007.
"""


def is_10_substring_friendly(number):
    string = str(number)
    total_indices_used = set()
    def substring_10(length, position, string):
        total = 0
        for x in string[position:position + length]:
            total += int(x)
        else:
            if total == 10:
                return True
        return False
    for length in range(0, len(string)):
        for position in range(0, len(string)):
            if substring_10(length, position, string):
                total_indices_used.update(range(position, position + length - 1))
    for pos in range(0, len(string)):
        if not pos in total_indices_used:
            break
    else:
        return True
    return False

print(is_10_substring_friendly(3523014))
