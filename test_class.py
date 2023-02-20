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
        
    def test_remove_quotes_left(self):
        from corruptor import JSONCorruptor
        from random import randint
        import json
        original_json = '{"a":{"b":"c"}}'
        json_dict = json.loads(original_json)
        
        for _ in range(50):
            rnd_str = f"string_{randint(1,3)}"
            jc = JSONCorruptor(json_dict)
            jc._corrupt_schema = jc._remove_quotations_left(jc._corrupt_schema,rnd_str)
            corrupt_json = jc._schema_to_json_str(jc._corrupt_schema)
            
            expected = {
                """{a": {"b": "c"}}""",
                """{"a": {b": "c"}}""",
                """{"a": {"b": c"}}"""
            }
            print(f"{original_json = }, {corrupt_json = }")
            self.assertIn(corrupt_json, expected)
    
    def test_remove_quotes_right(self):
        from corruptor import JSONCorruptor
        from random import randint
        import json
        original_json = '{"a":{"b":"c"}}'
        json_dict = json.loads(original_json)
        
        for _ in range(50):
            rnd_str = f"string_{randint(1,3)}"
            jc = JSONCorruptor(json_dict)
            jc._corrupt_schema = jc._remove_quotations_right(jc._corrupt_schema,rnd_str)
            corrupt_json = jc._schema_to_json_str(jc._corrupt_schema)
            
            expected = {
                """{"a: {"b": "c"}}""",
                """{"a": {"b: "c"}}""",
                """{"a": {"b": "c}}"""
            }
            print(f"{original_json = }, {corrupt_json = }")
            self.assertIn(corrupt_json, expected)
            
    def test_add_curly_left(self):
        from corruptor import JSONCorruptor
        from random import randint
        import json
        original_json = '{"number_1":{"1":"one"}, "number_2":{"2":"two"}}'
        json_dict = json.loads(original_json)
        
        for _ in range(50):
            rnd_str = f"object_{randint(1,3)}"
            jc = JSONCorruptor(json_dict)
            jc._corrupt_schema = jc._add_curly_bracket_left(jc._corrupt_schema,rnd_str)
            corrupt_json = jc._schema_to_json_str(jc._corrupt_schema)
        
            expected = {
                """{{"number_1": {"1": "one"}, "number_2": {"2": "two"}}""",
                """{"number_1": {{"1": "one"}, "number_2": {"2": "two"}}""",
                """{"number_1": {"1": "one"}, "number_2": {{"2": "two"}}"""
            }
            print(f"{original_json = }, {corrupt_json = }")
            self.assertIn(corrupt_json, expected)
            
    def test_remove_curly_left(self):
        from corruptor import JSONCorruptor
        from random import randint
        import json
        original_json = '{"number_1":{"1":"one"}, "number_2":{"2":"two"}}'
        json_dict = json.loads(original_json)
        
        for _ in range(50):
            rnd_str = f"object_{randint(1,3)}"
            jc = JSONCorruptor(json_dict)
            jc._corrupt_schema = jc._remove_curly_bracket_left(jc._corrupt_schema,rnd_str)
            corrupt_json = jc._schema_to_json_str(jc._corrupt_schema)
        
            expected = {
                """"number_1": {"1": "one"}, "number_2": {"2": "two"}}""",
                """{"number_1": "1": "one"}, "number_2": {"2": "two"}}""",
                """{"number_1": {"1": "one"}, "number_2": "2": "two"}}"""
            }
            print(f"{original_json = }, {corrupt_json = }")
            self.assertIn(corrupt_json, expected)
            
    def test_add_curly_right(self):
        from corruptor import JSONCorruptor
        from random import randint
        import json
        original_json = '{"number_1":{"1":"one"}, "number_2":{"2":"two"}}'
        json_dict = json.loads(original_json)
        
        for _ in range(50):
            rnd_str = f"object_{randint(1,3)}"
            jc = JSONCorruptor(json_dict)
            jc._corrupt_schema = jc._add_curly_bracket_right(jc._corrupt_schema,rnd_str)
            corrupt_json = jc._schema_to_json_str(jc._corrupt_schema)
        
            expected = {
                """{"number_1": {"1": "one"}}, "number_2": {"2": "two"}}""",
                """{"number_1": {"1": "one"}, "number_2": {"2": "two"}}}""",
            }
            print(f"{original_json = }, {corrupt_json = }")
            self.assertIn(corrupt_json, expected)
            
    def test_remove_curly_right(self):
        from corruptor import JSONCorruptor
        from random import randint
        import json
        original_json = '{"number_1":{"1":"one"}, "number_2":{"2":"two"}}'
        json_dict = json.loads(original_json)
        
        for _ in range(50):
            rnd_str = f"object_{randint(1,3)}"
            jc = JSONCorruptor(json_dict)
            jc._corrupt_schema = jc._remove_curly_bracket_right(jc._corrupt_schema,rnd_str)
            corrupt_json = jc._schema_to_json_str(jc._corrupt_schema)
        
            expected = {
                """{"number_1": {"1": "one", "number_2": {"2": "two"}}""",
                """{"number_1": {"1": "one"}, "number_2": {"2": "two"}""",
            }
            print(f"{original_json = }, {corrupt_json = }")
            self.assertIn(corrupt_json, expected)
    
    def test_capitalize_literal(self):
        from corruptor import JSONCorruptor
        from random import choice
        import json
        original_json = '{"a": null, "b": false, "c": true}'
        json_dict = json.loads(original_json)
        name = choice(["null_1", "false_1", "true_1"])
        jc  = JSONCorruptor(json_dict)
        jc._corrupt_schema = jc._capitalize_literal(jc._corrupt_schema, name)
        corrupt_json = jc._schema_to_json_str(jc._corrupt_schema)
        
        expected = {
            '{"a": Null, "b": false, "c": true}',
            '{"a": null, "b": False, "c": true}',
            '{"a": null, "b": false, "c": True}'
        }
        print(f"{original_json = }, {corrupt_json = }")
        self.assertIn(corrupt_json, expected)

    def test_capitalize_literal_2(self):
        from corruptor import JSONCorruptor
        from random import choice
        import json
        original_json = '{"a": null, "b": "false", "c": true}'
        json_dict = json.loads(original_json)
        name = choice(["null_1", "false_1", "true_1"])
        jc  = JSONCorruptor(json_dict)
        jc._corrupt_schema = jc._capitalize_literal(jc._corrupt_schema, name)
        corrupt_json = jc._schema_to_json_str(jc._corrupt_schema)
        
        expected = {
            '{"a": Null, "b": "false", "c": true}',
            '{"a": null, "b": "false", "c": True}'
        }
        print(f"{original_json = }, {corrupt_json = }")
        self.assertIn(corrupt_json, expected)