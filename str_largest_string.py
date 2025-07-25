sentences = ["my name is John", "I love programming", "Python is great", "Hello world"]

def largest_string(sentences):
    largest = ""
    max_len = 0
    for sentence in sentences:
        if len(sentence) > max_len:
            max_len = len(sentence)
            largest = sentence

    return largest, max_len

# Example usage
largest_sentence, length = largest_string(sentences)

print("Largest sentence:", largest_sentence)
print("Length of largest sentence:", length)