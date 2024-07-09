# What is the Big O of the below function? (Hint, you may want to go line by line)
def funChallenge(input):
   a = 10 # O(1)
   a = 50 + 3 #O(1)

   for i in range(len(input)): # O(n)
     anotherFunction() # O(n)
     stranger = true #O(n)
  
   return a #O(1)

# O(1) + O(1) + O(n) + O(n) + O(n) + O(1)
# O (1 + 1 + 1 + n + n + n)
# O(3 + 3n)
# O(n)

# // What is the Big O of the below function? (Hint, you may want to go line by line)
# function anotherFunChallenge(input) {
#     let a = 5; // O(1)
#     let b = 10; // O(1)
#     let c = 50; // O(1)
#     for (let i = 0; i < input; i++) { // O(n)
#       let x = i + 1; // O(n)
#       let y = i + 2; // O(n)
#       let z = i + 3; // O(n)

#     }
#     for (let j = 0; j < input; j++) { // O(n)
#       let p = j * 2; // O(n)
#       let q = j * 2; // O(n) 
#     }
#     let whoAmI = "I don't know"; // O(1)
#   }
#   // Big O = 4 + 7n = O(n)


