'''Alice wants to send a message to Bob but doesn't want Eve to read it. So decides to encrypt it using a scheme. This 
scheme follows the following rule:
A = ._
B = _...
C = _._.
D = _..
E = .
F = .._.
G = __.
H = ....
I = ..
J = .___
K = _._
L = ._..
M = __
N = _.
O = ___
P = .__.
Q = __._
R = ._.
S = ...
T = _
U = .._
V = ..._
W = .__
X = _.._
Y = _.__
Z = __..
For example, "__.._...__" is the word "GREAT". Unfortunately, this
sequence also decrypts to 'GAEEAT', 'GAEEEM', 'MEAIW', 'TTELW', 'ZTEUT', etc., along
with many others. To solve this problem, Alice asks you to find a
solution while she works on developing her own language.'''

encrypt_code = {
    '._': 'A', '_...': 'B', '_._.': 'C', '_..': 'D', '.': 'E',
    '.._.': 'F', '__.': 'G', '....': 'H', '..': 'I', '.___': 'J',
    '_._': 'K', '._..': 'L', '__': 'M', '_.': 'N', '___': 'O',
    '.__.': 'P', '__._': 'Q', '._.': 'R', '...': 'S', '_': 'T',
    '.._': 'U', '..._': 'V', '.__': 'W', '_.._': 'X', '_.__': 'Y',
    '__..': 'Z'
}

s = input("Enter the encrypted message:").strip()  # strip() function is used to remove whitespaces and newline 
n = len(s)           # Used to know when decoding is complete
results = []

def dfs(index, current): # index - current position in Morse string; current - decoded letters so far
    if index == n:       # stop condition
        results.append(current)
        return
    for code, letter in encrypt_code.items():     # code - keys of the dictionary; letter - values of the dictionary
        if s.startswith(code, index):      # startwith() function check the string value with code at the given index
            dfs(index + len(code), current + letter) # incrementing the index and updating the decoded letters

dfs(0, "")       # starting decoding from begining
results.sort()   # sort the list of ecoded values in alphabetical order 

for word in results:
    print(word)