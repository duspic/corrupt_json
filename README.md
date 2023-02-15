# The main function is
# def corrupt_json(json_string:str, no_of_corrupts:int=3) -> str

Other functions each deal with a certain common type of JSON corruption, 
each making a single corruption at a time by semi-randomly selecting where to place the corruption.
For example, adding a curly bracket won't happen in the middle of a key or value, but will happen next to an existing bracket, 
as that is where those corruptions are most probable. The specific bracket which will be duplicated, however, is randomly selected.

A similar principle is applied to other functions.


Try the **corrupt_json** with a small no_of_corrupts and a simple json_string first.

Disclaimer: I haven't tested this properly, but have tried to make it somewhat robust.
