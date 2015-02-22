
__problem_title__ = "Sum square difference"
__problem_url___ = "https://projecteuler.net/problem=6"
__problem_description__ = "The sum of the squares of the first ten natural numbers is, The " \
                          "square of the sum of the first ten natural numbers is, Hence the " \
                          "difference between the sum of the squares of the first ten natural " \
                          "numbers and the square of the sum is 3025 − 385 = 2640. Find the " \
                          "difference between the sum of the squares of the first one hundred " \
                          "natural numbers and the square of the sum."

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

