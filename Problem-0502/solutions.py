
__problem_title__ = "Counting Castles"
__problem_url___ = "https://projecteuler.net/problem=502"
__problem_description__ = "We define a to be a rectangle with a height of 1 and an " \
                          "integer-valued length. Let a be a configuration of stacked blocks. " \
                          "Given a game grid that is units wide and units tall, a castle is " \
                          "generated according to the following rules: The following is a sample " \
                          "castle for =8 and =5: Let F( , ) represent the number of valid " \
                          "castles, given grid parameters and . For example, F(4,2) = 10, " \
                          "F(13,10) = 3729050610636, F(10,13) = 37959702514, and F(100,100) mod " \
                          "1 000 000 007 = 841913936. Find (F(10 ,100) + F(10000,10000) + " \
                          "F(100,10 )) mod 1 000 000 007."

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

