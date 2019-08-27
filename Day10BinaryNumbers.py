# #!/bin/python3

# import math
# import os
# import random
# import re
# import sys




# n = int(input().strip())


# #initialize present and maximum consecutive 1s variables
# presentConsecutive1s = 0
# maxConsecutive1s = 0

# #While we have not finished converting n to binary, n greater than 0
# while n > 0:
#     #We will get the remainder n modulo 2
#     remainder = n % 2
#     if remainder == 1:
#         #If the remainder is equal to 1 then we will increment our
#         #current consecutive 1s counter
#         presentConsecutive1s += 1

#         #if the current consecutive 1s is greater than max consecutive 1s
#         #we will set max consecutives 1s to that value
#         if presentConsecutive1s > maxConsecutive1s:
#             maxConsecutive1s = presentConsecutive1s

#         #if however the remainder is 0 the else condition then we will set
#         #the current consecutive 1s to 0
#         else:
#             presentConsecutive1s = 0

#         #finally we will use integer division to divide n by 2 and reset it
#         #and repeat the while loop
#         n = n // 2

# #When n is equal to 0 we will exit the while loop and print the maximum values
# #of consecutive 1s
# print(maxConsecutive1s)     



# #Version 2


#  #!/bin/python3

#  import sys
#  n = int(input().strip())
#  def max(a,b):
#      return a if a>b else b
#  maxN = 0
#  count = 0
#  while n:
#      while n&1:
#          count+=1
#          n>>=1
#      maxN = max(count,maxN)
#      if not n&1:
#          count = 0
#          n>>=1
#  print(maxN)
 
 
#  #Version 3
 
#  defmodule BinaryNumbers do
#    use Bitwise
 
#    def solve(n, max_num, nums) when n == 0 do
#      Enum.max(nums ++ [max_num])
#    end
 
#    def solve(n, max_num, nums) do
#      if band(n, 1) == 1 do
#        solve(n >>> 1, max_num + 1, nums)
#      else
#        if max_num > 0 do
#          solve(n >>> 1, 0, nums ++ [max_num])
#        else
#          solve(n >>> 1, 0, nums)
#        end
#      end
#    end
 
#    def main() do
#      {n, _} = IO.gets("") |> Integer.parse()
 
#      IO.puts(solve(n, 0, []))
#    end
#  end
 
#  BinaryNumbers.main()
 
 
 
 
 
 
#  #Version 4
 
#  #!/bin/python
 
#  import sys
 
#  n = int(raw_input().strip())
 
#  binary = list(bin(n)[2:])
#  #print (binary)
 
#  count = 0
#  max_count = 0
#  for i in binary:
#      if (i == '1'):
#          count += 1
#      else:
#          if count > max_count:
#              max_count = count
#          count = 0
#  if count > max_count:
#      max_count = count
#  print (max_count)
 
 
 
 
 
 
#  #Version 5

# num = int(input())
# consecutiveOne = 0
# maxOne = 0
# l=[]
# while(num>0):
#     rem = num % 2
#     l.append(rem)
#     if rem == 1:
#         consecutiveOne += 1
#         if consecutiveOne > maxOne:
#             maxOne = consecutiveOne
#     else:
#         consecutiveOne = 0
    
#     num = num // 2
    
# print(maxOne)







#Version Mine
 #!/bin/python3

import sys

n = int(input().strip())
binary = list(str("{0:b}".format(n)))
count = 0
values = []
for i in binary:
    if int(i) == 1:
        count += 1
    else:
        values.append(count)
        count = 0
values.append(count)
print(max(values))

 
 
 
 
 