#WAP to convert numbers

print("1.Binary to Decimal number")
print("2.Decimal to Binary number")
print("3.Hexadecimal to Decimal number")
print("4.Decimal to Hexadecimal number")

op=int(input("Enter conversion type:"))

# Binary to Decimal
if op==1:
    b=int(input("Enter Binary number:"))
    n,d=0,0
    
    while b!=0:
        pv=b%10
        d+=pv*(2**n)
        n+=1
        b=int(b/10)
    print("Decimal number:",d)

# Decimal to Binary
elif op==2:
    d=int(input("Enter Decimal number:"))
    n,b,b1=0,0,1
    #converting decimal no. to {1,0} form
    while d!=0:
        rem=d%2
        b1=(b1*10)+rem
        n+=1
        d=int(d/2)
    #reversing the {1,0} form no. to get binary no.
    while n>0:
        rem=b1%10
        b=(b*10)+rem
        n-=1
        b1=int(b1/10)
    print("Binary number:",b)

# Hexadecimal to Decimal
elif op==3:
    HexDecimal = { 0: 0, 1: 1, 2: 2, 3: 3, 4: 4,5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14,'F': 15 }
    hx = input("Enter Hexadecimal number:")
    d,i = 0,0
    b = []
    n = len(hx)
    b1 = list(hx)
    
    while i <= n:
        #Error Line b1[i] = HexDecimal[b1[i]]
        i+=1
    
    for j in range(n+1):
        b+=b1[j]
    
    while int(b)!=0:
        pv=int(b)%10
        d+=pv*(2**n)
        n+=1
        b=int(b/10)
    print("Decimal number:",d)

# Decimal to Hexadecimal

    
else:
    print("Invalid Conversion choosen.")
