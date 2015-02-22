
__problem_title__ = "Squarefree Fibonacci Numbers"
__problem_url___ = "https://projecteuler.net/problem=399"
__problem_description__ = "The first 15 fibonacci numbers are: " \
                          "1,1,2,3,5,8,13,21,34,55,89,144,233,377,610. It can be seen that 8 and " \
                          "144 are not squarefree: 8 is divisible by 4 and 144 is divisible by 4 " \
                          "and by 9. So the first 13 squarefree fibonacci numbers are: " \
                          "1,1,2,3,5,13,21,34,55,89,233,377 and 610. The 200th squarefree " \
                          "fibonacci number is: " \
                          "971183874599339129547649988289594072811608739584170445. The last " \
                          "sixteen digits of this number are: 1608739584170445 and in scientific " \
                          "notation this number can be written as 9.7e53. Find the 100 000 000th " \
                          "squarefree fibonacci number. Give as your answer its last sixteen " \
                          "digits followed by a comma followed by the number in scientific " \
                          "notation (rounded to one digit after the decimal point). For the " \
                          "200th squarefree number the answer would have been: " \
                          "1608739584170445,9.7e53"

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

