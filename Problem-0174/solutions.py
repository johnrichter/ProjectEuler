
__problem_title__ = "Counting the number of "hollow" square laminae that can form one, two, three, ... distinct arrangements"
__problem_url___ = "https://projecteuler.net/problem=174"
__problem_description__ = "We shall define a square lamina to be a square outline with a square " \
                          ""hole" so that the shape possesses vertical and horizontal symmetry. " \
                          "Given eight tiles it is possible to form a lamina in only one way: " \
                          "3x3 square with a 1x1 hole in the middle. However, using thirty-two " \
                          "tiles it is possible to form two distinct laminae. If represents the " \
                          "number of tiles used, we shall say that = 8 is type L(1) and = 32 is " \
                          "type L(2). Let N( ) be the number of ≤ 1000000 such that is type L( " \
                          "); for example, N(15) = 832. What is ∑ N( ) for 1 ≤ ≤ 10?"

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

