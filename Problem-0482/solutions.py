
__problem_title__ = "The incenter of a triangle"
__problem_url___ = "https://projecteuler.net/problem=482"
__problem_description__ = "ABC is an integer sided triangle with incenter I and perimeter p. The " \
                          "segments IA, IB and IC have integral length as well. Let L = p + |IA| " \
                          "+ |IB| + |IC|. Let S(P) = ∑L for all such triangles where p ≤ P. For " \
                          "example, S(10 ) = 3619. Find S(10 )."

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

