"""Write a Python function that takes two lists (arrays) as parameters and determines if the second list is a rotation of the first list (left or right).

A rotation means that the elements are shifted circularly. For example, shifting [1, 2, 3] to the right by one position results in [3, 1, 2].

The function must return True if arr2 is a rotation of arr1, and False otherwise.
If the arrays have different lengths, they cannot be rotations of each other.
Two empty arrays are considered rotations of each other.
FUNCTION SIGNATURE
def array_rotation_detector(arr1: list, arr2: list) -> bool:
EXAMPLES
array_rotation_detector([1, 2, 3, 4, 5], [4, 5, 1, 2, 3])->True
array_rotation_detector([1, 2, 3, 4, 5], [5, 1, 2, 3, 4])->True
array_rotation_detector([1, 2, 3], [3, 2, 1])->False
array_rotation_detector([1, 2], [1, 2, 3])->False
array_rotation_detector([], [])->True"""

def twister(nums, n) -> list:
    if len(nums) == 0:
        return []
    n = n % len(nums)
    return nums[-n:]+ nums[:-n]

def array_rotation_detector(arr1: list, arr2: list) -> bool:
    if len(arr1) == 0:
        if len(arr2) == 0:
            return True
    if len(arr1) != len(arr2):
        return False
    i = 0
    while i < len(arr1):
        if(twister(arr1,i) == arr2):
            return True
        i= i+1

    return False

print(array_rotation_detector([1, 2, 3, 4, 5], [4, 5, 1, 2, 3]))
print(array_rotation_detector([1, 2, 3, 4, 5], [5, 1, 2, 3, 4]))
print(array_rotation_detector([1, 2, 3], [3, 2, 1]))
print(array_rotation_detector([1, 2], [1, 2, 3]))
print(array_rotation_detector([1, 2], []))
print(array_rotation_detector([], []))

