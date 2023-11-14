import unittest
import hello_world as hw
from src.pipelines import word_count_minimal


class TestWordCountMinimal(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(True, hw.hello_world())  # add assertion here

    def test_run_word_count_minimal_direct_direct_runner(self):
        self.assertEqual(True, word_count_minimal.hello_world())  # add assertion here


if __name__ == '__main__':
    unittest.main()
