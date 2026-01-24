.data
num: .asciz "%d"
x: .long 32
y: .long 255
# debug with gdb
.text
.global main
main: 
    movl x, %eax
    movl y, %ebx

    xorl %ebx, %eax
    xorl %eax, %ebx
    xorl %ebx, %eax

    movl $1, %eax
    xorl %ebx, %ebx
    int $0x80
