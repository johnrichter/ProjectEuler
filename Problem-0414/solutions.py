
__problem_title__ = "Kaprekar constant"
__problem_url___ = "https://projecteuler.net/problem=414"
__problem_description__ = "6174 is a remarkable number; if we sort its digits in increasing " \
                          "order and subtract that number from the number you get when you sort " \
                          "the digits in decreasing order, we get 7641-1467=6174. Even more " \
                          "remarkable is that if we start from any 4 digit number and repeat " \
                          "this process of sorting and subtracting, we'll eventually end up with " \
                          "6174 or immediately with 0 if all digits are equal. This also works " \
                          "with numbers that have less than 4 digits if we pad the number with " \
                          "leading zeroes until we have 4 digits. E.g. let's start with the " \
                          "number 0837: 8730-0378=8352 8532-2358=6174 6174 is called the . The " \
                          "process of sorting and subtracting and repeating this until either 0 " \
                          "or the Kaprekar constant is reached is called the . We can consider " \
                          "the Kaprekar routine for other bases and number of digits. " \
                          "Unfortunately, it is not guaranteed a Kaprekar constant exists in all " \
                          "cases; either the routine can end up in a cycle for some input " \
                          "numbers or the constant the routine arrives at can be different for " \
                          "different input numbers. However, it can be shown that for 5 digits " \
                          "and a base b = 6t+3≠9, a Kaprekar constant exists. E.g. base 15: " \
                          "(10,4,14,9,5) base 21: (14,6,20,13,7) Define to be the Kaprekar " \
                          "constant in base for 5 digits. Define the function to be Define as " \
                          "the sum of for 0 < < . E.g. S(15) = 5274369 S(111) = 400668930299 " \
                          "Find the sum of S(6k+3) for 2 ≤ k ≤ 300. Give the last 18 digits as " \
                          "your answer."

import timeit


class Solution():

    @staticmethod
    def solution1():
        pass

    @staticmethod
    def time_solutions():
        setup = 'from __main__ import Solution'
        print('Solution 1:', timeit.timeit('Solution.solution1()', setup=setup, number=1))


if __name__ == '__main__':
    s = Solution()
    print(s.solution1())
    s.time_solutions()

