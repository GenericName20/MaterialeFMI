#Problema 6

#a)

# text=input("text: ")
# k=int(input("k= "))
# sir=""

# for l in text:
#     if l.isalpha():
#         if l.islower():
#             l=chr(ord('a')+((ord(l)+k-ord('a')))%26)
#             sir+=l
#         else:
#             l=chr(ord('A')+((ord(l)+k-ord('A')))%26)
#             sir+=l

# print(sir)
# input()

#b)

# text=input("text: ")
# k=int(input("k= "))
# sir=""

# for l in text:
#     if l.isalpha():
#         if l.islower():
#             if ord(l)-(k%26)>=ord('a'):
#                 l=chr(ord(l)-(k%26))
#             else:
#                 l=chr(26+ord(l)-(k%26))
#         else:
#             if ord(l)-(k%26)>=ord('A'):
#                 l=chr(ord(l)-(k%26))
#             else:
#                 l=chr(26+ord(l)-(k%26))
#     sir+=l

# print(sir)
# input()

#Problema 7

#a)

# c=input("text: ")
# s=""

# for i in c:
#     s+=i
#     if i in "aeiouAEIOU":
#         s+='p'+i

# print(s)
# input()

#b)

# c=input("text: ")
# s=""

# for i in "aeiouAEIOU":
#     c=c.replace(f"{i}p{i}",f"{i}")

# print(c)
# input()

# #Problema 8

# c="Astazi am cumparat paine de 5 RON, pe lapte am dat 10 RON, iar de 15 RON am cumparat niste cascaval. De asemenea, mi-am cumparat si niste papuci cu 50 RON!"
# s=0
# L_cuv=c.split()
# for i in L_cuv:
#     if i.isdigit():
#         s+=int(i)

# print(s)
# input()
