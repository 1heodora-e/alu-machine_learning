#!/usr/bin/env python3
"""
Module for calculating the definiteness of a given matrix.
"""
import numpy as np


def definiteness(matrix):
    """
    Calculate the definiteness of a given matrix.

    Args:
        matrix: A numpy.ndarray of shape (n, n) whose definiteness should be
                calculated

    Returns:
        String indicating the definiteness: 'Positive definite',
        'Positive semi-definite', 'Negative semi-definite',
        'Negative definite', 'Indefinite', or None if matrix is invalid

    Raises:
        TypeError: If matrix is not a numpy.ndarray
    """
    # Check if matrix is a numpy.ndarray
    if not isinstance(matrix, np.ndarray):
        raise TypeError("matrix must be a numpy.ndarray")

    # Check if matrix is empty
    if matrix.size == 0:
        return None

    # Check if matrix is 2D and square
    if len(matrix.shape) != 2 or matrix.shape[0] != matrix.shape[1]:
        return None

    # Check if matrix is symmetric (required for definiteness)
    if not np.allclose(matrix, matrix.T):
        return None

    # Calculate eigenvalues
    try:
        eigenvalues = np.linalg.eigvals(matrix)
    except np.linalg.LinAlgError:
        return None

    # Check for complex eigenvalues (shouldn't happen for symmetric matrices)
    if np.any(np.iscomplex(eigenvalues)):
        return None

    # Convert to real values (in case of tiny imaginary parts due to precision)
    eigenvalues = np.real(eigenvalues)

    # Define tolerance for zero comparison
    tolerance = 1e-8

    # Count positive, negative, and zero eigenvalues
    positive_count = np.sum(eigenvalues > tolerance)
    negative_count = np.sum(eigenvalues < -tolerance)
    zero_count = np.sum(np.abs(eigenvalues) <= tolerance)

    n = len(eigenvalues)

    # Determine definiteness based on eigenvalues
    if positive_count == n:
        # All eigenvalues are positive
        return "Positive definite"
    elif positive_count > 0 and negative_count == 0 and zero_count > 0:
        # Some positive, some zero, no negative
        return "Positive semi-definite"
    elif negative_count == n:
        # All eigenvalues are negative
        return "Negative definite"
    elif negative_count > 0 and positive_count == 0 and zero_count > 0:
        # Some negative, some zero, no positive
        return "Negative semi-definite"
    elif positive_count > 0 and negative_count > 0:
        # Both positive and negative eigenvalues
        return "Indefinite"
    else:
        return None
