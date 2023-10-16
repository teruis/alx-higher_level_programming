#!/usr/bin/python3 
 """ 
 test for class rectangle 
 """ 
 import unittest 
 from models.base import Base 
 from models.rectangle import Rectangle 
  
  
 class Tese_rectangle(unittest.TestCase): 
     """ 
     testing class 
     """ 
     def test_for_id_twice(self): 
         r1 = Rectangle(10, 2) 
         r2 = Rectangle(2, 10) 
         self.assertEqual(r1.id, r2.id - 1) 
  
     def test_for_three_args(self): 
         r1 = Rectangle(1, 2, 3) 
         r2 = Rectangle(4, 5, 6) 
         self.assertEqual(r1.id, r2.id - 1) 
  
     def test_for_four_arg(self): 
         r1 = Rectangle(1, 2, 3, 4) 
         r2 = Rectangle(5, 6, 7, 8) 
         self.assertEqual(r1.id, r2.id - 1) 
  
     def test_for_id_arg(self): 
         r = Rectangle(1, 2, 3, 4, 5) 
         self.assertEqual(r.id, 5) 
  
     def test_for_width(self): 
         r = Rectangle(1, 2, 3, 4, 5) 
         self.assertEqual(r.width, 1) 
  
     def test_for_update_width(self): 
         r = Rectangle(1, 2, 3, 4, 5) 
         r.width = 6 
         self.assertEqual(r.width, 6) 
  
     def test_for_height(self): 
         r = Rectangle(1, 2, 3, 4, 5) 
         self.assertEqual(r.height, 2) 
  
     def test_for_update_height(self): 
         r = Rectangle(1, 2, 3, 4, 5) 
         r.height = 6 
         self.assertEqual(r.height, 6) 
  
     def test_for_x(self): 
         r = Rectangle(1, 2, 3, 4, 5) 
         self.assertEqual(r.x, 3) 
  
     def test_for_update_x(self): 
         r = Rectangle(1, 2, 3, 4, 5) 
         r.x = 6 
         self.assertEqual(r.x, 6) 
  
     def test_for_y(self): 
         r = Rectangle(1, 2, 3, 4, 5) 
         self.assertEqual(r.y, 4) 
  
     def test_for_update_y(self): 
         r = Rectangle(1, 2, 3, 4, 5) 
         r.y = 6 
         self.assertEqual(r.y, 6) 
  
     def test_for_no_arg(self): 
         with self.assertRaises(TypeError): 
             Rectangle() 
  
     def test_for_one_arg(self): 
         with self.assertRaises(TypeError): 
             Rectangle(1) 
  
     def test_for_more_than_five_arg(self): 
         with self.assertRaises(TypeError): 
             Rectangle(1, 2, 3, 4, 5, 6) 
  
     def test_for_width_with_None(self): 
         with self.assertRaisesRegex(TypeError, "width must be an integer"): 
             Rectangle(None, 1) 
  
     def test_for_width_with_string(self): 
         with self.assertRaisesRegex(TypeError, "width must be an integer"): 
             Rectangle("zomme", 1) 
  
     def test_for_width_with_float(self): 
         with self.assertRaisesRegex(TypeError, "width must be an integer"): 
             Rectangle(1.1, 1) 
  
     def test_for_width_with_dict(self): 
         with self.assertRaisesRegex(TypeError, "width must be an integer"): 
             Rectangle({"s": 1, "d": 2}, 1) 
  
     def test_for_width_with_bool(self): 
         with self.assertRaisesRegex(TypeError, "width must be an integer"): 
             Rectangle(True, 1) 
  
     def test_for_width_with_list(self): 
         with self.assertRaisesRegex(TypeError, "width must be an integer"): 
             Rectangle([1, 2, 3], 1) 
  
     def test_for_width_with_set(self): 
         with self.assertRaisesRegex(TypeError, "width must be an integer"): 
             Rectangle({1, 2}, 1) 
  
     def test_for_width_with_tuple(self): 
         with self.assertRaisesRegex(TypeError, "width must be an integer"): 
             Rectangle((1, 2), 1) 
  
     def test_for_width_with_negative(self): 
         with self.assertRaisesRegex(ValueError, "width must be > 0"): 
             Rectangle(-1, 1) 
  
     def test_for_width_with_zero(self): 
         with self.assertRaisesRegex(ValueError, "width must be > 0"): 
             Rectangle(0, 1) 
  
     def test_for_height_with_None(self): 
         with self.assertRaisesRegex(TypeError, "height must be an integer"): 
             Rectangle(1, None) 
  
     def test_for_height_with_string(self): 
         with self.assertRaisesRegex(TypeError, "height must be an integer"): 
             Rectangle(1, "zomme") 
  
     def test_for_height_with_float(self): 
         with self.assertRaisesRegex(TypeError, "height must be an integer"): 
             Rectangle(1, 1.1) 
  
     def test_for_height_with_dict(self): 
         with self.assertRaisesRegex(TypeError, "height must be an integer"): 
             Rectangle(1, {"s": 1, "d": 2}) 
  
     def test_for_height_with_bool(self): 
         with self.assertRaisesRegex(TypeError, "height must be an integer"): 
             Rectangle(1, True) 
  
     def test_for_height_with_list(self): 
         with self.assertRaisesRegex(TypeError, "height must be an integer"): 
             Rectangle(1, [1, 2, 3]) 
  
     def test_for_height_with_set(self): 
         with self.assertRaisesRegex(TypeError, "height must be an integer"): 
             Rectangle(1, {1, 2}) 
  
     def test_for_height_with_tuple(self): 
         with self.assertRaisesRegex(TypeError, "height must be an integer"): 
             Rectangle(1, (1, 2)) 
  
     def test_for_height_with_negative(self): 
         with self.assertRaisesRegex(ValueError, "height must be > 0"): 
             Rectangle(1, -1) 
  
     def test_for_height_with_zero(self): 
         with self.assertRaisesRegex(ValueError, "height must be > 0"): 
             Rectangle(1, 0) 
  
     def test_for_x_with_None(self): 
         with self.assertRaisesRegex(TypeError, "x must be an integer"): 
             Rectangle(1, 2, None) 
  
     def test_for_x_with_string(self): 
         with self.assertRaisesRegex(TypeError, "x must be an integer"): 
             Rectangle(1, 2, "zomme") 
  
     def test_for_x_with_float(self): 
         with self.assertRaisesRegex(TypeError, "x must be an integer"): 
             Rectangle(1, 2, 1.1) 
  
     def test_for_x_with_dict(self): 
         with self.assertRaisesRegex(TypeError, "x must be an integer"): 
             Rectangle(1, 2, {"s": 1, "d": 2}) 
  
     def test_for_x_with_bool(self): 
         with self.assertRaisesRegex(TypeError, "x must be an integer"): 
             Rectangle(1, 2, True) 
  
     def test_for_x_with_list(self): 
         with self.assertRaisesRegex(TypeError, "x must be an integer"): 
             Rectangle(1, 2, [1, 2, 3]) 
  
     def test_for_x_with_set(self): 
         with self.assertRaisesRegex(TypeError, "x must be an integer"): 
             Rectangle(1, 2, {1, 2}) 
  
     def test_for_x_with_tuple(self): 
         with self.assertRaisesRegex(TypeError, "x must be an integer"): 
             Rectangle(1, 1, (1, 2)) 
  
     def test_for_x_with_negative(self): 
         with self.assertRaisesRegex(ValueError, "x must be >= 0"): 
             Rectangle(1, 1, -1) 
  
     def test_for_y_with_None(self): 
         with self.assertRaisesRegex(TypeError, "y must be an integer"): 
             Rectangle(1, 2, 3, None) 
  
     def test_for_y_with_string(self): 
         with self.assertRaisesRegex(TypeError, "y must be an integer"): 
             Rectangle(1, 2, 3, "zomme") 
  
     def test_for_y_with_float(self): 
         with self.assertRaisesRegex(TypeError, "y must be an integer"): 
             Rectangle(1, 2, 3, 1.1) 
  
     def test_for_y_with_dict(self): 
         with self.assertRaisesRegex(TypeError, "y must be an integer"): 
             Rectangle(1, 2, 3, {"s": 1, "d": 2}) 
  
     def test_for_y_with_bool(self): 
         with self.assertRaisesRegex(TypeError, "y must be an integer"): 
             Rectangle(1, 2, 3, True) 
  
     def test_for_y_with_list(self): 
         with self.assertRaisesRegex(TypeError, "y must be an integer"): 
             Rectangle(1, 2, 3, [1, 2, 3]) 
  
     def test_for_y_with_set(self): 
         with self.assertRaisesRegex(TypeError, "y must be an integer"): 
             Rectangle(1, 2, 3, {1, 2}) 
  
     def test_for_y_with_tuple(self): 
         with self.assertRaisesRegex(TypeError, "y must be an integer"): 
             Rectangle(1, 1, 3, (1, 2)) 
  
     def test_for_y_with_negative(self): 
         with self.assertRaisesRegex(ValueError, "y must be >= 0"): 
             Rectangle(1, 1, 3, -1) 
  
     def test_for_width_and_height(self): 
         with self.assertRaisesRegex(TypeError, "width must be an integer"): 
             Rectangle("zomme", "hazem") 
  
     def test_for_width_and_x(self): 
         with self.assertRaisesRegex(TypeError, "width must be an integer"): 
             Rectangle("zoome", 1, "hazem") 
  
     def test_for_widht_and_y(self): 
         with self.assertRaisesRegex(TypeError, "width must be an integer"): 
             Rectangle("zoome", 1, 2, "hazem") 
  
     def test_for_height_and_x(self): 
         with self.assertRaisesRegex(TypeError, "height must be an integer"): 
             Rectangle(1, "zoome", "hazem") 
  
     def test_for_height_and_y(self): 
         with self.assertRaisesRegex(TypeError, "height must be an integer"): 
             Rectangle(1, "zoome", 2, "hazem") 
  
     def test_for_x_and_y(self): 
         with self.assertRaisesRegex(TypeError, "x must be an integer"): 
             Rectangle(1, 2, "zoome", "hazem") 
  
     def test_for_area(self): 
         r = Rectangle(1, 2, 3, 4, 5) 
         self.assertEqual(2, r.area()) 
  
     def test_for_area_bigger(self): 
         r = Rectangle(111111111111111, 22222222222222, 3, 4, 5) 
         self.assertEqual((111111111111111 * 22222222222222), r.area()) 
  
     def test_for_area_after_update(self): 
         r = Rectangle(1, 2, 3, 4, 5) 
         r.width = 6 
         r.height = 7 
         self.assertEqual(42, r.area()) 
  
     def test_for_sending_arg_with_area(self): 
         r = Rectangle(1, 2, 3, 4, 5) 
         with self.assertRaises(TypeError): 
             r.area(6) 
  
  
 if __name__ == "__main__": 
     unittest.main()
