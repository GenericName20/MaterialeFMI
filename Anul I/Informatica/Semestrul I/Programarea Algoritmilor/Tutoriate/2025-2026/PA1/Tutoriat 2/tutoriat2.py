# #1
# T=int(input())
#
# text=input().lower()
# sep=".,!?:;-"
#
# for s in sep:
#     text=text.replace(s," ")
#
# # print(text)
#
# cuvinte=[]
# for cuv in text.split():
#     if cuv.isalpha():
#         cuvinte.append(cuv)
#
# n=len(cuvinte)
#
# if T==1:
#     print(n)
#     for cuv in cuvinte:
#         print(cuv)
#
# elif T==2:
#     min_cuv="~"
#     for cuv in cuvinte:
#         if cuv<min_cuv:
#             min_cuv=cuv
#     print(min_cuv)
#
# elif T==3:
#     contor = 0
#     for cuv in cuvinte:
#         if "ini" in cuv:
#             contor += 1
#     print(contor)
#
# elif T==4:
#     print([cuv[::-1] for cuv in cuvinte])
#
#
# elif T==5:
#     contor = 0
#     for cuv in cuvinte:
#         if cuv[-1] == 'a':
#             contor += 1
#     print(contor)
#
# elif T==6:
#     l_min = len(cuvinte[0])
#     l_max = len(cuvinte[0])
#     for cuv in cuvinte:
#         if len(cuv) < l_min:
#             l_min = len(cuv)
#         if len(cuv)>l_max:
#             l_max = len(cuv)
#     print(l_min,l_max)
#
#     #cuvinte.sort(key=len)
#     #print(cuvinte[0],cuvinte[-1])
from fontTools.subset import intersect

# # 2
# text=input().lower()
# sep=".,!?:;-"
#
# for s in sep:
#     text=text.replace(s," ")
#
# # print(text)
#
# cuvinte=[]
# for cuv in text.split():
#     if cuv.isalpha():
#         cuvinte.append(cuv)
#
# n=len(cuvinte)
# gasit=0
#
# for i in range(n-1):
#     cuv1=cuvinte[i]
#     cuv2=cuvinte[i+1]
#
#     if len(cuv1)==len(cuv2):
#         gasit=1
#         print(cuv1,cuv2)
#         break
#
# if gasit==0:
#     print("Nu")


# 3
#acasa
#4
# text = input("Introdu textul: ")
# cuvinte = text.split()
# doar_litere = []
# print(cuvinte)
# for cuv in cuvinte:
#     if not cuv.isalpha() :
#        continue
#     else :
#         doar_litere.append(cuv)
#
# for cuv in doar_litere:
#     print(cuv, " ")

#5
# c = input("Introduceti caracterul: ")
# text = input("Introduceti textul: ")
# for cuv in text.split() :
#     if (cuv.count(c)==2):
#         print(cuv)


#6
# text = input()
# for i in text.split()[::2]:
#     print(i)

# text2= "ama isej veri".split()
# for cuv in text2[:]:
#     print(cuv)
#
# 8
text = input("Introduceti textul: ")
vocale="aeiou"
for cuv in text.split() :
    cnt = 0
    for ch in cuv:
        if ch in vocale:
            cnt+=1

    if cnt>=2:
        print(cuv)






