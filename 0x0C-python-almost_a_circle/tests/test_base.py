#!/usr/bin/python3
"""
test for class base
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """
    class for testing
    """
    def test_for_id(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_for_id_twice(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_for_id_third(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def test_for_id_with_arg(self):
        b = Base(12)
        self.assertEqual(b.id, 12)

    def test_for_id_with_none(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_for_id_mix(self):
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)

    def test_for_change_value(self):
        b = Base(12)
        b.id = 15
        self.assertEqual(15, b.id)

    def test_base_with_two_arg(self):
        with self.assertRaises(TypeError):
            Base(1, 1)


if __name__ == "__main__":
    unittest.main()
