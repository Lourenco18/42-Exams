"""
Write a function that finds the intersection of multiple sorted lists.
Return a new list containing elements that appear in ALL  lists, in sorted order.

The function should:
- Return elements that appear in ALL lists
- Result should be sorted in ascending order
- Remove duplicates from the result
- Handle empty  or empty lists gracefully
- If any list is empty, the intersection is empty
FUNCTION SIGNATURE
def list_intersection_finder(lists: list[list[int]]) -> list[int]:
EXAMPLES
list_intersection_finder([[1, 2, 3], [2, 3, 4], [2, 3, 5]])->[2, 3]
list_intersection_finder([[1, 2, 3, 4], [2, 4, 6, 8], [4, 8, 12]])->[4]
list_intersection_finder([[1, 1, 2, 3], [1, 2, 2, 3], [1, 2, 3, 3]])->[1, 2, 3]
list_intersection_finder([[1, 2, 3], [4, 5, 6]])->[]
list_intersection_finder([])->[]
list_intersection_finder([[1, 2, 3], []])->[]
list_intersection_finder([[5]])->[5]
"""
def list_intersection_finder(lists: list[list[int]]) -> list[int]:
    i = 0
    """verificacoes """
    if not lists:
        return []        
    while i < len(lists):
        if lists[i] == []:
            return []
        i +=1
    if len(lists) == 1:
        return lists[0]
    """logica"""
    result = []
    for value in lists[0]:
        if all(value in lista for lista in lists):
            if value not in result:
                result.append(value)
    return result

print(list_intersection_finder([[1, 2, 3], [2, 3, 4], [2, 3, 5]]))
print(list_intersection_finder([[1, 2, 3, 4], [2, 4, 6, 8], [4, 8, 12]]))
print(list_intersection_finder([[1, 1, 2, 3], [1, 2, 2, 3], [1, 2, 3, 3]]))
print(list_intersection_finder([[1, 2, 3], [4, 5, 6]]))
print(list_intersection_finder([]))
print(list_intersection_finder([[1, 2, 3], []]))
print(list_intersection_finder([[5]]))