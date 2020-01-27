import math

def get_q(Un, n, Uo):
    return 10**(Un/(U0*n))

def get_n(Un, U0, q):
    return (Un/(U0*math.log(q)))

def get_U0(Un, n, q):
    return Un/(n*math.log(q))

def get_Un(U0, q, n):
    return U0*q**n
