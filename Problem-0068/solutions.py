
__problem_title__ = "Magic 5-gon ring"
__problem_url___ = "https://projecteuler.net/problem=68"
__problem_description__ = "Consider the following "magic" 3-gon ring, filled with the numbers 1 " \
                          "to 6, and each line adding to nine. Working , and starting from the " \
                          "group of three with the numerically lowest external node (4,3,2 in " \
                          "this example), each solution can be described uniquely. For example, " \
                          "the above solution can be described by the set: 4,3,2; 6,2,1; 5,1,3. " \
                          "It is possible to complete the ring with four different totals: 9, " \
                          "10, 11, and 12. There are eight solutions in total. By concatenating " \
                          "each group it is possible to form 9-digit strings; the maximum string " \
                          "for a 3-gon ring is 432621513. Using the numbers 1 to 10, and " \
                          "depending on arrangements, it is possible to form 16- and 17-digit " \
                          "strings. What is the maximum string for a "magic" 5-gon ring?"

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

