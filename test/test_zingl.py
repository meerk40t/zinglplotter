import unittest
from math import ceil

from zinglplotter import *


class TestZingl(unittest.TestCase):
    def test_line(self):
        for x, y in plot_line(0, 0, 100, 100):
            self.assertEqual(x, y)

        for i, v in enumerate(plot_line(0, 0, 100, 0)):
            x, y = v
            self.assertEqual(y, 0)
            self.assertEqual(x, i)

        for i, v in enumerate(plot_line(0, 0, 0, 100)):
            x, y = v
            self.assertEqual(x, 0)
            self.assertEqual(y, i)

        for i, v in enumerate(plot_line(0, 0, 100, 300)):
            x, y = v
            self.assertEqual(x, int(round(i / 3.0)))
            self.assertEqual(y, i)

        for i, v in enumerate(plot_line(0, 0, 300, 100)):
            x, y = v
            self.assertEqual(y, int(round(i / 3.0)))
            self.assertEqual(x, i)

        for i, v in enumerate(plot_line(0, 0, 100, 200)):
            x, y = v
            self.assertEqual(x, int(ceil(i / 2.0)))
            self.assertEqual(y, i)

    def test_quad_bezier(self):
        for x, y in plot_quad_bezier(0, 0, 50, 50, 100, 100):
            self.assertEqual(x, y)
        for x, y in plot_quad_bezier(0, 0, 50, 50, 0, 0):
            self.assertEqual(x, y)

    def test_cubic_bezier(self):
        for x, y in plot_cubic_bezier(0, 0, 50, 50, 100, 100, 150, 150):
            self.assertEqual(x, y)
        for x, y in plot_cubic_bezier(0, 0, 100, 100, 100, 100, 0, 0):
            self.assertEqual(x, y)

    def test_random_cubic(self):
        import random

        for i in range(1000):
            x, y = random.randint(0, 100), random.randint(0, 100)
            for plot in plot_cubic_bezier(
                x,
                y,
                (random.random() * 100),
                (random.random() * 100),
                (random.random() * 100),
                (random.random() * 100),
                random.randint(0, 100),
                random.randint(0, 100),
            ):
                pass

    def test_random_quad(self):
        import random

        for i in range(1000):
            x, y = random.randint(0, 100), random.randint(0, 100)
            for plot in plot_quad_bezier(
                x,
                y,
                (random.random() * 100),
                (random.random() * 100),
                random.randint(0, 100),
                random.randint(0, 100),
            ):
                pass

    def test_random_line(self):
        import random

        for i in range(100000):
            x, y = random.randint(0, 100), random.randint(0, 100)
            for plot in plot_line(x, y, random.randint(0, 100), random.randint(0, 100)):
                pass
