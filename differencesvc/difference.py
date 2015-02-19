import math

def sum_squares(n):
    """returns sum(1^2, ..., n^2)"""
    return sum([ i * i for i in xrange(1, n + 1) ])

def square_sums(n):
    """returns sum([1, ..., n])^2"""
    return sum([ i for i in xrange(1, n + 1) ]) ** 2

def difference(n):
    """returns difference between sum_squares(n) and square_sums(n)"""
    return abs(square_sums(n) - sum_squares(n))

