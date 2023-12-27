def letter_count(ws, letter):
    sentence = ws
    reference = letter
    result = sentence.count(reference)
    return result


input1 = input("Enter a sentence: ")
input2 = input("What letter to count: ")
Result = letter_count(input1, input2)
print(f"The number of '{input2}' in '{input1}':", Result)
