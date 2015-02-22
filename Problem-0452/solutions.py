
__problem_title__ = "Long Products"
__problem_url___ = "https://projecteuler.net/problem=452"
__problem_description__ = "Define F( , ) as the number of -tuples of positive integers for which " \
                          "the product of the elements doesn't exceed . F(10, 10) = 571. F(10 , " \
                          "10 ) mod 1 234 567 891 = 252903833. Find F(10 , 10 ) mod 1 234 567 " \
                          "891."

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

