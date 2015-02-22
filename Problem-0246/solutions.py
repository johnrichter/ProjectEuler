
__problem_title__ = "Tangents to an ellipse"
__problem_url___ = "https://projecteuler.net/problem=246"
__problem_description__ = "A definition for an ellipse is: Given a circle c with centre M and " \
                          "radius r and a point G such that d(G,M)<r, the locus of the points " \
                          "that are equidistant from c and G form an ellipse. Given are the " \
                          "points M(-2000,1500) and G(8000,1500). Given is also the circle c " \
                          "with centre M and radius 15000. The locus of the points that are " \
                          "equidistant from G and c form an ellipse e. From a point P outside e " \
                          "the two tangents t and t to the ellipse are drawn. Let the points " \
                          "where t and t touch the ellipse be R and S. For how many lattice " \
                          "points P is angle RPS greater than 45 degrees?"

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

