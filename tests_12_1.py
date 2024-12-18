import unittest

from runner import Runner


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        a = Runner('Pablo')
        for i in range(10):
            a.walk()
        self.assertEqual(a.distance, 50)

    def test_run(self):
        b = Runner('Pedro')
        for i in range(10):
            b.run()
        self.assertEqual(b.distance, 100)

    def test_challenge(self):
        a = Runner('Pablo')
        b = Runner('Pedro')
        for i in range(10):
            a.run()
            b.walk()
        self.assertNotEqual(a.distance, b.distance)


if __name__ == '__main__':
    unittest.main()
