
__problem_title__ = "Cross flips"
__problem_url___ = "https://projecteuler.net/problem=331"
__problem_description__ = "× disks are placed on a square game board. Each disk has a black side " \
                          "and white side. At each turn, you may choose a disk and flip all the " \
                          "disks in the same row and the same column as this disk: thus 2× -1 " \
                          "disks are flipped. The game ends when all disks show their white " \
                          "side. The following example shows a game on a 5×5 board. It can be " \
                          "proven that 3 is the minimal number of turns to finish this game. The " \
                          "bottom left disk on the × board has coordinates (0,0); the bottom " \
                          "right disk has coordinates ( -1,0) and the top left disk has " \
                          "coordinates (0, -1). Let C be the following configuration of a board " \
                          "with × disks: A disk at ( , ) satisfying , shows its black side; " \
                          "otherwise, it shows its white side. C is shown above. Let T( ) be the " \
                          "minimal number of turns to finish a game starting from configuration " \
                          "C or 0 if configuration C is unsolvable. We have shown that T(5)=3. " \
                          "You are also given that T(10)=29 and T(1 000)=395253. Find ."

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

