'''
You're working on a seach engine. Watch your back Google!
The given code takes a text and a word as input and passes them to a function called search().
The search() function should return "Word found" if the word is print in the text,
or "Word not found", if it's not.

Sample Input:
"This is awesome"
"awesome"

Sample Output:
Word found
'''

def search(text, word):
    x = text.split(' ')
    c=0
    for i in x:
        if i==word:
            c+=1
    if c==0:
        return "Word not found"
    else:
        return "Word found"

text = input("Enter a text message:")
word = input("Enter a word to be found in message:")

print(search(text, word))