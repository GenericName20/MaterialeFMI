# ------------------------------------------------------|
# given two numbers x and y in memory                   |
# compute (x / 16) + (y * 16) in 2 methods              |
# ------------------------------------------------------|
# compare the 2 values, print "PASS" if they are equal  |
#                       else, print "FAIL"              |
# ------------------------------------------------------|
# -----------------(x / 16) + (y * 16)------------------|
# I:  x >> 4 + y << 4                                   |
# (closest interpretation of original)                  |
#                                                       |
# II: (x >> 8 + y) << 4                                 |
# (correct, yet erroneous for x's value)                |
# ------------------------------------------------------|

.data
x:    .long 41
y:    .long 67
# x:    .long 2
# y:    .long 3
val1: .space 4
val2: .space 4
afisnum: .asciz "x = %d, y = %d\n"
compar: .asciz "prima varianta  (corecta) = %d\na doua varianta (gresita) = %d\n"
pass: .asciz "PASS\n"
fail: .asciz "FAIL\n"

.text
.global main
main:
#  prima modalitate  #
    movl x, %eax     #
    shr $4, %eax     #
    movl y, %ebx     #
    shl $4, %ebx     #
    addl %ebx, %eax  #
    movl %eax, val1  #
# ------------------ #
# afisarea numerelor #
    pushl y          #
    pushl x          #
    pushl $afisnum   #
    call printf      #
    addl $12, %esp   #
# ------------------ #
# a doua modalitate  #
    movl x, %eax     #
    shr $8, %eax     #
    addl y, %eax     #
    shl $4, %eax     #
    movl %eax, val2  #
# ------------------ #
# ----comparatie---- #
    pushl val2       #
    pushl val1       #
    pushl $compar    #
    call printf      #
    addl $12, %esp   #
# -----PASS/FAIL---- #
    movl val1, %eax  #
    movl val2, %ebx  #
    cmpl %eax, %ebx  #
    je etegale       #
                     #
    movl $4, %eax    #
    movl $1, %ebx    #
    movl $fail, %ecx #
    movl $5, %edx    #
    int $0x80        #
    jmp etexit       #
                     #
etegale:             #
    movl $4, %eax    #
    movl $1, %ebx    #
    movl $pass, %ecx #
    movl $5, %edx    #
    int $0x80        #
# ------------------ #
# --------EXIT------ #
etexit:              #
    movl $1, %eax    #
    xorl %ebx, %ebx  #
    int $0x80        #
# ------------------ #
