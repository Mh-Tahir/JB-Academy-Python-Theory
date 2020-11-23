# Write a program that reads a sequence of numbers from the first line and the number x from the second line. 
#Then it should output all positions of x in the numerical sequence.
n1 = input().split()
n2 = input()
n3 = []
if n2 in n1:
    for i, k in enumerate(n1):
        if k == n2:
            n3.append(str(i))
    print(' '.join(n3))
else:
    print('not found')

# Substring search
def contains(text, pattern):
    for i in range(len(text) - len(pattern) + 1):
        found = True
 
        for j in range(len(pattern)):
            if text[i + j] != pattern[j]:
                found = False
                break
 
        if found:
            return True
 
    return False

# The index of the last occurrence of substring (recursive version)
def contains(text, pattern):
    found = text.find(pattern)
    if found == -1:
        return found
    if text[found + 1:].find(pattern) == -1:
        return found
    else:
        return contains(text[found + 1:], pattern) + found + 1
print(contains(input(), input()))

# The index of the last occurrence of substring (rfind)
def contains(text, pattern):
    return text.rfind(pattern)
print(contains(input(), input()))

# Find hashtags and print them
for n in input().split():
    if n[0] == '#' and '#' not in n[1:]:
        if n.endswith('...'):
            print(n[1:-3])
        elif n[-1] in '.,!?':
            print(n[1:-1])
        else:
            print(n[1:])

#Finding a submatrix in a matrix
def contains2d(text, pattern):
    t = len(text[0])
    p = len(pattern[0])
    for tn in range(len(text) - len(pattern) + 1):
        found = True
        for pn in range(len(pattern)):
            row_found = None
            for i in range(t - p + 1):
                row_found = False
                for j in range(p):
                    if text[tn + pn][i + j] != pattern[pn][j]:
                        break
                else:
                    row_found = True
                if row_found:
                    break
            else:
                found = row_found is True
            if not found:
                break
        else:
            return True
    return False

n, _ = list(map(int, input().split()))
text = [input() for _ in range(n)]
n, _ = list(map(int, input().split()))
pattern = [input() for _ in range(n)]
print(contains2d(text, pattern))

#Find an apostrophe (a' e' i' o' u')
vowels = {'a', 'e', 'i', 'o', 'u'}
 
def find_apostrophe(word, start): 
    i = word.find("'", start)  
    if i == -1:  # there are no apostrophes in the given word
        return -1      
    if i == 0:  # found apostrophe is the first symbol in the word, it doesn't meet the conditions
        return find_apostrophe(word, 1)  # keep searching further 
    elif i == len(word) - 1:  # the apostrophe is the last symbol, doesn't meet the conditions
        return -1  # we have reached the end of the word and haven't found a correct apostrophe 
    else:
        previous_char = word[i - 1]
        if previous_char in vowels:
            return i
        else:  # the found apostrophe does not meet the conditions, we keep searching further
            return find_apostrophe(word, i + 1)

#Identiy whether a text contains a substring equal to a pattern up to symbols permutation
def contains_upto_permutations(text, pattern):
    for i in pattern:
        if text.count(i) < pattern.count(i):
            return False
    return True
print(contains_upto_permutations(input(), input()))

# Checking the validity of an email
def check_email(string):
    return " " not in string and "@" in string and (string.rfind(".")) > (string.find("@") + 1)

