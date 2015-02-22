
__problem_title__ = "Nim"
__problem_url___ = "https://projecteuler.net/problem=301"
__problem_description__ = "is a game played with heaps of stones, where two players take it in " \
                          "turn to remove any number of stones from any heap until no stones " \
                          "remain. We'll consider the three-heap normal-play version of Nim, " \
                          "which works as follows: - At the start of the game there are three " \
                          "heaps of stones. - On his turn the player removes any positive number " \
                          "of stones from any single heap. - The first player unable to move " \
                          "(because no stones remain) loses. If ( , , ) indicates a Nim position " \
                          "consisting of heaps of size , and then there is a simple function ( , " \
                          ", ) — that you may look up or attempt to deduce for yourself — that " \
                          "returns: For example (1,2,3) = 0 because, no matter what the current " \
                          "player does, his opponent can respond with a move that leaves two " \
                          "heaps of equal size, at which point every move by the current player " \
                          "can be mirrored by his opponent until no stones remain; so the " \
                          "current player loses. To illustrate: - current player moves to " \
                          "(1,2,1) - opponent moves to (1,0,1) - current player moves to (0,0,1) " \
                          "- opponent moves to (0,0,0), and so wins. For how many positive " \
                          "integers ≤ 2 does ( ,2 ,3 ) = 0 ?"

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

