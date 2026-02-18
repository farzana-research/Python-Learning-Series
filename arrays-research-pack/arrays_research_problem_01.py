"""
1) Prefix Sum Build + Range Sum Query

Problem: Build prefix sums to answer many range-sum queries fast.
Approach: pref[i+1]=pref[i]+a[i]; query sum(l,r)=pref[r+1]-pref[l].
Time: Build O(n), query O(1)
Space: O(n)
Edge cases: empty array, invalid l/r bounds.

"""


from typing import List, Tuple

def build_prefix_sum(a: List[int]) -> List[int]:
    """Build prefix sums where pref[i] = sum of a[:i]."""
    pref = [0]
    for x in a:
        pref.append(pref[-1] + x)
    return pref

def range_sum(pref: List[int], l: int, r: int) -> int:
    """Return sum of original a[l:r+1] using pref built by build_prefix_sum."""
    if l < 0 or r >= len(pref) - 1 or l > r:
        raise ValueError("Invalid range")
    return pref[r + 1] - pref[l]


pref = build_prefix_sum(a)

print("Prefix Sum:", pref)

  

result = range_sum(pref, 1, 3)

print("Range Sum (1,3):", result)