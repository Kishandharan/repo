import random


def pw():
    nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    alphabets = ["a", "b", "c", "d", "e", "f", "g", "h"]
    specialChars = ["%", "^", "*", "(", ")", "-", "="]
    nums_r = random.choice(nums)
    alphabets_r = random.choice(alphabets)
    specialChars_r = random.choice(specialChars)
    password = nums_r + alphabets_r + specialChars_r + nums_r
    return password


a = pw()
print(a)
