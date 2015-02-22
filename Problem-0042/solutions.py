
__problem_title__ = "Coded triangle numbers"
__problem_url___ = "https://projecteuler.net/problem=42"
__problem_description__ = "The term of the sequence of triangle numbers is given by, = ½ ( +1); " \
                          "so the first ten triangle numbers are: 1, 3, 6, 10, 15, 21, 28, 36, " \
                          "45, 55, ... By converting each letter in a word to a number " \
                          "corresponding to its alphabetical position and adding these values we " \
                          "form a word value. For example, the word value for SKY is 19 + 11 + " \
                          "25 = 55 = . If the word value is a triangle number then we shall call " \
                          "the word a triangle word. Using (right click and 'Save Link/Target " \
                          "As...'), a 16K text file containing nearly two-thousand common " \
                          "English words, how many are triangle words?"

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

