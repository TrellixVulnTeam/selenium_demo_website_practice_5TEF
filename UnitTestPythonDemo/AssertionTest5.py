import unittest


class Test(unittest.TestCase):
    def testName(self):
        # self.assertGreater(10, 100)
        # self.assertGreaterEqual(100, 100)

        # self.assertLess(10,100)
        self.assertLessEqual(100, 100)


if __name__ == "__main__":
    unittest.main()
