
__problem_title__ = "Permuted multiples"
__problem_url___ = "https://projecteuler.net/problem=52"
__problem_description__ = "It can be seen that the number, 125874, and its double, 251748, " \
                          "contain exactly the same digits, but in a different order. Find the " \
                          "smallest positive integer, , such that 2 , 3 , 4 , 5 , and 6 , " \
                          "contain the same digits."

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

