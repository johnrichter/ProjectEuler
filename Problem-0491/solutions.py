
__problem_title__ = "Double pandigital number divisible by 11"
__problem_url___ = "https://projecteuler.net/problem=491"
__problem_description__ = "We call a positive integer if it uses all the digits 0 to 9 exactly " \
                          "twice (with no leading zero). For example, 40561817703823564929 is " \
                          "one such number. How many double pandigital numbers are divisible by " \
                          "11?"

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

