#!/usr/bin/env python3
"""This module defines a function that adds two arrays element-wise.
"""

def add_arrays(arr1, arr2):
    """Adds two arrays element-wise and returns the result."""
    if len(arr1) != len(arr2):
        return None
    return [a + b for a, b in zip(arr1, arr2)]
