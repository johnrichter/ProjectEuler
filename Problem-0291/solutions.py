
__problem_title__ = "Panaitopol Primes"
__problem_url___ = "https://projecteuler.net/problem=291"
__problem_description__ = "A prime number is called a Panaitopol prime if for some positive " \
                          "integers and . Find how many Panaitopol primes are less than 5×10 ."

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

