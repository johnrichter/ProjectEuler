
__problem_title__ = "Investigating Gaussian Integers"
__problem_url___ = "https://projecteuler.net/problem=153"
__problem_description__ = "As we all know the equation =-1 has no solutions for real . If we " \
                          "however introduce the imaginary number this equation has two " \
                          "solutions: and . If we go a step further the equation ( -3) =-4 has " \
                          "two complex solutions: =3+2 and =3-2 . =3+2 and =3-2 are called each " \
                          "others' complex conjugate. Numbers of the form + are called complex " \
                          "numbers. In general + and − are each other's complex conjugate. A " \
                          "Gaussian Integer is a complex number + such that both and are " \
                          "integers. The regular integers are also Gaussian integers (with =0). " \
                          "To distinguish them from Gaussian integers with ≠ 0 we call such " \
                          "integers "rational integers." A Gaussian integer is called a divisor " \
                          "of a rational integer if the result is also a Gaussian integer. If " \
                          "for example we divide 5 by 1+2 we can simplify in the following " \
                          "manner: Multiply numerator and denominator by the complex conjugate " \
                          "of 1+2 : 1−2 . The result is . So 1+2 is a divisor of 5. Note that 1+ " \
                          "is not a divisor of 5 because . Note also that if the Gaussian " \
                          "Integer ( + ) is a divisor of a rational integer , then its complex " \
                          "conjugate ( − ) is also a divisor of . In fact, 5 has six divisors " \
                          "such that the real part is positive: {1, 1 + 2 , 1 − 2 , 2 + , 2 − , " \
                          "5}. The following is a table of all of the divisors for the first " \
                          "five positive rational integers: For divisors with positive real " \
                          "parts, then, we have: . For 1 ≤ ≤ 10 , ∑ s( )=17924657155. What is ∑ " \
                          "s( ) for 1 ≤ ≤ 10 ?"

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

