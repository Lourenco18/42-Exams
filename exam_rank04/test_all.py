"""Write a Python function that takes two lists (arrays) as parameters and determines if the second list is a rotation of the first list (left or right).

A rotation means that the elements are shifted circularly. For example, shifting [1, 2, 3] to the right by one position results in [3, 1, 2].

The function must return True if arr2 is a rotation of arr1, and False otherwise.
If the arrays have different lengths, they cannot be rotations of each other.
Two empty arrays are considered rotations of each other.
FUNCTION SIGNATURE
def array_rotation_detector(arr1: list, arr2: list) -> bool:
EXAMPLES
array_rotation_detector([1, 2, 3, 4, 5], [4, 6, 1, 2, 3])->True
array_rotation_detector([1, 2, 3, 4, 5], [5, 1, 2, 3, 4])->True
array_rotation_detector([1, 2, 3], [3, 2, 1])->False
array_rotation_detector([1, 2], [1, 2, 3])->False
array_rotation_detector([], [])->True"""
print("-----Rotation detector-----")
def twister(nums,n):
    if len(nums) == 0:
        return []
    n %= len(nums)
    return nums[-n:] + nums[:-n]
def array_rotation_detector(arr1: list, arr2: list) -> bool:
    if len(arr1) != len(arr2):
        return False
    if arr1 == []:
        return True
    i = 0
    while i < len(arr1):
        if twister(arr1,i) == arr2:
            return True
        i+=1
    return False
print(array_rotation_detector([1, 2, 3, 4, 5], [4, 5, 1, 2, 3]))
print(array_rotation_detector([1, 2, 3, 4, 5], [5, 1, 2, 3, 4]))
print(array_rotation_detector([1, 2, 3], [3, 2, 1]))
print(array_rotation_detector([1, 2], [1, 2, 3]))
print(array_rotation_detector([1, 2], []))
print(array_rotation_detector([], []))
"""
For this exercise, you must implement the `constellation_mapper` function. The function must:
- Take as a parameter a list of tuples, each consisting of an int(row) and an int(col).
- Return a list[str] representing a grid of size `size` * `size`, composed of "." and "*" characters based on the coordinates provided in the `stars` variable.
- Ignore coordinates that fall outside the grid boundaries.
- Ignore duplicate coordinates.
FUNCTION SIGNATURE
def constellation_mapper(stars: list[tuple[int, int]], size: int) -> list[str]:
EXAMPLES
constellation_mapper([(0, 0), (1, 1), (2, 2)], 3)->["*..", ".*.", "..*"]
constellation_mapper([(0, 0), (0, 1), (0, 2), (1, 1), (2, 2)], 3)->["***", ".*.", "..*"]
constellation_mapper([(0, 0), (5, 5), (2, 2)], 3)->["*..", "...", "..*"]
constellation_mapper([(0, 0), (5, 5)], 2)->["*.", ".."]
"""
print("-----Constellation Mapper-----")
def constellation_mapper(stars: list[tuple[int, int]], size: int) -> list[str]:
    grid = []
    i = 0
    while i < size:
        grid.append(["."]*size)
        i+=1
    for row, col in stars:
        if 0 <= row < size and 0 <= col < size:
            grid[row][col] = "*"
    result = []
    for row in grid:
        result.append("".join(row))
    return result

print(constellation_mapper([(0, 0), (1, 1), (2, 2)], 3))
print(constellation_mapper([(0, 0), (0, 1), (0, 2), (1, 1), (2, 2)], 3))
print(constellation_mapper([(0, 0), (5, 5), (2, 2)], 3))
print(constellation_mapper([(0, 0), (5, 5)], 2))
print(constellation_mapper([(0, 0), (0, 0), (0, 0)], 2))
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
print("-----Intersection Finder-----")
def list_intersection_finder(lists: list[list[int]]) -> list[int]:
    if not lists: 
        return []
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
"""
You are given a list of sorted integer sublists in any order.
Merge all sublists into a single sorted list in ascending order and return it.

Constraints:
- The outer list may be empty -> return []
- Empty sublists may exist and should be ignored.
- Values can repeat (keep the duplicates).
- Each sublist is already sorted individually.
FUNCTION SIGNATURE
def merge_sorted_list(lists: list[list[int]]) -> list[int]:
EXAMPLES
merge_sorted_list([[1, , 5], [1, 3, 4], [2, 6]])->[1, 1, 2, 3, 4, 4, 5, 6]
merge_sorted_list([[1, 2, 3], [], [0, 4]])->[0, 1, 2, 3, 4]
merge_sorted_list([])->[]
merge_sorted_list([[], []])->[]
"""
print("-----Merge List-----")
def merge_sorted_list(lists: list[list[int]]) -> list[int]:
    if not lists: 
        return []
    result = []
    i = 0
    while i < len(lists):
        result += lists[i]
        i+=1
    return sorted(result)
print(merge_sorted_list([[1, 5], [1, 3, 4], [2, 6]]))
"""Given a string `s`, find the minimum number of cuts needed to partition it such that every resulting substring is a palindrome.

A cut divides the string between two characters. With `c` cuts, the string is split into `c + 1` substrings. We want the minimum number of cuts `c` such that all parts are palindromes.

Return this minimum number of cuts (an integer).

Constraints:
- An empty string or a string of length 1 is already a palindrome -> 0 cuts.
- If the entire string is already a palindrome -> 0 cuts.
- In the worst case (all characters are distinct), the result is len(s) - 1 cuts.
FUNCTION SIGNATURE
def palindrome_partitioner(s: str) -> int:
EXAMPLES
palindrome_partitioner("aab")->1
palindrome_partitioner("aba")->0
palindrome_partitioner("abc")->2"""
print("-----Palindrome-----")
def is_palindrome(parcial):
    return parcial == parcial[::-1] 
def find_mi_cuts(s,dp,end):
    best = end
    for start in range(end+1):
        parcial = s[start:end+1]
        if is_palindrome(parcial):
            if start == 0:
                best = 0
            else:
                cuts = dp[start -1] +1
                best = min(best,cuts)
    return best

def palindrome_partitioner(s: str) -> int:
    if len(s) <=1:
        return 0
    dp = [0] * len(s)
    for end in range (len(s)):
        dp[end] = find_mi_cuts(s,dp,end)
    return dp[-1]
print(palindrome_partitioner("aac"))
print(palindrome_partitioner("aba"))
print(palindrome_partitioner("abc"))
"""
Given a list of integers `nums` and an integer `k`, consider a "window" of size `k` sliding from left to right, one position at a time.

For each window position, find the maximum value within it.
Return the list of all these maximum values, in the order the windows appear.

Constraints:
- 1 <= k <= len(nums) in normal cases.
- If nums is empty or k <= 0, return [].
- The number of windows (and maximums) is: len(nums) - k + 1.
FUNCTION SIGNATURE
def sliding_window_maximium(nums: list[int], k: int) -> list[int]:
EXAMPLES
sliding_window_maximium([1, 3, -1, -3, 5, 3, 6, 7], 3)->[3, 3, 5, 5, 6, 7]
sliding_window_maximium([4, 2, 12, 11, -5], 2)->[4, 12, 12, 11]
sliding_window_maximium([], 3)->[]
"""
print("-----Sliding Window Maximium-----")
def sliding_window_maximium(nums: list[int], k: int) -> list[int]:
    if not nums or k <=0 or k > len(nums):
        return []
    i = 0
    result = []
    while i < len(nums) -k +1:
        biggest = nums[i]
        j = 1
        while j < k:
            if biggest < nums[i+j]:
                biggest = nums[i+j]
            j+=1
        i+=1
        result.append(biggest)
    return result 
print(sliding_window_maximium([4, 2, 12, 11, -5], 2))


"""
Write a function that determines a valid package installation order by resolving dependencies. Use topological sorting to ensure dependencies are installed before the packages that require them.

The function should:
- Take a dictionary where keys are package names and values are lists of dependencies.
- Return packages in installation order (dependencies first).
- Return an empty list ([]) if no valid order exists (e.g., circular dependencies or self-dependencies).
- Handle empty inputs and isolated dependency chains gracefully.
- Ignore references to packages that are not present as keys in the input dictionary.
- Ensure a package cannot be installed until all its dependencies are installed.

Algorithm Details & Edge Cases:
- Topological Sorting: Use a topological sort algorithm (e.g., Kahn's algorithm).
- Dependency Priority: Process packages with no remaining dependencies first.
- Deterministic Output: When multiple valid packages can be processed at the same time (choices exist), process them alphabetically to ensure deterministic output.
- Empty Input: Return an empty list.
- Multiple Independent Chains: Process all chains, respecting the alphabetical order rule.
- Missing Dependencies: Ignore missing packages (treat them as if they don't exist in the requirements).
FUNCTION SIGNATURE
def package_dependency_resolver(packages: dict[str, list[str]]) -> list[str]:
EXAMPLES
package_dependency_resolver({"app": ["database"], "database": ["driver"], "driver": []})->["driver", "database", "app"]
package_dependency_resolver({"A": [], "B": ["A"], "C": ["A", "B"]})->["A", "B", "C"]
package_dependency_resolver({})->[]
package_dependency_resolver({"X": ["Y"], "Y": ["X"]})->[]
package_dependency_resolver({"web": [], "api": [], "frontend": ["web"], "backend": ["api"]})->["api", "backend", "web", "frontend"]
"""

def package_dependency_resolver(packages: dict[str, list[str]]) -> list[str]:
    if not packages:
        return []
    result = []
    wait = {}
    connections = {}
    for package in packages:
        wait[package] = 0
        connections[package] = []
    for package in packages:
        for dependencies in packages[package]:
            if dependencies in packages:
                wait[package] +=1
                connections[dependencies].append(package)
    ready = []
    for package in wait:
        if wait[package] ==0:
            ready.append(package)
    ready.sort()
    result = []
    while ready:
        current = ready.pop(0)
        result.append(current)
        for package in connections[current]:
            wait[package]-=1
            if wait[package] == 0:
                ready.append(package)
        ready.sort()
    if len(result) != len(packages):
        return []
    return result
    
print(package_dependency_resolver(
    {"app": ["database"], "database": ["driver"], "driver": []}
))
print(package_dependency_resolver(
    {"A": [], "B": ["A"], "C": ["A", "B"]}
))
print(package_dependency_resolver({}))
print(package_dependency_resolver(
    {"X": ["Y"], "Y": ["X"]}
))
print(package_dependency_resolver(
    {"web": [], "api": [], "frontend": ["web"], "backend": ["api"]}
))
