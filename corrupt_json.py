import json
import random


def random_idx_of_element_in_str(el:str, s:str) -> int:
    """
    Randomly selects a starting point in the string,
    searches for appearance of element from the starting
    point onwards. 
    If no element is found that way, searches from
    the beginning of string. 
    Returns the index of found element in str, or -1
    """
    
    idx = random.randint(0, len(s)-1)
    el_idx = s.find(el,idx)
    if el_idx == -1:
        el_idx = s.find(el,0)
        
    return el_idx
    
def add_curly_bracket(s: str) -> str:
    """
    Randomly selects an existing curly bracket in the string and doubles it.
    In the case of not finding a bracket from the randomly selected index,
    doubles the first similar bracket it finds
    """
    bracket = random.choice(['{','}'])
    bracket_idx = random_idx_of_element_in_str(bracket,s)
    
    if bracket_idx == -1:
        report = f"Failed to add curly bracket '{bracket}'"
        success = False
        return s, success, report
    
    s = s[:bracket_idx] + bracket + s[bracket_idx:]
    report = f"Added a curly bracket '{bracket}' to index {bracket_idx}"
    success = True
    return s, success, report

def remove_curly_bracket(s: str) -> str:
    """
    Randomly selects an existing curly bracket in the string and removes it.
    In the case of not finding a bracket from the randomly selected index,
    removes the first similar bracket it finds
    """
    bracket = random.choice(['{','}'])
    bracket_idx = random_idx_of_element_in_str(bracket,s)
    if bracket_idx == -1:
        report = f"Failed to add curly bracket '{bracket}'"
        success = False
        return s, success, report
    
    s = s[:bracket_idx] + s[bracket_idx+1:]
    report = f"Removed a curly bracket '{bracket}' from index {bracket_idx}"
    success = True
    return s, success, report

def add_quotation_mark(s: str) -> str:
    """
    Randomly selects an existing quotation mark in the string and doubles it.
    In the case of not finding one from the randomly selected index,
    places a quotation mark at the beginning.
    """
    qmark_idx = random_idx_of_element_in_str('"',s)
    if qmark_idx == -1:
        report = "Failed to add quotation marks"
        success = False
        return s, success, report
    
    s = s[:qmark_idx] + '"' + s[qmark_idx:]
    report = f"Added a quotation mark to index {qmark_idx}"
    success = True
    return s, success, report

def remove_quotation_mark(s: str) -> str:
    """
    Randomly selects an existing quotation mark in the string and removes it.
    In the case of not finding one from the randomly selected index,
    removes the first one it finds.
    """
    qmark_idx = random_idx_of_element_in_str('"',s)
    if qmark_idx == -1:
        report = "Failed to remove quotation marks"
        success = False
        return s, success, report
    
    s = s[:qmark_idx] + s[qmark_idx+1:]
    report = f"Removed a quotation mark from index {qmark_idx}"
    success = True
    return s, success, report

def uppercase_literal(s: str) -> str:
    """ 
    Randomly selects a literal and makes it uppercase
    """
    literal = random.choice(['true','false','null'])
    literal_idx = random_idx_of_element_in_str(literal,s)
    if literal_idx == -1:
        report = f"Failed to find '{literal}' and make it uppercase"
        success = False
        return s, success, report
    
    s = s[:literal_idx] + s[literal_idx:].replace(literal,literal.upper(),1)
    
    report = f"Made the literal {literal} uppercase at index {literal_idx}"
    success = True
    return s, success, report

def capitalize_literal(s: str) -> str:
    """ 
    Randomly selects a literal and makes it capitalized
    """
    literal = random.choice(['true','false','null'])
    literal_idx = random_idx_of_element_in_str(literal,s)
    if literal_idx == -1:
        report = f"Failed to find '{literal}' and make it capitalized"
        success = False
        return s, success, report
    
    s = s[:literal_idx] + s[literal_idx:].replace(literal,literal.capitalize(),1)
    
    report = f"Made the literal {literal} capitalized at index {literal_idx}"
    success = True
    return s, success, report

def add_trailing_comma(s: str) -> str:
    """ 
    Randomly selects a comma and duplicates it
    If here are none add the comma before or after the last element
    """
    
    comma_idx = random_idx_of_element_in_str(',',s)
    if comma_idx == -1:
        colon_idx = s.find(':')
        # check for second quotes right of colon symbol
        quote_idx = s[colon_idx+1:].find('"')
        # if there aren't any, find the first quotes in str
        if quote_idx == -1:
            quote_idx = s.find('"')
        # the first quote can't be next to colon
        if quote_idx in [-1, colon_idx-1, colon_idx+1]:
            report = "Failed to add a trailing comma"
            success = False
            return s, success, report
        
        comma_idx = quote_idx+1
    
    s = s[:comma_idx] + ',' + s[comma_idx:]
    
    report = f"Added a trailing comma at index {comma_idx}"
    success = True
    return s, success, report

def unescape_char(s: str) -> str:
    idx = random_idx_of_element_in_str("\\",s)
    if idx == -1:
        report = "Failed to find backslashes - unescape chars"
        success = False
        return s, success, report
    
    s = s[:idx] + s[idx+1:]
    report = f"Removed one backslash at position {idx}"
    success = True
    return s, success, report


COMMON_JSON_CORRUPTS = [add_curly_bracket, remove_curly_bracket, add_quotation_mark, remove_quotation_mark, uppercase_literal, capitalize_literal, add_trailing_comma, unescape_char]

def corrupt_json(no_of_corrupts:int, json_string: str) -> str:
    # check if it's already corrupted, that could lead to unexpected problems
    # as this deals only with common corrupts, and not with other possibilities
    try:
        print(json.loads(json_string))
        
    except json.decoder.JSONDecodeError as e:
        print("Json formatting already corrupted:")
        print(e)
    
    count = 0
    while count < no_of_corrupts:
        fn = random.choice(COMMON_JSON_CORRUPTS)
        json_string, success, report = fn(json_string)
        if success:
            count += 1
        print(report)
         
    return json_string

# flaw - adding and removing quotation marks can cancel each other out, the same with curly braces
# uppercasing or capitalizing literals seldom works, because the literals are also randomly selected.
# so if a string containst 100s of "null" literals, none of them will capitalize if "true" was selected

# otherwise, I guess it's best to try it out