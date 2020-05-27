"""
Unit tests for the calculator library.
"""

import calculator


class TestCalculator:

    def test_adition(self):
        assert 5 == calculator.add(2, 3)

    def test_substraction(self):
        assert 2 == calculator.subtract(4, 2)
