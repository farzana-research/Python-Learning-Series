



## 1) Prefix Sum Build + Range Sum Query

**Problem:** Build prefix sums to answer many range-sum queries fast.  
**Approach:** `pref[i+1]=pref[i]+a[i]`; query sum(l,r)=pref[r+1]-pref[l].  
**Time:** Build `O(n)`, query `O(1)`  
**Space:** `O(n)`  
**Edge cases:** empty array, invalid l/r bounds.
