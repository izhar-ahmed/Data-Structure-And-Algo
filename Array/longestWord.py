# My solution
def longestWord(str):
    longestWord = ""
    arr = str.split(" ")
    for i in range(len(arr)):
        if len(arr[i]) > len(longestWord):
            longestWord = arr[i]
    
    return longestWord

print(longestWord("izhar is awesome"))
