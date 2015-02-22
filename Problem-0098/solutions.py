
__problem_title__ = "Anagramic squares"
__problem_url___ = "https://projecteuler.net/problem=98"
__problem_description__ = "By replacing each of the letters in the word CARE with 1, 2, 9, and 6 " \
                          "respectively, we form a square number: 1296 = 36 . What is remarkable " \
                          "is that, by using the same digital substitutions, the anagram, RACE, " \
                          "also forms a square number: 9216 = 96 . We shall call CARE (and RACE) " \
                          "a square anagram word pair and specify further that leading zeroes " \
                          "are not permitted, neither may a different letter have the same " \
                          "digital value as another letter. Using (right click and 'Save " \
                          "Link/Target As...'), a 16K text file containing nearly two-thousand " \
                          "common English words, find all the square anagram word pairs (a " \
                          "palindromic word is NOT considered to be an anagram of itself). What " \
                          "is the largest square number formed by any member of such a pair? " \
                          "NOTE: All anagrams formed must be contained in the given text file."

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

