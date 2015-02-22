
__problem_title__ = "Triangles with non rational sides and integral area"
__problem_url___ = "https://projecteuler.net/problem=390"
__problem_description__ = "Consider the triangle with sides √5, √65 and √68. It can be shown " \
                          "that this triangle has area 9. S(n) is the sum of the areas of all " \
                          "triangles with sides √(1+b ), √(1+c ) and √(b +c ) (for positive " \
                          "integers b and c ) that have an integral area not exceeding n. The " \
                          "example triangle has b=2 and c=8. S(10 )=18018206. Find S(10 )."

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

