
__problem_title__ = "Connectedness of a network"
__problem_url___ = "https://projecteuler.net/problem=186"
__problem_description__ = "Here are the records from a busy telephone system with one million " \
                          "users: The telephone number of the caller and the called number in " \
                          "record n are Caller(n) = S and Called(n) = S where S come from the " \
                          ""Lagged Fibonacci Generator": For 1 ≤ k ≤ 55, S = [100003 - 200003k + " \
                          "300007k ] (modulo 1000000) For 56 ≤ k, S = [S + S ] (modulo 1000000) " \
                          "If Caller(n) = Called(n) then the user is assumed to have misdialled " \
                          "and the call fails; otherwise the call is successful. From the start " \
                          "of the records, we say that any pair of users X and Y are friends if " \
                          "X calls Y or vice-versa. Similarly, X is a friend of a friend of Z if " \
                          "X is a friend of Y and Y is a friend of Z; and so on for longer " \
                          "chains. The Prime Minister's phone number is 524287. After how many " \
                          "successful calls, not counting misdials, will 99% of the users " \
                          "(including the PM) be a friend, or a friend of a friend etc., of the " \
                          "Prime Minister?"

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

