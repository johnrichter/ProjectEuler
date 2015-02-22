
__problem_title__ = "Intersections"
__problem_url___ = "https://projecteuler.net/problem=165"
__problem_description__ = "A segment is uniquely defined by its two endpoints. By considering " \
                          "two line segments in plane geometry there are three possibilities: " \
                          "the segments have zero points, one point, or infinitely many points " \
                          "in common. Moreover when two segments have exactly one point in " \
                          "common it might be the case that that common point is an endpoint of " \
                          "either one of the segments or of both. If a common point of two " \
                          "segments is not an endpoint of either of the segments it is an " \
                          "interior point of both segments. We will call a common point T of two " \
                          "segments L and L a true intersection point of L and L if T is the " \
                          "only common point of L and L and T is an interior point of both " \
                          "segments. Consider the three segments L , L , and L : L : (27, 44) to " \
                          "(12, 32) L : (46, 53) to (17, 62) L : (46, 70) to (22, 40) It can be " \
                          "verified that line segments L and L have a true intersection point. " \
                          "We note that as the one of the end points of L : (22,40) lies on L " \
                          "this is not considered to be a true point of intersection. L and L " \
                          "have no common point. So among the three line segments, we find one " \
                          "true intersection point. Now let us do the same for 5000 line " \
                          "segments. To this end, we generate 20000 numbers using the so-called " \
                          ""Blum Blum Shub" pseudo-random number generator. s = 290797 s = s ×s " \
                          "(modulo 50515093) t = s (modulo 500) To create each line segment, we " \
                          "use four consecutive numbers t . That is, the first line segment is " \
                          "given by: (t , t ) to (t , t ) The first four numbers computed " \
                          "according to the above generator should be: 27, 144, 12 and 232. The " \
                          "first segment would thus be (27,144) to (12,232). How many distinct " \
                          "true intersection points are found among the 5000 line segments?"

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

