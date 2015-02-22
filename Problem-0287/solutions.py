
__problem_title__ = "Quadtree encoding (a simple compression algorithm)"
__problem_url___ = "https://projecteuler.net/problem=287"
__problem_description__ = "The quadtree encoding allows us to describe a 2 ×2 black and white " \
                          "image as a sequence of bits (0 and 1). Those sequences are to be read " \
                          "from left to right like this: Consider the following 4×4 image " \
                          "(colored marks denote places where a split can occur): This image can " \
                          "be described by several sequences, for example : " 10101010 " \
                          "1011111011 10101010", of length 30, or " 10 101111101110", of length " \
                          "16, which is the minimal sequence for this image. For a positive " \
                          "integer , define as the 2 ×2 image with the following coloring " \
                          "scheme: What is the length of the minimal sequence describing ?"

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

