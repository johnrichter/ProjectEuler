
__problem_title__ = "Bounded Sequences"
__problem_url___ = "https://projecteuler.net/problem=319"
__problem_description__ = "Let , ,..., be a sequence of length such that: There are only five " \
                          "such sequences of length 2, namely: {2,4}, {2,5}, {2,6}, {2,7} and " \
                          "{2,8}. There are 293 such sequences of length 5; three examples are " \
                          "given below: {2,5,11,25,55}, {2,6,14,36,88}, {2,8,22,64,181}. Let ( ) " \
                          "denote the number of such sequences of length . You are given that " \
                          "(10) = 86195 and (20) = 5227991891. Find (10 ) and give your answer " \
                          "modulo 10 ."

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

