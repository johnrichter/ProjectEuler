
__problem_title__ = "Cuboid layers"
__problem_url___ = "https://projecteuler.net/problem=126"
__problem_description__ = "The minimum number of cubes to cover every visible face on a cuboid " \
                          "measuring 3 x 2 x 1 is twenty-two. If we then add a second layer to " \
                          "this solid it would require forty-six cubes to cover every visible " \
                          "face, the third layer would require seventy-eight cubes, and the " \
                          "fourth layer would require one-hundred and eighteen cubes to cover " \
                          "every visible face. However, the first layer on a cuboid measuring 5 " \
                          "x 1 x 1 also requires twenty-two cubes; similarly the first layer on " \
                          "cuboids measuring 5 x 3 x 1, 7 x 2 x 1, and 11 x 1 x 1 all contain " \
                          "forty-six cubes. We shall define C( ) to represent the number of " \
                          "cuboids that contain cubes in one of its layers. So C(22) = 2, C(46) " \
                          "= 4, C(78) = 5, and C(118) = 8. It turns out that 154 is the least " \
                          "value of for which C( ) = 10. Find the least value of for which C( ) " \
                          "= 1000."

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

