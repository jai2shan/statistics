from operator import mul
from functools import reduce

class binomial_dist:
    """
    Binomial distribution is concerned with trials of a repetitive nature in which only the occurence or non occurence,
    success or failure, acceptance or rejection, yes or no of a particular event of interest.

    If we perform series of independent trials such that for each trail p is the probability of success and q is that
    of a failure, then probability of r successes in a series of n trials is given by (n,C,r)*(p^r)*(q^n-r), where
    r takes any integral value from 0 to n.

    Attributes:
    -----------
        n : number of trials
        p : probability of success
        q : probability of failure
        r : number of successes

    """

    def __init__(self, n, p, q):
        self.n = n
        self.p = p
        self.q = q
        self.n_fact = reduce(mul, list(range(1,self.n+1)))

    def nCr(self,r):
        """
        nCr - gives nCr value
        :param r:
        :return: gives nCr value
        """
        prod = 1
        if self.n!=r:
            n_r = reduce(mul, list(range(1,self.n-r+1)))
        else:
            n_r = 1
        if r !=0:
            r_fact = reduce(mul, list(range(1,r+1)))
        else:
            r_fact = 1
        return self.n_fact/(r_fact*n_r)

    def p_le_r(self, r):
        """
        p_le_r - probability of less than or equal to r successes
        :param r:
        :return:
        """
        prob = 0
        for i in list(range(0,r+1)):
            prob = prob+ self.nCr(i)*(self.p**i)*(self.q**(self.n-i))
        return prob

    def p_l_r(self, r):
        """
        p_l_r - probability of less than r successes
        :param r:
        :return:
        """
        prob = 0
        for i in list(range(0, r)):
            prob = prob + self.nCr(i) * (self.p ** i) * (self.q ** (self.n - i))
        return prob

    def p_r(self, r):
        """
        p_r - probability of r successes
        :param r:
        :return: probability of r successes
        """
        return self.nCr(r) * (self.p ** r) * (self.q ** (self.n - r))

    def p_ge_r(self,r):
        """
        p_ge_r - probability of greater than or equal to r successes
        :param r:
        :return:
        """
        return 1-self.p_l_r(r)

    def p_g_r(self,r):
        """
        p_l_r - probability of greater than r successes
        :param r:
        :return:
        """
        return 1-self.p_le_r(r)


if __name__ == "__main__":
    my_prob = binomial_dist(20,0.1,0.9)
    print(my_prob.p_ge_r(3))



