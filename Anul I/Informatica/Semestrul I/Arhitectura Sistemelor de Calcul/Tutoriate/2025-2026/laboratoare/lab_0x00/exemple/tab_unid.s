.data
    v: .long 10, 20, 30, 40, 50
    n: .long 5

.text
.global main
main:
    leal v, %edi
    movl n, %ecx

etloop:
    movl n, %eax
    subl %ecx, %eax
    movl (%edi, %eax, 4), %edx
    loop etloop
# weird counter logic, but it works:
# store v[n - i] in %EDX,
# where i = n -> n-1 -> ... -> 1

etexit:
    movl $1, %eax
    xorl %ebx, %ebx
    int $0x80
# because of the instruction logic,
# last element of v (v[4] = 50) is left out
