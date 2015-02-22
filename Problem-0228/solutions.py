
__problem_title__ = "Minkowski Sums"
__problem_url___ = "https://projecteuler.net/problem=228"
__problem_description__ = "Let be the regular -sided polygon – or – whose vertices ( = 1,2,…, ) " \
                          "have coordinates: Each is to be interpreted as a filled shape " \
                          "consisting of all points on the perimeter and in the interior. The , " \
                          "+ , of two shapes and is the result of adding every point in to every " \
                          "point in , where point addition is performed coordinate-wise: ( , ) + " \
                          "( , ) = ( + , + ). For example, the sum of and is the six-sided shape " \
                          "shown in pink below: How many sides does + + … + have?"

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

