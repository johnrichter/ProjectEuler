
__problem_title__ = "The Last Question"
__problem_url___ = "https://projecteuler.net/problem=480"
__problem_description__ = "Consider all the words which can be formed by selecting letters, in " \
                          "any order, from the phrase: Suppose those with 15 letters or less are " \
                          "listed in and numbered sequentially starting at 1. The list would " \
                          "include: Define ( ) as the position of the word . Define ( ) as the " \
                          "word in position . We can see that ( ) and ( ) are inverses: ( ( )) = " \
                          "and ( ( )) = . Examples: Find ( (legionary) + (calorimeters) - " \
                          "(annihilate) + (orchestrated) - (fluttering)). Give your answer using " \
                          "lowercase characters (no punctuation or space)."

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

