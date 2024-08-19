"""
Implements a bottle
"""


class Bottle:
    """
    class representing a bottle

    Attributes
    ----------
    _quantity_available: float
    _color: str
    _capacity: float

    """

    def __init__(self, color, capacity):
        """
        constructor with color and capacity
        :param color:
        :param capacity:
        """
        self._quantity_available = 0.0  # 0.0 da float
        self._color = color
        self._capacity = capacity

    @property
    def color(self):
        """
        Gets the color of the bottle.
        :return: color(str)
        """
        return self._color

    @property
    def quantity_available(self):
        """
        Get the available quantity.
        :return: quantity_available(float)
        """
        return self._quantity_available

    @property
    def capacity(self):
        """
        Gets the capacity.
        :return: capacity(float)
        """
        return self._capacity

    def open_bottle(self):
        """
        Empty method.
        """
        return

    def close_the_bottle(self):
        """
        Empty method.
        """
        return

    def fill_bottle(self):
        """
        Fill the bottle to capacity
        """
        self._quantity_available = self._capacity

    def get_liquid(self, amount):
        """
        Returns the specified amount of liquid if available.
        Otherwise, returns the available quantity.

            :param: amount (float): the requested amount
            :return: amount(float)
        """
        if amount > self._quantity_available:
            amount = self._quantity_available
            self._quantity_available = 0.0
        else:
            self._quantity_available -= amount
        return amount
