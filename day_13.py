print("Never give up !!")
num=int(input("Enter the number to check wether palindrome or not : "))
org=num
reverse=0
while num > 0:
    last = num % 10
    reverse=reverse*10+last
    num=num//10
if org==reverse:
    print("its a palindrome number : ")
else:
    print("its not an palindrome number ")

--------------------------------------------------------------------------------------------------------------------------------------------------------------


name=str(input("Enter the string to check wether palindrome or not : "))
name=name.lower()
name=name.replace(" ","")
cln =""
for ch in name:
    if ch.isalpha():
        cln+=ch

rev=""                                 # IMPORTANT
for ch in cln:
    rev = ch + rev                      # its (ch + rev)  not !!! (rev + ch)
if cln==rev:
    print("its a palindrome string : ")
else:
    print("its not a palindrome string")

if name==name[::-1]:
    print(name)
    print("its a palindrome  : ")
else:
    print("its not an palindrome  ")



