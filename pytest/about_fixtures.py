#!/usr/bin/env python

import pytest


class Fruit:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name


# Test fixture is defined by the decorator: @pytest.fixture
@pytest.fixture
def my_fruit():
    return Fruit("apple")


@pytest.fixture
def fruit_basket(my_fruit):
    return [Fruit("banana"), my_fruit]


# Fixtures can be used in the test
def test_my_fruit_in_basket(my_fruit, fruit_basket):
    assert my_fruit in fruit_basket
