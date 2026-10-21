string = "python"
pattern = "th"

#length of string and pattern
x = len(string)
y = len(pattern)
d = 256

#Hashcode of pattern

sumP = 0
for i in range(y):
    sumP += ord(pattern[i]) * d**(y - i - 1)

sumS = 0
for i in range(y):
    sumS += ord(string[i]) * d**(y - 1 - i)

if(sumS == sumP):
    print("Pattern found at index 0")
for i in range(y , x):
    sumS = ((sumS - ord(string[i-y]) * (d**(y-1))) * d) + ord(string[i])
    if(sumS == sumP):
        print("pattern found at index",i - y + 1)