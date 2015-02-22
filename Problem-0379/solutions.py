
__problem_title__ = "Least common multiple count"
__problem_url___ = "https://projecteuler.net/problem=379"
__problem_description__ = "Let ( ) be the number of couples ( , ) with and positive integers, ≤ " \
                          "and the least common multiple of and equal to . Let be the of , i.e.: " \
                          "( ) = ∑ ( ) for 1 ≤ ≤ . You are given that (10 ) = 37429395. Find (10 " \
                          ")."

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

