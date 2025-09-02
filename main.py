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
    def __init__(self, longest_size , left_size , right_size , is_entire_range ):
        self.longest_size  = longest_size 
        self.left_size  = left_size 
        self.right_size  = right_size 
        self.is_entire_range  = is_entire_range 

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

    is_entire_range = left.is_entire_range + right.is_entire_range if left.is_entire_range == mid and right.is_entire_range == len(arr) - mid else 0
    left_size = left.left_size if left.left_size != mid else left.left_size + right.left_size
    right_size = right.right_size if right.right_size != (len(arr) - mid) else right.right_size + left.right_size
    longest_size = max(left.longest_size, right.longest_size, left.right_size + right.left_size)

    return Result(longest_size, left_size, right_size, is_entire_range)

def get_longest_run(arr, key):
    return longest_run_recursive(arr, key).longest_size

## Feel free to add your own tests here.
def test_longest_run():
    assert get_longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3

## Tests
test_longest_run()

