def febnacciIterative(num):
    if num == 0:
        return 0
    if num == 1:
        return [0,1]
    answer = [0, 1]
    for i in range(2, num + 1):
        answer.append(answer[len(answer) - 1] + answer[len(answer) - 2])
    return answer[len(answer) - 1]

def febonacciRecursive(num):
    if num < 2:
        return num
    
    return febonacciRecursive(num - 1) + febonacciRecursive(num - 2)


print(febnacciIterative(8))