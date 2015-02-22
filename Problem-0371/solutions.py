
__problem_title__ = "Licence plates"
__problem_url___ = "https://projecteuler.net/problem=371"
__problem_description__ = "Oregon licence plates consist of three letters followed by a three " \
                          "digit number (each digit can be from [0..9]). While driving to work " \
                          "Seth plays the following game: Whenever the numbers of two licence " \
                          "plates seen on his trip add to 1000 that's a win. E.g. MIC-012 and " \
                          "HAN-988 is a win and RYU-500 and SET-500 too. (as long as he sees " \
                          "them in the same trip). Find the expected number of plates he needs " \
                          "to see for a win. Give your answer rounded to 8 decimal places behind " \
                          "the decimal point. We assume that each licence plate seen is equally " \
                          "likely to have any three digit number on it."

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

