from unittest import TestCase


class Test(TestCase):
    def test(self):
        self.assertTrue(True)

    def test_add_curly_bracket_1(self):
        from corrupt_json import add_curly_bracket
        original_json = '{"a": 1, "b": 2}'
        (corrupt_json, success, report) = add_curly_bracket(original_json)
        print(f"{original_json = }, {corrupt_json = }, {success = }, {report = }")

        expected = {
            """{"a": 1, "b": 2}}""",
            """{{"a": 1, "b": 2}""",
        }

        self.assertIn(corrupt_json, expected)

    def test_add_curly_bracket_2(self):
        from corrupt_json import add_curly_bracket
        original_json = '{"{a}": 1, "b": 2}'
        for _ in range(100):
            (corrupt_json, success, report) = add_curly_bracket(original_json)
            print(f"{original_json = }, {corrupt_json = }, {success = }, {report = }")

            expected = {
                """{"{a}": 1, "b": 2}}""",
                """{{"{a}": 1, "b": 2}""",
            }

            self.assertIn(corrupt_json, expected)
