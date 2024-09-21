#Task2 - String
sentence = "Learning Python is fun and rewarding."

substring = sentence[-28:-14]
print(substring)
    
modified_sentence = sentence.replace("rewarding", "exciting")

insertion_point = modified_sentence.find("exciting") + len("exciting")
final_sentence = modified_sentence[:insertion_point] + " Keep practicing!" + modified_sentence[insertion_point:]

final_sentence = final_sentence.title()
print(final_sentence)