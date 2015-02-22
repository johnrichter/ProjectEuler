
__problem_title__ = "Roman numerals"
__problem_url___ = "https://projecteuler.net/problem=89"
__problem_description__ = "For a number written in Roman numerals to be considered valid there " \
                          "are basic rules which must be followed. Even though the rules allow " \
                          "some numbers to be expressed in more than one way there is always a " \
                          ""best" way of writing a particular number. For example, it would " \
                          "appear that there are at least six ways of writing the number " \
                          "sixteen: IIIIIIIIIIIIIIII VIIIIIIIIIII VVIIIIII XIIIIII VVVI XVI " \
                          "However, according to the rules only and are valid, and the last " \
                          "example is considered to be the most efficient, as it uses the least " \
                          "number of numerals. The 11K text file, (right click and 'Save " \
                          "Link/Target As...'), contains one thousand numbers written in valid, " \
                          "but not necessarily minimal, Roman numerals; see for the definitive " \
                          "rules for this problem. Find the number of characters saved by " \
                          "writing each of these in their minimal form. Note: You can assume " \
                          "that all the Roman numerals in the file contain no more than four " \
                          "consecutive identical units."

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

