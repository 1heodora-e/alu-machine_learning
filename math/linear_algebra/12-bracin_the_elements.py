#!/usr/bin/env python3
"""Performs element-wise addition, subtraction, multiplication,
and division of two arrays.
"""


def np_elementwise(mat1, mat2):
    """Returns a tuple: (mat1 + mat2, mat1 - mat2, mat1 * mat2, mat1 / mat2)."""
    return (mat1 + mat2,
            mat1 - mat2,
            mat1 * mat2,
            mat1 / mat2)
