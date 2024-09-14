# Fibonecci sequence without dynamic programming.
def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)

# The above solution is inefficient because it recompute same subproblem again and again.

# Fibonecci sequence using dynamic programming
def fib_memoization(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memoization(n - 1, memo) + fib_memoization(n - 2, memo)
    return memo[n]

# The above solution is using dynamic programming and we used memoization for optimization.
# It stores the subproblems solutions so it can prevent redundant computation.


# Here is bottom-up approach
def fib3(n):
    answer = [0, 1]
    for i in range(2, len(n)):
        answer.append(answer[i-2] + answer[i-1])
    return answer.pop()

#-----------------------------------------------

# Here are some popular Dynamic Programming Questions (see if you can notice the pattern):

# 1. House Robber    
# 2. Best Time to Buy and Sell Stock  
# 3. Climbing Stairs    