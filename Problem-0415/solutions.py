
__problem_title__ = "Titanic sets"
__problem_url___ = "https://projecteuler.net/problem=415"
__problem_description__ = "A set of lattice points S is called a if there exists a line passing " \
                          "through exactly two points in S. An example of a titanic set is S = " \
                          "{(0, 0), (0, 1), (0, 2), (1, 1), (2, 0), (1, 0)}, where the line " \
                          "passing through (0, 1) and (2, 0) does not pass through any other " \
                          "point in S. On the other hand, the set {(0, 0), (1, 1), (2, 2), (4, " \
                          "4)} is not a titanic set since the line passing through any two " \
                          "points in the set also passes through the other two. For any positive " \
                          "integer , let ( ) be the number of titanic sets S whose every point ( " \
                          ", ) satisfies 0 ≤ , ≤ . It can be verified that (1) = 11, (2) = 494, " \
                          "(4) = 33554178, (111) mod 10 = 13500401 and (10 ) mod 10 = 63259062. " \
                          "Find (10 ) mod 10 ."

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

