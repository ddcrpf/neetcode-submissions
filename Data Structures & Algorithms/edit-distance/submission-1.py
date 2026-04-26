class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}

        def f(i,j):
            if (i, j) in memo:
                return memo[(i,j)]

            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i

            if word1[i] == word2[j]: 
                ans  = f(i+1, j+1)
            else:
                ans = 1 + min(f(i+1,j), f(i, j+1), f(i+1, j+1))
                memo[(i,j)] = ans
            return ans 


        return f(0,0)
    

#     w1 -> w2 

# Input: word1 = "monkeys", word2 = "money"



# f(0,0) = 
# F(1,1)
# m == m
# o == o
# n == n
# k != e 
# delete k 
# f(0,0) -> match -> 
# f(1,1) -> match -> f(2,2) -
# > match -> f(3,3) -> mismatch -> 
# delete k 
# replace k -> e
# insert e
# delete -> k


# f(3,3) k != e  delete 
# |-> f(4,3) e = e -> f(5,4) -> y = y -> f(6,5) s!="" delete -> f(7,6)
# -> 2
# ney
# f(3,3)
# |-> 










