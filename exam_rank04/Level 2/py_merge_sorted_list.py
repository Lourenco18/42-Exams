"""
You are given a list of sorted integer sublists in any order.
Merge all sublists into a single sorted list in ascending order and return it.

Constraints:
- The outer list may be empty -> return []
- Empty sublists may exist and should be ignored.
- Values can repeat (keep the duplicates).
- Each sublist is already sorted individually.
FUNCTION SIGNATURE
def merge_sorted_list(lists: list[list[int]]) ->[ list[int]:
EXAMPLES
merge_sorted_list([[1, , 5], [1, 3, 4], [2, 6]])->[1, 1, 2, 3, 4, 4, 5, 6]
merge_sorted_list([[1, 2, 3], [], [0, 4]])->[0, 1, 2, 3, 4]
merge_sorted_list([])->[]
merge_sorted_list([[], []])->[]
"""
def merge_sorted_list(lists: list[list[int]]) -> list[int]:
    if not lists:
        return []  
    i = 0
    result = []
    while i < len(lists):
        result+=  sorted(lists[i])
        i+=1
    return sorted(result)
print(merge_sorted_list([[1, 4, 5], [1, 3, 4], [2, 6]]))
print(merge_sorted_list([[1, 2, 3], [], [0, 4]]))
print(merge_sorted_list([]))
print(merge_sorted_list([[], []]))