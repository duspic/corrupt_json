from unittest import TestCase

class Test(TestCase):
    def test(self):
        self.assertTrue(True)

    def test_add_quotes_left(self):
        from corruptor import JSONCorruptor
        from random import randint
        import json
        original_json = '{"a":"abc", "b":"bca", "c":"cab"}'
        json_dict = json.loads(original_json)
        
        for _ in range(50):
            rnd_str = f"string_{randint(1,6)}"
            jc = JSONCorruptor(json_dict)
            jc._corrupt_schema = jc._add_quotations_left(jc._corrupt_schema,rnd_str)
            corrupt_json = jc._schema_to_json_str(jc._corrupt_schema)
            
            expected = {
                """{""a": "abc", "b": "bca", "c": "cab"}""",
                """{"a": ""abc", "b": "bca", "c": "cab"}""",
                """{"a": "abc", ""b": "bca", "c": "cab"}""",
                """{"a": "abc", "b": ""bca", "c": "cab"}""",
                """{"a": "abc", "b": "bca", ""c": "cab"}""",
                """{"a": "abc", "b": "bca", "c": ""cab"}"""
            }
            print(f"{original_json = }, {corrupt_json = }")
            self.assertIn(corrupt_json, expected)
            
    def test_add_quotes_right(self):
        from corruptor import JSONCorruptor
        from random import randint
        import json
        original_json = '{"a":"abc", "b":"bca", "c":"cab"}'
        json_dict = json.loads(original_json)
        
        for _ in range(50):
            rnd_str = f"string_{randint(1,6)}"
            jc = JSONCorruptor(json_dict)
            jc._corrupt_schema = jc._add_quotations_right(jc._corrupt_schema,rnd_str)
            corrupt_json = jc._schema_to_json_str(jc._corrupt_schema)
            
            expected = {
                """{"a"": "abc", "b": "bca", "c": "cab"}""",
                """{"a": "abc"", "b": "bca", "c": "cab"}""",
                """{"a": "abc", "b"": "bca", "c": "cab"}""",
                """{"a": "abc", "b": "bca"", "c": "cab"}""",
                """{"a": "abc", "b": "bca", "c"": "cab"}""",
                """{"a": "abc", "b": "bca", "c": "cab""}"""
            }
            print(f"{original_json = }, {corrupt_json = }")
            self.assertIn(corrupt_json, expected)
        
        
