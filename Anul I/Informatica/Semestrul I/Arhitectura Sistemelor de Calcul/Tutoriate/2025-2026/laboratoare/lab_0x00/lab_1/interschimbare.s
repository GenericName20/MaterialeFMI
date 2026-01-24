# interschimbarea a doua numere date x si y
.data
x: .space 4
y: .space 4
input: .asciz "input:\n"
putx: .asciz "x = "
puty: .asciz "y = "
readnum: .asciz "%d"
write: .asciz "output: x = %d, y = %d\n"

.text
.global main
main:
    pushl $input
    call printf
    addl $4, %esp

    pushl $putx
    call printf
    addl $4, %esp

    pushl $x
    pushl $readnum
    call scanf
    addl $8, %esp

    pushl $puty
    call printf
    addl $4, %esp

    pushl $y
    pushl $readnum
    call scanf
    addl $8, %esp

    movl x, %eax    # EAX = x
    movl y, %ebx    # EBX = y
    xorl %ebx, %eax # EAX = EAX ^ EBX
    xorl %eax, %ebx # EBX = EAX ^ EBX
    xorl %ebx, %eax # EAX = EAX ^ EBX

    movl %eax, x
    movl %ebx, y
    pushl y
    pushl x
    pushl $write
    call printf
    addl $12, %esp

    movl $1, %eax
    xorl %ebx, %ebx
    int $0x80