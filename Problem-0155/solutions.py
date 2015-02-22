
__problem_title__ = "Counting Capacitor Circuits"
__problem_url___ = "https://projecteuler.net/problem=155"
__problem_description__ = "An electric circuit uses exclusively identical capacitors of the same " \
                          "value C. The capacitors can be connected in series or in parallel to " \
                          "form sub-units, which can then be connected in series or in parallel " \
                          "with other capacitors or other sub-units to form larger sub-units, " \
                          "and so on up to a final circuit. Using this simple procedure and up " \
                          "to identical capacitors, we can make circuits having a range of " \
                          "different total capacitances. For example, using up to =3 capacitors " \
                          "of 60 F each, we can obtain the following 7 distinct total " \
                          "capacitance values: If we denote by ( ) the number of distinct total " \
                          "capacitance values we can obtain when using up to equal-valued " \
                          "capacitors and the simple procedure described above, we have: (1)=1, " \
                          "(2)=3, (3)=7 ... Find (18). When connecting capacitors C , C etc in " \
                          "parallel, the total capacitance is C = C + C +..., whereas when " \
                          "connecting them in series, the overall capacitance is given by:"

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

