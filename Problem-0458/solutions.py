
__problem_title__ = "Permutations of Project"
__problem_url___ = "https://projecteuler.net/problem=458"
__problem_description__ = "Consider the alphabet A made out of the letters of the word " \
                          ""project": A={c,e,j,o,p,r,t}. Let T(n) be the number of strings of " \
                          "length n consisting of letters from A that do not have a substring " \
                          "that is one of the 5040 permutations of "project". Find T(10 ). Give " \
                          "the last 9 digits of your answer."

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

