# given a, b, c 3 numbers saved in memory and min a 4 byte space
# determine min(a, min(b, c)) and store said value in min

.data
a: .long 6
b: .long 7
c: .long 4
min: .space 4

.text
.global main
main:
    movl a, %eax
    movl b, %ebx
    movl c, %ecx

# # # # # # # # # # # # # # # #
# left-side  = true           #
# right-side = false          #
# # # # # # # # # # # # # # # #
#         |a<b|               #
#        /     \              #
#       /       \             #
#   |a<c|       |b<c|         #
#  /     \     /     \        #
# |a|    |c|  |b|    |c|      #
# # # # # # # # # # # # # # # # 

    