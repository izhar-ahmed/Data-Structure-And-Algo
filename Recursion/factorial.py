# Write two functions that finds factorial any number.
# One should use recursive, the other should use for loop
# Factorial example 5 * 4 * 3 * 2 * 1

def findFactorialIterative(num):
    answer = 1
    if num == 2:
        answer = 2
    for i in range(2,num + 1):
        answer *= i 
    return answer

def findFactorialRecursive(num):
    if num == 1: # Base Case
        return 1
    # Recursive Case
    return num * findFactorialRecursive(num - 1) 

print(findFactorialIterative(5))

# 5 * findFactorialRecursive(4)
# 5 * 4 * findFactorialRecursive(3)
# 5 * 4 * 3 findFactorialRecursive(2)
# 5 * 4 * 3 * 2 findFactorialRecursive(1)

# 5 * 4 * 3 * 2 * 1
# 120
