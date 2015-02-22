
__problem_title__ = "Mixtures"
__problem_url___ = "https://projecteuler.net/problem=478"
__problem_description__ = "Let us consider of three substances: , and . A mixture can be " \
                          "described by a ratio of the amounts of , , and in it, i.e., ( : : ). " \
                          "For example, a mixture described by the ratio (2 : 3 : 5) contains " \
                          "20% , 30% and 50% . For the purposes of this problem, we cannot " \
                          "separate the individual components from a mixture. However, we can " \
                          "combine different amounts of different mixtures to form mixtures with " \
                          "new ratios. For example, say we have three mixtures with ratios (3 : " \
                          "0 : 2), (3 : 6 : 11) and (3 : 3 : 4). By mixing 10 units of the " \
                          "first, 20 units of the second and 30 units of the third, we get a new " \
                          "mixture with ratio (6 : 5 : 9), since: (10· / + 20· / + 30· / : 10· / " \
                          "+ 20· / + 30· / : 10· / + 20· / + 30· / ) = (18 : 15 : 27) = (6 : 5 : " \
                          "9) However, with the same three mixtures, it is impossible to form " \
                          "the ratio (3 : 2 : 1), since the amount of is always less than the " \
                          "amount of . Let be a positive integer. Suppose that for every triple " \
                          "of integers ( , , ) with 0 ≤ , , ≤ and gcd( , , ) = 1, we have a " \
                          "mixture with ratio ( : : ). Let M( ) be the set of all such mixtures. " \
                          "For example, M(2) contains the 19 mixtures with the following ratios: " \
                          "{(0 : 0 : 1), (0 : 1 : 0), (0 : 1 : 1), (0 : 1 : 2), (0 : 2 : 1), (1 " \
                          ": 0 : 0), (1 : 0 : 1), (1 : 0 : 2), (1 : 1 : 0), (1 : 1 : 1), (1 : 1 " \
                          ": 2), (1 : 2 : 0), (1 : 2 : 1), (1 : 2 : 2), (2 : 0 : 1), (2 : 1 : " \
                          "0), (2 : 1 : 1), (2 : 1 : 2), (2 : 2 : 1)}. Let E( ) be the number of " \
                          "subsets of M( ) which can produce the mixture with ratio (1 : 1 : 1), " \
                          "i.e., the mixture with equal parts , and . We can verify that E(1) = " \
                          "103, E(2) = 520447, E(10) mod 11 = 82608406 and E(500) mod 11 = " \
                          "13801403. Find E(10 000 000) mod 11 ."

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

