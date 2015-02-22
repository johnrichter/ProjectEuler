
__problem_title__ = "Eleven-free integers"
__problem_url___ = "https://projecteuler.net/problem=442"
__problem_description__ = "An integer is called if its decimal expansion does not contain any " \
                          "substring representing a power of 11 except 1. For example, 2404 and " \
                          "13431 are eleven-free, while 911 and 4121331 are not. Let E( ) be the " \
                          "th positive eleven-free integer. For example, E(3) = 3, E(200) = 213 " \
                          "and E(500 000) = 531563. Find E(10 )."

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

