from difflib import get_close_matches
list1 = {1:"rok", 2:"rockot"}
if len(get_close_matches(list1, list1.keys)) > 0:
    print("Did you mean %s")
