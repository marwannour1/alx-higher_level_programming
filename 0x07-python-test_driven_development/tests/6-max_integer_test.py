#!/usr/bin/python3
"""Unittest for max_integer([..]) function"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Class for unittests for ``max_integer`` function"""

    def test_no_arg(self):
        """Test with no arguments passed"""
        self.assertEqual(max_integer(), None)
    
    def test_empty_list(self):
        """Test with empty list"""
        self.assertEqual(max_integer([]), None)

    def test_one_element(self):
        """Test with one element in list"""
        self.assertEqual(max_integer([1]), 1)
    
    def test_max_at_end(self):
        """Test with max at end of list"""
        self.assertEqual(max_integer([1, 2, 3]), 3)
    
    def test_max_at_beginning(self):
        """Test with max at beginning of list"""
        self.assertEqual(max_integer([3, 2, 1]), 3)
    
    def test_max_in_middle(self):
        """Test with max in middle of list"""
        self.assertEqual(max_integer([1, 3, 2]), 3)

    def test_max_negative(self):
        """Test with max negative"""
        self.assertEqual(max_integer([-1, -2, -3]), -1)
    
    def test_max_float(self):
        """Test with max float"""
        self.assertEqual(max_integer([1.1, 2.2, 3.3]), 3.3)
    
    def test_max_string(self):
        """Test with max string"""
        self.assertEqual(max_integer(["a", "b", "c"]), "c")
    
    def test_max_none(self):
        """Test with max None"""
        self.assertEqual(max_integer([None, None, None]), None)
    
    def test_max_mixed(self):
        """Test with max mixed"""
        self.assertEqual(max_integer([1, 2.2, 3]), 3)

    def test_max_inf(self):
        """Test with max inf"""
        self.assertEqual(max_integer([1, float('inf'), 3]), float('inf'))
    
    def test_max_nan(self):
        """Test with nan"""
        with self.assertRaises(TypeError):
            max_integer([1, float('nan'), 3])
    
    def test_int(self):
        """Test with int"""
        with self.assertRaises(TypeError):
            max_integer(1)
    
    def test_str(self):
        """Test with str"""
        with self.assertRaises(TypeError):
            max_integer("str")

if __name__ == '__main__':
    unittest.main()
