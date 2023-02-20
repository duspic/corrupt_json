# JSONCorruptor class #
#### (in corruptor.py)
I've figured this is the robust solution I was looking for.
It is initialized with a json-compatible dict. During initialization, it creates a schema representation of the json structure, but separates the actual data (values).

![json_dict](readme_imgs/json.png "JSON")

![schema](readme_imgs/schema.png "SCHEMA")

in this example, "string_2" is mapped to "name", "string_3" to "iran" etc.

This approach keeps the data safe from harm, once the corruptions are done, the data is inserted in place of its pair.

_____
# JSONCorruptor.corrupt() method #
Makes a number of corruptions, inserts the data and formats to string representation. Returns the string representation with the corruptions and intact data.

# WHAT NEXT?
- add corrupt functions for numbers and arrays
- test this out as much as possible
- figure out a smarter way of corrupting;
    - avoid accidental repairs (removing and then adding same quotes/brackets)
    - avoid numerous same corrupts (adding 10 quotes/brackets to the same place)
    - avoid reduntant corrupts (once a literal is capitalized, there's no need to try to capitalize it again)
    - individual corrupt functions could produce a (result, success, report) tuple, so we're more familiar with what happened