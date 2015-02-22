
__problem_title__ = "Peredur fab Efrawg"
__problem_url___ = "https://projecteuler.net/problem=339"
__problem_description__ = "Initially each flock consists of sheep. Each sheep (regardless of " \
                          "colour) is equally likely to be the next sheep to bleat. After a " \
                          "sheep has bleated and a sheep from the other flock has crossed over, " \
                          "Peredur may remove a number of white sheep in order to maximize the " \
                          "expected final number of black sheep. Let E( ) be the expected final " \
                          "number of black sheep if Peredur uses an optimal strategy. You are " \
                          "given that E(5) = 6.871346 rounded to 6 places behind the decimal " \
                          "point. Find E(10 000) and give your answer rounded to 6 places behind " \
                          "the decimal point."

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

