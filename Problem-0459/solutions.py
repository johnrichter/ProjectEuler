
__problem_title__ = "Flipping game"
__problem_url___ = "https://projecteuler.net/problem=459"
__problem_description__ = "The flipping game is a two player game played on a N by N square " \
                          "board. Each square contains a disk with one side white and one side " \
                          "black. The game starts with all disks showing their white side. A " \
                          "turn consists of flipping all disks in a rectangle with the following " \
                          "properties: Players alternate turns. A player wins by turning the " \
                          "grid all black. Let W(N) be the number of for the first player on a N " \
                          "by N board with all disks white, assuming perfect play. W(1) = 1, " \
                          "W(2) = 0, W(5) = 8 and W(10 ) = 31395. For N=5, the first player's " \
                          "eight winning first moves are: Find W(10 )."

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

