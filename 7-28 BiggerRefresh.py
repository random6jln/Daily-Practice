numbers = []

with open("numbers.txt") as f:
    for line in f:
            n = int(line.strip())    #because line is considered a string you have to make a storage variable that holds the value (strips line) as an int 
            numbers.append(n)

biggest = numbers[0]

for n in numbers:
    if n > biggest:
        biggest = n 
print(biggest)       