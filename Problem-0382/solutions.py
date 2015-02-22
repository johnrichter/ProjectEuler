
__problem_title__ = "Generating polygons"
__problem_url___ = "https://projecteuler.net/problem=382"
__problem_description__ = "A is a flat shape consisting of straight line segments that are " \
                          "joined to form a closed chain or circuit. A polygon consists of at " \
                          "least three sides and does not self-intersect. A set S of positive " \
                          "numbers is said to P if: For example: The set {3, 4, 5} generates a " \
                          "polygon with sides 3, 4, and 5 (a triangle). The set {6, 9, 11, 24} " \
                          "generates a polygon with sides 6, 9, 11, and 24 (a quadrilateral). " \
                          "The sets {1, 2, 3} and {2, 3, 4, 9} do not generate any polygon at " \
                          "all. Consider the sequence s, defined as follows: Let U be the set {s " \
                          ", s , ..., s }. For example, U = {1, 2, 3, 4, 6, 9, 13, 19, 28, 41}. " \
                          "Let f( ) be the number of subsets of U which generate at least one " \
                          "polygon. For example, f(5) = 7, f(10) = 501 and f(25) = 18635853. " \
                          "Find the last 9 digits of f(10 )."

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

