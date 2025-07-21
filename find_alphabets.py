paragraph = "Hello 12 34 WOrld"

alpha = 0
space = 0
digit = 0

for i in range(len(paragraph)):
    if paragraph[i].isalpha():
        print(paragraph[i], end=" " )
        alpha += 1
    else:
        if paragraph[i].isspace():
            space += 1
        elif paragraph[i].isdigit():
            digit += 1

print("Alphabets:", alpha)
print("Spaces:", space)
print("Digits:", digit)