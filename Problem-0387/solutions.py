
__problem_title__ = "Harshad Numbers"
__problem_url___ = "https://projecteuler.net/problem=387"
__problem_description__ = "A is a number that is divisible by the sum of its digits. 201 is a " \
                          "Harshad number because it is divisible by 3 (the sum of its digits.) " \
                          "When we truncate the last digit from 201, we get 20, which is a " \
                          "Harshad number. When we truncate the last digit from 20, we get 2, " \
                          "which is also a Harshad number. Let's call a Harshad number that, " \
                          "while recursively truncating the last digit, always results in a " \
                          "Harshad number a Also: 201/3=67 which is prime. Let's call a Harshad " \
                          "number that, when divided by the sum of its digits, results in a " \
                          "prime a . Now take the number 2011 which is prime. When we truncate " \
                          "the last digit from it we get 201, a strong Harshad number that is " \
                          "also right truncatable. Let's call such primes . You are given that " \
                          "the sum of the strong, right truncatable Harshad primes less than " \
                          "10000 is 90619. Find the sum of the strong, right truncatable Harshad " \
                          "primes less than 10 ."

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

