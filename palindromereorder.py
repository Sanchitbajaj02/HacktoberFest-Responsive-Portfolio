s = input()

# Loop through the array and keep track of which characters have a pair and which are single (have no pair)
pairs = []
single = []

for char in s:
    if char in single:
        single.remove(char)
        pairs.append(char)
    else:
        single.append(char)

# Construct the palindrome by sandwiching the single elements between the pair elements
res = ''.join(pairs) + ''.join(single) + ''.join(pairs)[::-1]

# Check if it is a palindrome
if res == res[::-1]:
    print(res)
else:
    print("NO SOLUTION")
