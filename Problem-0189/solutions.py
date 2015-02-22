
__problem_title__ = "Tri-colouring a triangular grid"
__problem_url___ = "https://projecteuler.net/problem=189"
__problem_description__ = "Consider the following configuration of 64 triangles: We wish to " \
                          "colour the interior of each triangle with one of three colours: red, " \
                          "green or blue, so that no two neighbouring triangles have the same " \
                          "colour. Such a colouring shall be called valid. Here, two triangles " \
                          "are said to be neighbouring if they share an edge. Note: if they only " \
                          "share a vertex, then they are not neighbours. For example, here is a " \
                          "valid colouring of the above grid: A colouring C' which is obtained " \
                          "from a colouring C by rotation or reflection is considered from C " \
                          "unless the two are identical. How many distinct valid colourings are " \
                          "there for the above configuration?"

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

