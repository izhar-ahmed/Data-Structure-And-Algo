def addTo80(n):
    return n + 80

addTo80(5)
addTo80(5)
addTo80(5)
# This function compute the same problem again and again 

memo = {}
def memoizationAddTo80(n):
    if n in memo:
        return memo[n]
    print("long time...")
    memo[n] = n + 80
    return memo[n]

# print(memoizationAddTo80(5))
# print(memoizationAddTo80(5))
# print(memoizationAddTo80(5))
# In second call and third call its directly return the solution without computing.
# Because its already in memo or cache memory.

# We dont want memo in global scop
def memoizAddTo80():
    memo = {}
    def innerMemoizationAddTo80(n):
        if n in memo:
            return memo[n]
        print("long time...")
        memo[n] = n + 80
        return memo[n]
    return innerMemoizationAddTo80

memoize = memoizAddTo80()
print(memoize(5))
print(memoize(5))
print(memoize(5))