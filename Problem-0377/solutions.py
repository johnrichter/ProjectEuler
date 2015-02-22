
__problem_title__ = "Sum of digits, experience 13"
__problem_url___ = "https://projecteuler.net/problem=377"
__problem_description__ = "There are 16 positive integers that do not have a zero in their " \
                          "digits and that have a digital sum equal to 5, namely: 5, 14, 23, 32, " \
                          "41, 113, 122, 131, 212, 221, 311, 1112, 1121, 1211, 2111 and 11111. " \
                          "Their sum is 17891. Let ( ) be the sum of all positive integers that " \
                          "do not have a zero in their digits and have a digital sum equal to . " \
                          "Find $\displaystyle \sum_{i=1}^{17} f(13^i)$. Give the last 9 digits " \
                          "as your answer."

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

