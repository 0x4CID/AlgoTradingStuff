import numpy as np
from scipy.stats import norm

N = norm.cdf

def call(S, K, R, T, V):
    """
    :param S: Underlying stock price
    :param K: Contract strike price
    :param R: Risk-Free rate
    :param T: Time till maturity
    :param V: Volatility
    :return: Call value
    """
    d1 = (1.0 / (V * np.sqrt(T))) * (np.log(S / K) + (R + 0.5 * V ** 2.0) * T)
    d2 = d1 - (V * np.sqrt(T))

    return N(d1) * S - N(d2) * K * np.exp(-R * T)

def put(S, K, R, T, V):
    """
    :param S: Underlying stock price
    :param K: Contract strike price
    :param R: Risk-Free rate
    :param T: Time till maturity
    :param V: Volatility
    :return: Put value
    """

    d1 = (1.0 / (V * np.sqrt(T))) * (np.log(S / K) + (R + 0.5 * V ** 2.0) * T)
    d2 = d1 - (V * np.sqrt(T))
    return N(-d2) * K * np.exp(-R * T) - N(-d1) * S
