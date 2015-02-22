
__problem_title__ = "Writing n as the product of k distinct positive integers"
__problem_url___ = "https://projecteuler.net/problem=495"
__problem_description__ = "Let ( , ) be the number of ways in which can be written as the " \
                          "product of distinct positive integers. For example, (144,4) = 7. " \
                          "There are 7 ways in which 144 can be written as a product of 4 " \
                          "distinct positive integers: Note that permutations of the integers " \
                          "themselves are not considered distinct. Furthermore, (100!,10) modulo " \
                          "1 000 000 007 = 287549200. Find (10000!,30) modulo 1 000 000 007."

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

