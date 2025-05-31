#!/usr/bin/env python3
"""
Module for calculating the inverse of a given matrix.
"""


def inverse(matrix):
    """
    Calculate the inverse of a given matrix.

    Args:
        matrix: A list of lists representing a square matrix

    Returns:
        The inverse matrix as a list of lists, or None if matrix is singular

    Raises:
        TypeError: If matrix is not a list of lists
        ValueError: If matrix is not square or is empty
    """
    # Check if matrix is a list
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a list of lists")

    # Check if matrix is empty
    if len(matrix) == 0:
        raise ValueError("matrix must be a non-empty square matrix")

    # Check if matrix is a list of lists
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a list of lists")

    # Check if matrix is square
    n = len(matrix)
    for row in matrix:
        if len(row) != n:
            raise ValueError("matrix must be a non-empty square matrix")

    # Calculate determinant
    det = determinant(matrix)

    # Check if matrix is singular (determinant is 0)
    if det == 0:
        return None

    # Special case for 1x1 matrix
    if n == 1:
        return [[1 / matrix[0][0]]]

    # Calculate adjugate matrix
    adj_matrix = adjugate(matrix)

    # Calculate inverse by dividing adjugate by determinant
    inverse_matrix = []
    for i in range(n):
        inverse_row = []
        for j in range(n):
            inverse_row.append(adj_matrix[i][j] / det)
        inverse_matrix.append(inverse_row)

    return inverse_matrix


def adjugate(matrix):
    """
    Calculate the adjugate matrix of a given matrix.

    Args:
        matrix: A square matrix as a list of lists

    Returns:
        The adjugate matrix as a list of lists
    """
    n = len(matrix)

    # Special case for 1x1 matrix
    if n == 1:
        return [[1]]

    # Calculate cofactor matrix
    cofactor_matrix = []
    for i in range(n):
        cofactor_row = []
        for j in range(n):
            # Calculate minor by removing row i and column j
            minor = []
            for row_idx in range(n):
                if row_idx != i:
                    minor_row = []
                    for col_idx in range(n):
                        if col_idx != j:
                            minor_row.append(matrix[row_idx][col_idx])
                    minor.append(minor_row)

            # Calculate determinant of minor
            minor_det = determinant(minor)

            # Calculate cofactor with alternating signs
            cofactor = ((-1) ** (i + j)) * minor_det
            cofactor_row.append(cofactor)

        cofactor_matrix.append(cofactor_row)

    # Transpose the cofactor matrix to get the adjugate
    adjugate_matrix = []
    for j in range(n):
        adj_row = []
        for i in range(n):
            adj_row.append(cofactor_matrix[i][j])
        adjugate_matrix.append(adj_row)

    return adjugate_matrix


def determinant(matrix):
    """
    Calculate the determinant of a square matrix using recursive expansion.

    Args:
        matrix: A square matrix as a list of lists

    Returns:
        The determinant of the matrix
    """
    n = len(matrix)

    # Base case: 1x1 matrix
    if n == 1:
        return matrix[0][0]

    # Base case: 2x2 matrix
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    # Recursive case: expand along first row
    det = 0
    for j in range(n):
        # Create minor by removing first row and column j
        minor = []
        for i in range(1, n):
            minor_row = []
            for k in range(n):
                if k != j:
                    minor_row.append(matrix[i][k])
            minor.append(minor_row)

        # Add to determinant with alternating signs
        det += ((-1) ** j) * matrix[0][j] * determinant(minor)

    return det
