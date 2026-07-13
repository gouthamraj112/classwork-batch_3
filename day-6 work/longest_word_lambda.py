
find_largest=lambda sentence: max(sentence.split(), key=len)
sentence=input("enter a sentence")
largest_word=find_largest(sentence)
print(f"The largest word in the sentence is: {largest_word}")



#madam logic
import time
def find_longest_word(sentence):
    words = sentence.split()
    longest = words[0]
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

sentence = input("Enter a sentence: ")

start_time= time.perf_counter()
result = find_longest_word(sentence)

print("Longest word:", result)
end_time=time.perf_counter()

#execution_time
execution_time=end_time-start_time
print(f"Execution time: {execution_time:.6f} seconds")