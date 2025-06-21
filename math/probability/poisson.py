#!/usr/bin/env python3
"""Poisson distribution module"""


class Poisson:
    """Represents a Poisson distribution"""

    def __init__(self, data=None, lambtha=1.):
        """
        Initializes the Poisson distribution

        Args:
            data (list): data to estimate the distribution
            lambtha (float): expected number of occurrences

        Raises:
            TypeError: if data is not a list
            ValueError: if data has fewer than 2 values
            ValueError: if lambtha is not a positive value
        """
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = float(sum(data) / len(data))

    def pmf(self, k):
        """
        Calculates the PMF for a given number of successes

        Args:
            k (int): number of successes

        Returns:
            float: PMF value for k
        """
        if not isinstance(k, int):
            k = int(k)
        if k < 0:
            return 0

        # Approximation of e (no imports allowed)
        e = 2.7182818285

        # k! (factorial) calculation
        factorial = 1
        for i in range(1, k + 1):
            factorial *= i

        # PMF formula: P(k) = (λ^k * e^-λ) / k!
        return (self.lambtha ** k) * (e ** -self.lambtha) / factorial
