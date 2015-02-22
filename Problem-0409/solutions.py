
__problem_title__ = "Nim Extreme"
__problem_url___ = "https://projecteuler.net/problem=409"
__problem_description__ = "Let be a positive integer. Consider positions where: Let W( ) be the " \
                          "number of winning nim positions satisfying the above conditions (a " \
                          "position is winning if the first player has a winning strategy). For " \
                          "example, W(1) = 1, W(2) = 6, W(3) = 168, W(5) = 19764360 and W(100) " \
                          "mod 1 000 000 007 = 384777056. Find W(10 000 000) mod 1 000 000 007."

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

