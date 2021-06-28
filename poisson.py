from math import exp
from operator import mul
from functools import reduce


class poisson:
    """
    It is a distribution related to the probabilities of events which are extremely rare, but which have a
    large number of independent opportunities for occurence.
    """

    def __init__(self, m=None):
            self.m = m

    def fact_(self, r):
        return reduce(mul, list(range(1, r + 1)))

    def p_r(self, r):
        if r != 0:
            return (self.m ** r) * exp(-1 * self.m) / self.fact_(r)
        else:
            return exp(-1 * self.m)

    def p_le_r(self, r):
        prob = 0
        for i in list(range(0,r+1)):
            prob = prob + self.p_r(i)
        return prob

    def p_l_r(self, r):
        prob = 0
        for i in list(range(0,r)):
            prob = prob + self.p_r(i)
        return prob

    def p_ge_r(self, r):
        return 1-self.p_l_r(r)

    def p_g_r(self,r):
        return 1-self.p_le_r(r)