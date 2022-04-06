import unittest
import sphere

class sphereTest(unittest.TestCase):

    #passing tests
    def test_volume1(self):
        assert(sphere.volume(10) == 4188.790204786391)

    def test_surfaceArea1(self):
        assert(sphere.surfaceArea(10) == 1256.6370614359173)

    #failing test
    #def test_volume3(self):
        #assert(cylinder.volume(10,1000) == 0)


if __name__ == '__main__':
    unittest.main()