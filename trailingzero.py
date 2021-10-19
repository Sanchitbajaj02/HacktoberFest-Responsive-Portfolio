n = int(input())

c = 0

i = 5

while(n/i >= 1):
    c += int(n/i)
    i *= 5

print(c)
