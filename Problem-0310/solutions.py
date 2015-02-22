
__problem_title__ = "Nim Square"
__problem_url___ = "https://projecteuler.net/problem=310"
__problem_description__ = "Alice and Bob play the game Nim Square. Nim Square is just like " \
                          "ordinary three-heap normal play Nim, but the players may only remove " \
                          "a square number of stones from a heap. The number of stones in the " \
                          "three heaps is represented by the ordered triple (a,b,c). If " \
                          "0≤a≤b≤c≤29 then the number of losing positions for the next player is " \
                          "1160. Find the number of losing positions for the next player if " \
                          "0≤a≤b≤c≤100 000."

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

