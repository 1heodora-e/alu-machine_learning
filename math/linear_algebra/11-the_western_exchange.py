#!/usr/bin/env python3
"""This module provides a function to transpose a 2D matrix."""

def np_transpose(matrix):
    """Returns the transpose of a 2D matrix."""
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
