# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle


# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right', '3,4,5 is a Right triangle')

    def testRightTriangleB(self):
        self.assertEqual(classifyTriangle(10, 6, 8), 'Right', '10, 6, 8 is a Right triangle')

    def testRightTriangleC(self):
        self.assertEqual(classifyTriangle(5, 3, 4), 'Right', '5,3,4 is a Right triangle')

    def testScaleneTriangleA(self):
        self.assertEqual(classifyTriangle(1, 2, 3), 'Scalene', '1, 2, 3 is a Scalene triangle')

    def testScaleneTriangleB(self):
        self.assertEqual(classifyTriangle(11, 6, 8), 'Scalene', '11, 6, 8 is a Scalene triangle')

    def testScaleneTriangleC(self):
        self.assertEqual(classifyTriangle(8, 3, 7), 'Scalene', '8, 3, 7 is a Scalene triangle')

    def testIsocelesTriangleA(self):
        self.assertEqual(classifyTriangle(2, 2, 3), 'Isoceles', '2, 2, 3 is a Isoceles triangle')

    def testIsocelesTriangleB(self):
        self.assertEqual(classifyTriangle(6, 8, 6), 'Isoceles', '6, 6, 8 is a Isoceles triangle')

    def testIsocelesTriangleC(self):
        self.assertEqual(classifyTriangle(8, 4, 4), 'Isoceles', '8, 6, 4 is a Isoceles triangle')

    def testEquilateralTrianglesA(self):
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral', '1,1,1 should be equilateral')

    def testEquilateralTrianglesB(self):
        self.assertEqual(classifyTriangle(10, 10, 10), 'Equilateral', '1,1,1 should be equilateral')

    def testEquilateralTrianglesC(self):
        self.assertEqual(classifyTriangle(100, 100, 100), 'Equilateral', '1,1,1 should be equilateral')

    def testInvalidInputGreaterThanA(self):
        self.assertEqual(classifyTriangle(300, 300, 300), 'InvalidInput',
                         'Any side input that is less than 0 or greater than 200 is invalid')

    def testInvalidInputGreaterThanB(self):
        self.assertEqual(classifyTriangle(100, 200, 300), 'InvalidInput',
                         'Any side input that is less than 0 or greater than 200 is invalid')

    def testInvalidInputGreaterThanC(self):
        self.assertEqual(classifyTriangle(100, 500, 400), 'InvalidInput',
                         'Any side input that is less than 0 or greater than 200 is invalid')

    def testInvalidInputLessThanA(self):
        self.assertEqual(classifyTriangle(-5, 5, 5), 'InvalidInput',
                         'Any side input that is less than 0 or greater than 200 is invalid')

    def testInvalidInputLessThanB(self):
        self.assertEqual(classifyTriangle(5, -5, 5), 'InvalidInput',
                         'Any side input that is less than 0 or greater than 200 is invalid')

    def testInvalidInputLessThanC(self):
        self.assertEqual(classifyTriangle(5, 5, -5), 'InvalidInput',
                         'Any side input that is less than 0 or greater than 200 is invalid')

    def testInvalidInputStringA(self):
        self.assertEqual(classifyTriangle('3', 4, 5), 'InvalidInput',
                         'Any side input that is not a integer is invalid')

    def testInvalidInputStringB(self):
        self.assertEqual(classifyTriangle('3', '4', 5), 'InvalidInput',
                         'Any side input that is not a integer is invalid')

    def testInvalidInputStringC(self):
        self.assertEqual(classifyTriangle('3', 4, '5'), 'InvalidInput',
                         'Any side input that is not a integer is invalid')

    def testInvalidTriangleLengthsA(self):
        self.assertEqual(classifyTriangle(2, 2, 5), 'NotATriangle',
                         'Any side input that is not a integer is invalid')

    def testInvalidTriangleLengthsB(self):
        self.assertEqual(classifyTriangle(2, 5, 2), 'NotATriangle',
                         'Any side input that is not a integer is invalid')

    def testInvalidTriangleLengthsC(self):
        self.assertEqual(classifyTriangle(5, 2, 2), 'NotATriangle',
                         'Any side input that is not a integer is invalid')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
