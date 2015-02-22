
__problem_title__ = "Passcode derivation"
__problem_url___ = "https://projecteuler.net/problem=79"
__problem_description__ = "A common security method used for online banking is to ask the user " \
                          "for three random characters from a passcode. For example, if the " \
                          "passcode was 531278, they may ask for the 2nd, 3rd, and 5th " \
                          "characters; the expected reply would be: 317. The text file, , " \
                          "contains fifty successful login attempts. Given that the three " \
                          "characters are always asked for in order, analyse the file so as to " \
                          "determine the shortest possible secret passcode of unknown length."

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

