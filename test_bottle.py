import pytest
from bottle import Bottle

class TestBottle:

    @pytest.fixture
    def bottle(self):
        return Bottle('Blue', 1000)

    def test_color(self, bottle):
        assert bottle.color == 'Blue'

    def test_capacity(self, bottle):
        assert bottle.capacity == 1000

    def test_initial_quantity(self, bottle):
        assert bottle.quantity_available == 0.0

    def test_fill_bottle(self, bottle):
        bottle.fill_bottle()
        assert bottle.quantity_available == 1000

    def test_drink_water_available(self, bottle):
        bottle.fill_bottle()
        amount = bottle.drink_water(500)
        assert amount == 500
        assert bottle.quantity_available == 500

    def test_drink_water_not_available(self, bottle):
        bottle.fill_bottle()
        amount = bottle.drink_water(1500)
        assert amount == 1000  # Max available amount
        assert bottle.quantity_available == 0

    def test_drink_water_partial_available(self, bottle):
        bottle.fill_bottle()
        bottle.drink_water(500)
        amount = bottle.drink_water(700)
        assert amount == 500  # Remaining available amount
        assert bottle.quantity_available == 0

    def test_open_and_close_bottle(self, bottle):
        bottle.open_bottle()
        assert True  # Add appropriate assertions
        bottle.close_the_bottle()
        assert True  # Add appropriate assertions