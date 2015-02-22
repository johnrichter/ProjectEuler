
__problem_title__ = "Pandigital multiples"
__problem_url___ = "https://projecteuler.net/problem=38"
__problem_description__ = "Take the number 192 and multiply it by each of 1, 2, and 3: By " \
                          "concatenating each product we get the 1 to 9 pandigital, 192384576. " \
                          "We will call 192384576 the concatenated product of 192 and (1,2,3) " \
                          "The same can be achieved by starting with 9 and multiplying by 1, 2, " \
                          "3, 4, and 5, giving the pandigital, 918273645, which is the " \
                          "concatenated product of 9 and (1,2,3,4,5). What is the largest 1 to 9 " \
                          "pandigital 9-digit number that can be formed as the concatenated " \
                          "product of an integer with (1,2, ... , ) where > 1?"

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

