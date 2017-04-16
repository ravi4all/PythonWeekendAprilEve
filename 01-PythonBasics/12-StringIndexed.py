word = 'Machine'
print(word[0])      # character in position 0

print(word[0] + word[4])    # character in position 0 + character in position 4

print(word[-1])     # Last character

print(word[-2])     # Second last Character

print(word[0:2])    # Character from position [0](included) to [2](excluded)

print(word[2:5])    # Character from position [2](included) to [5](excluded)

print(word[:2] + word[2:])  # This makes sure that s[:i] + s[i:] is always equal to s:

print(word[:-1])     # character from the beginning to position 2 (excluded)

print(word[::-1])       # Reverse the string

print(word[0:] + 's')   # To create different String

print(len(word))     # To print the length of string

a = ["I ", "Like ", "Logic"]
print("".join(a))
