
__problem_title__ = "Perfect right-angled triangles"
__problem_url___ = "https://projecteuler.net/problem=218"
__problem_description__ = "Consider the right angled triangle with sides a=7, b=24 and c=25. The " \
                          "area of this triangle is 84, which is divisible by the perfect " \
                          "numbers 6 and 28. Moreover it is a primitive right angled triangle as " \
                          "gcd(a,b)=1 and gcd(b,c)=1. Also c is a perfect square. We will call a " \
                          "right angled triangle perfect if -it is a primitive right angled " \
                          "triangle -its hypotenuse is a perfect square We will call a right " \
                          "angled triangle super-perfect if -it is a perfect right angled " \
                          "triangle and -its area is a multiple of the perfect numbers 6 and 28. " \
                          "How many perfect right-angled triangles with c≤10 exist that are not " \
                          "super-perfect?"

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

