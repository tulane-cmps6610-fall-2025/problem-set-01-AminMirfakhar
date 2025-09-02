"""
CMPS 6610  Assignment 1.
See problemset-01.pdf for details.
"""
# no imports needed.

def foo(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        x, y = min(a, b), max(a, b)
        return foo(y, y%x)


def longest_run(mylist, key):
    counter = 0
    longest = 0
    for element in mylist:
        if element == key:
            counter += 1
            longest = max(counter, longest)
        else:
            counter = 0

    return longest


class Result:
    def __init__(self, longest, prefix, suffix, total):
        self.longest = longest
        self.prefix = prefix
        self.suffix = suffix
        self.total = total

def longest_run_recursive(arr, key):
    if len(arr) == 0:
        return Result(0, 0, 0, 0)
    if len(arr) == 1:
        if arr[0] == key:
            return Result(1, 1, 1, 1)
        else:
            return Result(0, 0, 0, 0)

    mid = len(arr) // 2
    left = longest_run_recursive(arr[:mid], key)
    right = longest_run_recursive(arr[mid:], key)

    total = left.total + right.total if left.total == mid and right.total == len(arr) - mid else 0
    prefix = left.prefix if left.prefix != mid else left.prefix + right.prefix
    suffix = right.suffix if right.suffix != (len(arr) - mid) else right.suffix + left.suffix
    longest = max(left.longest, right.longest, left.suffix + right.prefix)

    return Result(longest, prefix, suffix, total)

def get_longest_run(arr, key):
    return longest_run_recursive(arr, key).longest

## Feel free to add your own tests here.
def test_longest_run():
    assert get_longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3


