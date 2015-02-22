
__problem_title__ = "Digital root clocks"
__problem_url___ = "https://projecteuler.net/problem=315"
__problem_description__ = "Sam and Max are asked to transform two digital clocks into two " \
                          ""digital root" clocks. A digital root clock is a digital clock that " \
                          "calculates digital roots step by step. When a clock is fed a number, " \
                          "it will show it and then it will start the calculation, showing all " \
                          "the intermediate values until it gets to the result. For example, if " \
                          "the clock is fed the number 137, it will show: " " → " " → " " and " \
                          "then it will go black, waiting for the next number. Every digital " \
                          "number consists of some light segments: three horizontal (top, " \
                          "middle, bottom) and four vertical (top-left, top-right, bottom-left, " \
                          "bottom-right). Number " " is made of vertical top-right and " \
                          "bottom-right, number " " is made by middle horizontal and vertical " \
                          "top-left, top-right and bottom-right. Number " " lights them all. The " \
                          "clocks consume energy only when segments are turned on/off. To turn " \
                          "on a " " will cost 5 transitions, while a " " will cost only 4 " \
                          "transitions. Sam and Max built two different clocks. Sam's clock is " \
                          "fed e.g. number 137: the clock shows " ", then the panel is turned " \
                          "off, then the next number (" ") is turned on, then the panel is " \
                          "turned off again and finally the last number (" ") is turned on and, " \
                          "after some time, off. For the example, with number 137, Sam's clock " \
                          "requires: Max's clock works differently. Instead of turning off the " \
                          "whole panel, it is smart enough to turn off only those segments that " \
                          "won't be needed for the next number. For number 137, Max's clock " \
                          "requires: Of course, Max's clock consumes less power than Sam's one. " \
                          "The two clocks are fed all the prime numbers between A = 10 and B = " \
                          "2×10 . Find the difference between the total number of transitions " \
                          "needed by Sam's clock and that needed by Max's one."

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

