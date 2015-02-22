
__problem_title__ = "Sliders"
__problem_url___ = "https://projecteuler.net/problem=244"
__problem_description__ = "You probably know the game . Here, instead of numbered tiles, we have " \
                          "seven red tiles and eight blue tiles. A move is denoted by the " \
                          "uppercase initial of the direction (Left, Right, Up, Down) in which " \
                          "the tile is slid, e.g. starting from configuration ( ), by the " \
                          "sequence we reach the configuration ( ): For each path, its checksum " \
                          "is calculated by (pseudocode): For the sequence given above, the " \
                          "checksum would be 19761398. Now, starting from configuration ( ), " \
                          "find all shortest ways to reach configuration ( ). What is the sum of " \
                          "all checksums for the paths having the minimal length?"

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

