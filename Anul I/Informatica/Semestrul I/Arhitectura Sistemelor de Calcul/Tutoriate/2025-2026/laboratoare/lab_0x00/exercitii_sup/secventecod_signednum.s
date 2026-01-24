.data
    ps: .asciz "pozitiv\n" # size_ps = 8 
    zr: .asciz "zero\n"    # size_zr = 5
    ng: .asciz "negativ\n" # size_ng = 8
    sc: .asciz "%d"
    vl: .space 4  

.text
.global main
main:
# (1)
# (a)------------------ #
    andl $1, %eax       #
# (b)------------------ #
    xorl %eax, %eax     #
# (c)------------------ #
    xorl %ebx, %ebx     #
    xorl %ebx, %eax     #
# (d)------------------ #
    movl %eax, %ebx     #
    decl %ebx           #
    andl %ebx, %eax     #
# (e)------------------ #
# (EAX & ~EBX) | (~EAX & EBX) <=> EAX ^ EBX
    xorl %ebx, %eax     #
# (f)------------------ #
# (EAX & ~EAX) | (~EBX & EBX) <=> 0 | 0
    xorl %eax, %eax     #
# (g)------------------ #
# (EAX | ~EBX) & (~EAX | EBX) <=> ~(EAX ^ EBX)
    xorl %ebx, %eax     #
    notl %eax           #
# (h)------------------ #
# (EAX | ~EAX) & (~EBX | EBX) = (-1) & (-1) = -1 
    movl $-1, %eax      #
# (i)------------------ #
# calculează min(EAX, EBX)
    cmpl %ebx, %eax     # compara EAX cu EBX
    cmovg %ebx, %eax    # daca EAX > EBX (greater), muta EBX (minimul) in EAX
# (j)------------------ #
# calculează max(EAX, EBX)
    cmpl %ebx, %eax     # compara EAX cu EBX
    cmovl %ebx, %eax    # daca EAX < EBX (less), muta EBX (maximul) in EAX
# (k)------------------ #
# ECX <- EAX + EBX - ECX
    movl %eax, %edx     #
    addl %ebx, %edx     #
    subl %ecx, %edx     #
    movl %edx, %ecx     #
# (l)---------------------- #
# EBX <- ((EAX × 2 + EBX) × 2 + ECX)/2
    leal (%eax, %eax), %edx #
    addl %ebx, %edx         #
    leal (%edx, %edx), %edx #
    addl %ecx, %edx         #
    shrl $1, %edx           #
    movl %edx, %ebx         #
# (m)------------------ ----#
# EAX <- (EAX + EBX + ECX) × 16
    addl %ebx, %eax     #
    addl %ecx, %eax     #
    shll $4, %eax       #
# (n)------------------ #
# ECX <- (EAX/16) + (EBX × 16)
    movl %eax, %edx     #
    sarl $4, %edx       #
    movl %ebx, %ecx     #
    shll $4, %ecx       #
    addl %edx, %ecx     #
# (o)---------------------- #
# ECX <- (EAX & 0xFFFF0000) + (EBX & 0x0000FFFF)
    movl %eax, %edx         #
    andl $0xFFFF0000, %edx  #
    movl %ebx, %ecx         #
    andl $0x0000FFFF, %ecx  #
    addl %edx, %ecx         #
# (p)---------------------- #
# EAX <- (EAX + EBX) / (EAX + ECX)
    pushl %ebp          #
    movl %eax, %edx     #
    addl %ebx, %edx     #
    movl %eax, %ebp     #
    addl %ecx, %ebp     #
                        #
    movl %edx, %eax     #
    cdq                 #
    idivl %ebp          #
    popl %ebp           #
# (q)------------------ #
# EAX <- (EAX * EBX) / (ECX^2)
    pushl %ebp          #
    movl %ecx, %ebp     #
    imull %ecx, %ebp    #
                        #
# EAX este deja setat   #
    imull %ebx          #
    idivl %ebp          #
    popl %ebp           #
# (r)------------------ #
# EAX <- EAX×((EAX+EBX)/ECX+1)
    pushl %ebp          #
    movl %eax, %ebp     #
    addl %ebx, %eax     #
    cdq                 #
    idivl %ecx          #
    addl $1, %eax       #
    imull %ebp, %eax    #
    popl %ebp           #
# --------------------- #

# (2)
    pushl $vl
    pushl $sc
    call scanf
    addl $8, %esp

    movl vl, %edi
    cmpl $0, %edi
    jle ngzr

    movl $4, %eax
    movl $1, %ebx
    movl $ps, %ecx
    movl $8, %edx
    int $0x80

    jmp exit

ngzr:
    cmpl $0, %edi
    je zero

    movl $4, %eax
    movl $1, %ebx
    movl $ng, %ecx
    movl $8, %edx
    int $0x80

    jmp exit

zero:
    movl $4, %eax
    movl $1, %ebx
    movl $zr, %ecx
    movl $5, %edx
    int $0x80


exit:
    movl $1, %eax
    xorl %ebx, %ebx
    int $0x80
