
find_largest=lambda sentence: max(sentence.split(), key=len)
sentence=input("enter a sentence")
largest_word=find_largest(sentence)
print(f"The largest word in the sentence is: {largest_word}")