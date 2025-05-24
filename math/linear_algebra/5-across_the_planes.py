#!/usr/bin/env python3
"""This module defines a function that adds two 2D matrices element-wise.
"""

def add_matrices2D(mat1, mat2):
    """Adds two 2D matrices element-wise and returns the result."""
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return None
    return [
        [mat1[i][j] + mat2[i][j] for j in range(len(mat1[0]))]
        for i in range(len(mat1))
    ]
