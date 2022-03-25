import unittest

from kr_1.kr1_1 import print_usage_statistic, Spy


def check_message(actual, expected: str) -> bool:
    return expected in str(actual.exception)


class SpyTestCase(unittest.TestCase):
    def test_error_function(self):
        with self.assertRaises(ValueError) as context:
            def foo():
                return 5

            for _, _ in print_usage_statistic(foo):
                pass

        self.assertTrue(
            check_message(context, "The function should be decorated with @Spy.")
        )

    def test_usual_function(self):
        @Spy
        def foo(number): return number

        foo(1)
        foo(2)
        foo(3)

        actual = []
        for _, parameters in print_usage_statistic(foo):
            actual.append(parameters)

        expected = [
            {"args": (1,), "kwargs": {}},
            {"args": (2,), "kwargs": {}},
            {"args": (3,), "kwargs": {}}

        ]

        self.assertEqual(actual, expected)
