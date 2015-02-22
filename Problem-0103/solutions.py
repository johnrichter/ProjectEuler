
__problem_title__ = "Special subset sums: optimum"
__problem_url___ = "https://projecteuler.net/problem=103"
__problem_description__ = "Let S(A) represent the sum of elements in set A of size . We shall " \
                          "call it a special sum set if for any two non-empty disjoint subsets, " \
                          "B and C, the following properties are true: If S(A) is minimised for " \
                          "a given , we shall call it an optimum special sum set. The first five " \
                          "optimum special sum sets are given below. = 1: {1} = 2: {1, 2} = 3: " \
                          "{2, 3, 4} = 4: {3, 5, 6, 7} = 5: {6, 9, 11, 12, 13} It that for a " \
                          "given optimum set, A = { , , ... , }, the next optimum set is of the " \
                          "form B = { , + , + , ... , + }, where is the "middle" element on the " \
                          "previous row. By applying this "rule" we would expect the optimum set " \
                          "for = 6 to be A = {11, 17, 20, 22, 23, 24}, with S(A) = 117. However, " \
                          "this is not the optimum set, as we have merely applied an algorithm " \
                          "to provide a near optimum set. The optimum set for = 6 is A = {11, " \
                          "18, 19, 20, 22, 25}, with S(A) = 115 and corresponding set string: " \
                          "111819202225. Given that A is an optimum special sum set for = 7, " \
                          "find its set string. NOTE: This problem is related to and ."

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

