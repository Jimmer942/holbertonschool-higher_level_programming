#!/usr/bin/python3
""" Test Rectangle class """
import unittest

from unittest import TestCase
from models.rectangle import Rectangle


class Rectangle(unittest.TestCase):

    def test_id(self):
        """ Test if the id change and it's counting"""
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 12)

    def test_Validate_attributes (self):
        """ Raises the errors """
        with self.assertRaises(TypeError):
            r1 = Rectangle(10, "2")
        with self.assertRaises(TypeError):
            r1 = Rectangle("10", 2)
