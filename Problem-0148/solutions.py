
__problem_title__ = "Exploring Pascal's triangle"
__problem_url___ = "https://projecteuler.net/problem=148"
__problem_description__ = "We can easily verify that none of the entries in the first seven rows " \
                          "of Pascal's triangle are divisible by 7: However, if we check the " \
                          "first one hundred rows, we will find that only 2361 of the 5050 " \
                          "entries are divisible by 7. Find the number of entries which are " \
                          "divisible by 7 in the first one billion (10 ) rows of Pascal's " \
                          "triangle."

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

