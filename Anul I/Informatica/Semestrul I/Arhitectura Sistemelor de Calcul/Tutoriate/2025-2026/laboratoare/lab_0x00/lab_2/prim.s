.data
    n: .space 4
    prim: .asciz "PRIM!!\n"
    nepr: .asciz "neprim\n"
    in:   ,asciz "n = "

.text
.global main
main:
    mov $4, %eax
    mov $1, %ebx
    mov $in, %ecx
    mov $7, %edx
    int $0x80
    
    mov $3, %eax
    xor %ebx, %ebx
    mov $n, %ecx
    mov $4, %edx
    int $0x80

    movl x, %eax
    xorl %ecx, %ecx

etloop:
    je 




etexit:
    movl $1, %eax
    xorl %ebx, %ebx
    int $0x80
