#!/usr/bin/python


def firstn(n):
   num, nums = 0, []
   while num < n:
       nums.append(num)
       num += 1
   return nums
   
sum_of_first_n = sum(firstn(10000000000))
