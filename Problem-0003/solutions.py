
__problem_title__ = "Largest prime factor"
__problem_url___ = "https://projecteuler.net/problem=3"
__problem_description__ = "The prime factors of 13195 are 5, 7, 13 and 29. What is the largest " \
                          "prime factor of the number 600851475143 ?"

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

