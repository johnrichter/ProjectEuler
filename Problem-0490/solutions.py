
__problem_title__ = "Jumping frog"
__problem_url___ = "https://projecteuler.net/problem=490"
__problem_description__ = "There are stones in a pond, numbered 1 to . Consecutive stones are " \
                          "spaced one unit apart. A frog sits on stone 1. He wishes to visit " \
                          "each stone exactly once, stopping on stone . However, he can only " \
                          "jump from one stone to another if they are at most 3 units apart. In " \
                          "other words, from stone , he can reach a stone if 1 ≤ ≤ and is in the " \
                          "set { -3, -2, -1, +1, +2, +3}. Let f( ) be the number of ways he can " \
                          "do this. For example, f(6) = 14, as shown below: 1 → 2 → 3 → 4 → 5 → " \
                          "6 1 → 2 → 3 → 5 → 4 → 6 1 → 2 → 4 → 3 → 5 → 6 1 → 2 → 4 → 5 → 3 → 6 1 " \
                          "→ 2 → 5 → 3 → 4 → 6 1 → 2 → 5 → 4 → 3 → 6 1 → 3 → 2 → 4 → 5 → 6 1 → 3 " \
                          "→ 2 → 5 → 4 → 6 1 → 3 → 4 → 2 → 5 → 6 1 → 3 → 5 → 2 → 4 → 6 1 → 4 → 2 " \
                          "→ 3 → 5 → 6 1 → 4 → 2 → 5 → 3 → 6 1 → 4 → 3 → 2 → 5 → 6 1 → 4 → 5 → 2 " \
                          "→ 3 → 6 Other examples are f(10) = 254 and f(40) = 1439682432976. Let " \
                          "S( ) = ∑ f( ) for 1 ≤ ≤ . Examples: S(10) = 18230635 S(20) = " \
                          "104207881192114219 S(1 000) mod 10 = 225031475 S(1 000 000) mod 10 = " \
                          "363486179 Find S(10 ) mod 10 ."

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

