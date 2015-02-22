
__problem_title__ = "Largest palindrome product"
__problem_url___ = "https://projecteuler.net/problem=4"
__problem_description__ = "A palindromic number reads the same both ways. The largest palindrome " \
                          "made from the product of two 2-digit numbers is 9009 = 91 × 99. Find " \
                          "the largest palindrome made from the product of two 3-digit numbers."

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

