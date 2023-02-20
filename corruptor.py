class JSONCorruptor():
    """
    For this to work properly, initialize with
    a json-compatible python dict. This can
    be assured by writing the json as a string
    and using json.loads() to create the dict
    
    call the .corrupt() method to get a string
    representation of the corrupted json object.
    
    the .corrupt() method doesn't change data,
    but only corrupts formatting. This is ensured
    by keeping the data abstracted while the corru-
    ptions are going on, and inserting it after.
    """
    
    def __init__(self, json_dict:dict):
        self.json_dict = json_dict
        self._counter = {
        "null":0,
        "false":0,
        "true":0,
        "number":0,
        "string":0,
        "array":0,
        "object":0
        }
        self.name_element_map = {}
        self._schema = self._make_schema()
        self._corrupt_schema = self.get_schema()
        
        self.element_corruption_map = {
            "string":[
                self._add_quotations_left,
                self._add_quotations_right,
                self._remove_quotations_left,
                self._remove_quotations_right
                ],
            "number": [
                ],
            "object": [
                self._add_curly_bracket_left,
                self._remove_curly_bracket_left,
            ],
            "array": [
            ],
            "literal": [
            ]
        }
    
    def corrupt(self, count:int=3) ->str:
        """ 
        one-stop-shop for corrupts
        """
        from random import choice
        # choose only from elements tha are present in this json
        elements = [k for k,v in self._counter.items() if v>0]
        
        for i in range(count):
            # choose an element
            el = choice(elements)
            # choose a corrupt func
            corrupts = self.element_corruption_map[el]
            fn = choice(corrupts)
            # choose a specific element
            no = choice(range(1,self._counter[el]+1))
            name = f"{el}_{no}"
            self._corrupt_schema = fn(self._corrupt_schema,name)
            print(f"corrupted {name} with {fn.__name__}") 
    
        return self._schema_to_json_str(self._corrupt_schema)
    
    def print_schema(self):
        from pprint import pprint
        return pprint(self._schema)
    
    def get_schema(self):
        return str(self._schema)
    
    ###################################
    
    def _add_quotations_left(self, schema:str, name:str) -> str:
        return schema.replace(name, f'"{name}', 1)
        
    def _add_quotations_right(self, schema:str, name:str) -> str:
        return schema.replace(name, f'{name}"', 1)
 
    def _remove_quotations_left(self, schema:str, name:str) -> str:
        return schema.replace(f"'{name}",name, 1)
    
    def _remove_quotations_right(self, schema:str, name:str) -> str:
        return schema.replace(f"{name}'",name, 1)
    
    def _add_curly_bracket_left(self, schema:str, name:str) -> str:
        return schema.replace(f"'{name}", "{'"+name, 1)
    
    def _add_curly_bracket_right(self, schema:str, name:str) -> str:
        pass
    
    def _remove_curly_bracket_left(self, schema:str, name:str) -> str:
        # left curly is 2 idxs before "object_x" or 3 idxs after
        idx = schema.find(name)
        if schema[idx-2] == '{':
            return schema[:idx-2]+schema[idx-1:]
        
        # len(object_x)+3 = 11
        if schema[idx+11] == '{':
            return schema[:idx+11]+schema[idx+12:]
        
        return schema
    
    def _translate_type(self,element):
            """
            +-------------------+---------------+
            | Python            | JSON          |
            +===================+===============+
            | dict              | object        |
            +-------------------+---------------+
            | list, tuple       | array         |
            +-------------------+---------------+
            | str               | string        |
            +-------------------+---------------+
            | int, float        | number        |
            +-------------------+---------------+
            | True              | true          |
            +-------------------+---------------+
            | False             | false         |
            +-------------------+---------------+
            | None              | null          |
            +-------------------+---------------+
            """
            dct = {
                dict:"object",
                list:"array",
                tuple:"array",
                str:"string",
                int:"number",
                float:"number",
                bool:"true" if element else "false",
                type(None):"null"
                }
            
            return dct[type(element)]
        
    def _map_name_to_element(self,name,el):
        self.name_element_map[name] = (el)
        return
    
    def _recursive(self,el):
        el_type = self._translate_type(el)
        name = self._create_unique_name(el_type)
        self._map_name_to_element(name, el)
        
        # if it's a "simple" type, just return the name
        if el_type in ('null', 'false', 'true', 'number', 'string'):
            return name
        
        # if it's a "complex" type, time for a recursion
        if el_type == 'array':
            return name,[self._recursive(x) for x in el]
        
        if el_type == 'object':
            ret_dict = {}
            for k,v in el.items():
                key = self._recursive(k)
                ret_dict[key] = self._recursive(v)
            return name, ret_dict

    def _make_schema(self):
        return self._recursive(self.json_dict)
    
    def _create_unique_name(self, el_type):
        self._counter[el_type] += 1
        return f"{el_type}_{self._counter[el_type]}"
    
    def _schema_to_json_str(self, sch):

        for k,v in self.name_element_map.items():
            # remove object_x and array_x appearances
            if "object" in k or "array" in k:
                sch = sch.replace(f"'{k}', ","",1)
            # replace number
            elif "number" in k:
                sch = sch.replace(f"'{k}'",str(v),1)
            # replace true, false, null and string
            else:
                sch = sch.replace(k,v,1)
        sch = sch.replace("(","")
        sch = sch.replace(")","")
        sch = sch.replace("'", '"')
        
        return sch