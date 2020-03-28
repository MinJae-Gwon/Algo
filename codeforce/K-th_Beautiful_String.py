#A number is ternary if it contains only digits 0, 1 and 2. For example, the following numbers are ternary: 1022, 11, 21, 2002.

#You are given a long ternary number 𝑥. The first (leftmost) digit of 𝑥 is guaranteed to be 2, the other digits of 𝑥 can be 0, 1 or 2.

#Let's define the ternary XOR operation ⊙ of two ternary numbers 𝑎 and 𝑏 (both of length 𝑛) as a number 𝑐=𝑎⊙𝑏 of length 𝑛, where 𝑐𝑖=(𝑎𝑖+𝑏𝑖)%3 (where % is modulo operation). In other words, add the corresponding digits and take the remainders of the sums when divided by 3. For example, 10222⊙11021=21210.

#Your task is to find such ternary numbers 𝑎 and 𝑏 both of length 𝑛 and both without leading zeros that 𝑎⊙𝑏=𝑥 and 𝑚𝑎𝑥(𝑎,𝑏) is the minimum possible.

#You have to answer 𝑡 independent test cases.

#output
11111
11111
11000
10211
1
1
110111011
110111010

import sys
sys.stdin = open('K-th_Beautiful_String.txt','r')

