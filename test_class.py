from unittest import TestCase

class Test(TestCase):
    def test(self):
        self.assertTrue(True)

    def test_method_corrupt(self):
        from corruptor import JSONCorruptor
        import json
        original_json = '{"{a}": 1, "b": 2}'
        json_dict = json.loads(original_json)
        
        jc = JSONCorruptor(json_dict)
        corrupt_json = jc.corrupt(1)

        expected = {
                """{""{a}": 1, "b": 2}""",
                """{"{a}"": 1, "b": 2}""",
                """{"{a}": 1, ""b": 2}""",
                """{"{a}": 1, "b"": 2}""",
            }
        print(f"{original_json = }, {corrupt_json = }")
        self.assertIn(corrupt_json, expected)
        
    def test_method_corrupt_50(self):
        from corruptor import JSONCorruptor
        import json
        original_json = '{"{a}": "abra", "b": "kadabra", "[c]":"cobra"}'
        json_dict = json.loads(original_json)
        
        for _ in range(50):
            jc = JSONCorruptor(json_dict)
            corrupt_json = jc.corrupt(1)

            expected = {
                    """{""{a}": "abra", "b": "kadabra", "[c]": "cobra"}""",
                    """{"{a}"": "abra", "b": "kadabra", "[c]": "cobra"}""",
                    """{"{a}": ""abra", "b": "kadabra", "[c]": "cobra"}""",
                    """{"{a}": "abra"", "b": "kadabra", "[c]": "cobra"}""",
                    """{"{a}": "abra", ""b": "kadabra", "[c]": "cobra"}""",
                    """{"{a}": "abra", "b"": "kadabra", "[c]": "cobra"}""",
                    """{"{a}": "abra", "b": ""kadabra", "[c]": "cobra"}""",
                    """{"{a}": "abra", "b": "kadabra"", "[c]": "cobra"}""",
                    """{"{a}": "abra", "b": "kadabra", ""[c]": "cobra"}""",
                    """{"{a}": "abra", "b": "kadabra", "[c]"": "cobra"}""",
                    """{"{a}": "abra", "b": "kadabra", "[c]": ""cobra"}""",
                    """{"{a}": "abra", "b": "kadabra", "[c]": "cobra""}"""
                }
            print(f"{original_json = }, {corrupt_json = }")
            self.assertIn(corrupt_json, expected)
