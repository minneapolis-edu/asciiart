import unittest
import os
import sys

#sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))
#import asciiart
import asciiart
from asciiart import asciify as asc

#from asciiart import asciify


class AsciifyTest(unittest.TestCase):

    def test_avg_color(self):

        #list of colors are in the format
        # [(2, (124, 84, 33)), (5, (125, 83, 33)), (3, (126, 82, 33)), (4, (124, 82, 32)), (2, (125, 81, 32))]
        # TODO

        expected = asc.avg_col([(2, (124, 84, 33)), (5, (125, 83, 33)), (3, (126, 82, 33)), (4, (124, 82, 32)), (2, (125, 81, 32))])
        self.assertEqual(expected, (125,83,33))


    def test_color_to_gray(self):

        colorvals = [ (0, 0, 0), (-10, -10, -10), (150, 170, 255), (600, 600, 600)]

        for val in colorvals:
            g = asc.color_to_gray(col)
            self.assertTrue(g >=0 and g <= 255)



    def test_ascii_pix(self):

        #Testing the appropriate character is being returned...
        self.assertEqual(asc.ascii_pixels[0], asc.ascii_pix(255) , '1')
        self.assertEqual(asc.ascii_pixels[2], asc.ascii_pix(190) , '2')
        self.assertEqual(asc.ascii_pixels[4], asc.ascii_pix(110) , '3')
        self.assertEqual(asc.ascii_pixels[7], asc.ascii_pix(2) , '4')

        pass


if __name__ == '__main__':
    unittest.main()