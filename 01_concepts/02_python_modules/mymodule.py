# this is my module for mathematical operations

"""

A lightweight algebra utility module providing
core mathematical operations in a centralized class.
Designed for reusability, clarity, and extensibility.
"""


class BasicAlgebra:
    """fundamental algebra operations."""

    @staticmethod
    def add(a, b):
        """Return the sum of two numbers."""
        return a + b

    @staticmethod
    def subtract(a, b):
        """Return the difference between two numbers."""
        return a - b

    @staticmethod
    def multiply(a, b):
        """Return the product of two numbers."""
        return a * b

    @staticmethod
    def divide(a, b):
        """
        Return the quotient of two numbers.
        Raises ZeroDivisionError for invalid division.
        """
        if b == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return a / b

    @staticmethod
    def power(base, exponent):
        """Return base raised to the given exponent."""
        return base**exponent

    @staticmethod
    def linear_equation(m, x, c):
        """
        Solve a linear equation of the form:
        y = mx + c
        """
        return m * x + c

    @staticmethod
    def quadratic_equation(a, b, c, x):
        """
        Evaluate a quadratic expression:
        ax² + bx + c
        """
        return a * x**2 + b * x + c
