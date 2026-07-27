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