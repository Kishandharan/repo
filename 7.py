import time
class ExistingChecker:
    def get(sentence = None, word = None, default = None):
        if word in sentence:
            return "Yes, it exist!"
        else:
            return default

senten_arg = input("Enter the sentence that should be tested: ")
word_arg = input("Enter the word or letter: ")
default_arg = input("Enter the default value: ")
result = ExistingChecker.get(senten_arg, word_arg, default_arg)
print("Processing...")
time.sleep(10)
print(result)
