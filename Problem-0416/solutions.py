
__problem_title__ = "A frog's trip"
__problem_url___ = "https://projecteuler.net/problem=416"
__problem_description__ = "A row of squares contains a frog in the leftmost square. By " \
                          "successive jumps the frog goes to the rightmost square and then back " \
                          "to the leftmost square. On the outward trip he jumps one, two or " \
                          "three squares to the right, and on the homeward trip he jumps to the " \
                          "left in a similar manner. He cannot jump outside the squares. He " \
                          "repeats the round-trip travel times. Let F( , ) be the number of the " \
                          "ways the frog can travel so that at most one square remains " \
                          "unvisited. For example, F(1, 3) = 4, F(1, 4) = 15, F(1, 5) = 46, F(2, " \
                          "3) = 16 and F(2, 100) mod 10 = 429619151. Find the last 9 digits of " \
                          "F(10, 10 )."

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

